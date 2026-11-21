"""Read an exact business rule from the pinned synthetic Markdown snapshot."""

from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re


PROJECT = "nimbusflow-synthetic"
TENANTS = ("tenant-a", "tenant-b")
READER_ROLES = ("business-analyst", "developer", "qa")
FIXTURE_SHA256 = "baa7cf19c58515e17f6d4d95355acfe37466596c0832edbe04665f4290f40ad4"


class SnapshotUnavailable(Exception):
    """Required files are missing or differ from the published snapshot."""


@dataclass(frozen=True)
class ReaderGrant:
    project: str
    tenant: str
    role: str


def _timestamp(value):
    moment = datetime.fromisoformat(value)
    if moment.utcoffset() is None:
        raise ValueError("Time must include an offset")
    return moment


def _is_effective(record, as_of):
    start = _timestamp(record["effective_from"])
    end = _timestamp(record["effective_until"]) if record["effective_until"] else None
    if end is not None and end <= start:
        raise ValueError("Invalid effective interval")
    return start <= as_of and (end is None or as_of < end)


class RuleMemory:
    """Bind the snapshot and synthetic grant in a trusted local launcher."""

    def __init__(self, root, grant, *, expected_digest, clock=None):
        self.root = Path(root).resolve()
        self.grant = grant
        self.expected_digest = expected_digest
        self.clock = clock or (lambda: datetime.now(timezone.utc))

    def _read_pinned(self, relative_path, expected_digest):
        path = (self.root / relative_path).resolve()
        if not path.is_relative_to(self.root):
            raise SnapshotUnavailable()
        data = path.read_bytes()
        if sha256(data).hexdigest() != expected_digest:
            raise SnapshotUnavailable()
        return data

    def _load_published(self, record, as_of):
        approval = record["approval"]
        if (approval["status"] != "approved"
                or approval["scope"] != (record["tenant"] or "shared")
                or approval["revision"] != record["revision"]
                or approval["source_sha256"] != record["sha256"]
                or _timestamp(approval["approved_at"]) > as_of
                or (approval["expires_at"] is not None
                    and as_of >= _timestamp(approval["expires_at"]))):
            raise ValueError("No matching current approval")
        decision = self._read_pinned(approval["path"], approval["sha256"]).decode("utf-8")
        lines = decision.splitlines()
        expected_fields = {
            "Decision: ": "Approved for this fixture.",
            "Approver: ": f'{approval["approver"]}.',
            "Approved at: ": f'{approval["approved_at"]}.',
            "Scope: ": f'NimbusFlow synthetic pilot, {approval["scope"]}.',
            "Rule: ": f'{record["rule_id"]} {record["revision"]}.',
            "Source: ": f'[{Path(record["source"]).stem}](../{record["source"]}).',
            "Source SHA-256: ": record["sha256"],
        }
        if not lines or lines[0] != f'# {approval["id"]} | Synthetic approval':
            raise ValueError("Approval document does not match the rule")
        for prefix, value in expected_fields.items():
            matching = [line for line in lines if line.startswith(prefix)]
            if matching != [prefix + value]:
                raise ValueError("Approval field does not match the rule")
        return self._read_pinned(record["source"], record["sha256"]).decode("utf-8")

    def lookup(self, rule_id):
        if (not isinstance(self.grant, ReaderGrant)
                or self.grant.project != PROJECT or self.grant.tenant not in TENANTS
                or self.grant.role not in READER_ROLES):
            return {"status": "DENIED"}
        if not isinstance(rule_id, str) or not re.fullmatch(r"[A-Z][A-Z0-9_.]{0,79}", rule_id):
            return {"status": "INVALID_RULE_ID"}

        try:
            manifest = json.loads(self._read_pinned("manifest.json", self.expected_digest))
            if not isinstance(manifest, dict) or manifest.get("project") != PROJECT:
                raise SnapshotUnavailable()
            records = manifest["records"]
            if not isinstance(records, list) or any(
                    not isinstance(row, dict) or "rule_id" not in row or "tenant" not in row
                    for row in records):
                raise SnapshotUnavailable()
            snapshot = manifest["snapshot"]
        except (OSError, SnapshotUnavailable, KeyError, ValueError):
            return {"status": "UNAVAILABLE"}

        try:
            as_of = self.clock()
            if as_of.utcoffset() is None:
                raise ValueError("Time must include an offset")
            active = [
                row for row in records
                if row["rule_id"] == rule_id and row["tenant"] in (None, self.grant.tenant)
                and _is_effective(row, as_of)
            ]
            shared = [row for row in active if row["tenant"] is None]
            overrides = [row for row in active if row["tenant"] is not None]

            if not active:
                return {"status": "NOT_FOUND", "snapshot": snapshot}
            if len(shared) != 1 or len(overrides) > 1:
                raise ValueError("Conflicting or missing shared authority")
            shared_rule = shared[0]
            if shared_rule["kind"] not in {"default", "invariant"}:
                raise ValueError("Invalid shared rule type")
            shared_text = self._load_published(shared_rule, as_of)

            record, body = shared_rule, shared_text
            if overrides:
                override = overrides[0]
                if (shared_rule["kind"] != "default" or shared_rule["overridable"] is not True
                        or override["kind"] != "override"):
                    raise ValueError("Override outside the shared rule's authority")
                record, body = override, self._load_published(override, as_of)

            return {
                "status": "RESOLVED", "snapshot": snapshot,
                "snapshot_sha256": self.expected_digest, "as_of": as_of.isoformat(),
                "project": self.grant.project, "tenant": self.grant.tenant, "rule_id": rule_id,
                "kind": record["kind"], "revision": record["revision"],
                "source": record["source"], "source_sha256": record["sha256"],
                "effective_from": record["effective_from"], "effective_until": record["effective_until"],
                "approval_id": record["approval"]["id"], "approval_source": record["approval"]["path"],
                "approver": record["approval"]["approver"],
                "shared_revision": shared_rule["revision"], "shared_approval_id": shared_rule["approval"]["id"],
                "markdown": body,
            }
        except (OSError, SnapshotUnavailable, UnicodeDecodeError):
            return {"status": "UNAVAILABLE", "snapshot": snapshot}
        except (KeyError, TypeError, ValueError):
            return {"status": "BLOCKED", "snapshot": snapshot}
