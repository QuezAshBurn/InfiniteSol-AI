from datetime import datetime
from hashlib import sha256
import json
from pathlib import Path
from shutil import copytree
from tempfile import TemporaryDirectory
import unittest

from rule_memory import FIXTURE_SHA256, PROJECT, ReaderGrant, RuleMemory


FIXTURE = Path(__file__).resolve().parents[1] / "snapshot"
RULE = "INVOICE.POD_REQUIRED"
INVARIANT = "PLATFORM.TENANT_ISOLATION"


class RuleMemoryTests(unittest.TestCase):
    def setUp(self):
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name) / "snapshot"
        copytree(FIXTURE, self.root)
        self.when = "2026-11-20T12:00:00+08:00"
        self.digest = FIXTURE_SHA256

    def read(self, rule=RULE, *, tenant="tenant-a", project=PROJECT, role="qa"):
        grant = ReaderGrant(project, tenant, role)
        memory = RuleMemory(self.root, grant, expected_digest=self.digest,
                            clock=lambda: datetime.fromisoformat(self.when))
        return memory.lookup(rule)

    def update_manifest(self, change):
        path = self.root / "manifest.json"
        snapshot = json.loads(path.read_bytes())
        change(snapshot["records"])
        path.write_text(json.dumps(snapshot), encoding="utf-8")
        self.digest = sha256(path.read_bytes()).hexdigest()

    def test_effective_rules_match_tenant_and_approval(self):
        first, second = self.read(), self.read(tenant="tenant-b")
        self.assertEqual(first["status"], "RESOLVED")
        self.assertEqual((first["kind"], first["revision"], first["approval_id"]),
                         ("override", "r2", "SYN-DEC-002"))
        self.assertEqual(first["shared_approval_id"], "SYN-DEC-001")
        self.assertIn("supervisor approves", first["markdown"])
        self.assertEqual((second["kind"], second["revision"], second["approval_id"]),
                         ("default", "r1", "SYN-DEC-001"))
        self.assertNotIn("supervisor", second["markdown"])
        for result in (first, second):
            body = (self.root / result["source"]).read_bytes()
            self.assertEqual(sha256(body).hexdigest(), result["source_sha256"])
            approval = (self.root / result["approval_source"]).read_text(encoding="utf-8")
            self.assertIn(result["source_sha256"], approval)

    def test_platform_invariant_applies_to_both_tenants(self):
        for tenant in ("tenant-a", "tenant-b"):
            result = self.read(INVARIANT, tenant=tenant)
            self.assertEqual((result["status"], result["kind"], result["approval_id"]),
                             ("RESOLVED", "invariant", "SYN-DEC-003"))

    def test_denial_precedes_storage_lookup(self):
        (self.root / "manifest.json").unlink()
        for wrong_scope in ({"tenant": "tenant-c"}, {"project": "other"}, {"role": "marketing"}):
            self.assertEqual(self.read(**wrong_scope), {"status": "DENIED"})

    def test_missing_grant_is_denied(self):
        memory = RuleMemory(self.root, None, expected_digest=self.digest)
        self.assertEqual(memory.lookup(RULE), {"status": "DENIED"})

    def test_unknown_rule_and_invalid_request_are_distinct(self):
        self.assertEqual(self.read("INVOICE.OTHER")["status"], "NOT_FOUND")
        self.assertEqual(self.read("invoice.pod required"), {"status": "INVALID_RULE_ID"})

    def test_one_tenants_unavailable_document_does_not_affect_the_other(self):
        (self.root / "rules/invoice-tenant-a.md").unlink()
        self.assertEqual(self.read()["status"], "UNAVAILABLE")
        self.assertEqual(self.read(tenant="tenant-b")["kind"], "default")

    def test_override_effective_start_included(self):
        self.update_manifest(lambda rows: rows[1].update(effective_from="2026-11-20T13:00:00+08:00"))
        self.assertEqual(self.read()["kind"], "default")
        self.when = "2026-11-20T05:00:00+00:00"
        self.assertEqual(self.read()["kind"], "override")

    def test_override_effective_end_excluded(self):
        self.update_manifest(lambda rows: rows[1].update(effective_until="2026-11-20T12:00:00+08:00"))
        self.assertEqual(self.read()["kind"], "default")

    def test_expired_active_approval_blocks_default(self):
        self.update_manifest(lambda rows: rows[1]["approval"].update(expires_at=self.when))
        self.assertEqual(self.read()["status"], "BLOCKED")

    def test_draft_and_mismatched_approval_block_default(self):
        self.update_manifest(lambda rows: rows[1]["approval"].update(status="draft"))
        self.assertEqual(self.read()["status"], "BLOCKED")
        self.update_manifest(lambda rows: rows[1]["approval"].update(status="approved", revision="r3"))
        self.assertEqual(self.read()["status"], "BLOCKED")

    def test_conflicting_active_overrides_block_default(self):
        self.update_manifest(lambda rows: rows.append(dict(rows[1], revision="r3")))
        self.assertEqual(self.read()["status"], "BLOCKED")

    def test_invariant_cannot_be_overridden(self):
        self.update_manifest(lambda rows: rows.append(dict(rows[1], rule_id=INVARIANT)))
        self.assertEqual(self.read(INVARIANT)["status"], "BLOCKED")

    def test_changed_rule_body_is_unavailable(self):
        (self.root / "rules/invoice-tenant-a.md").write_text("Unpublished text", encoding="utf-8")
        self.assertEqual(self.read()["status"], "UNAVAILABLE")

    def test_missing_approval_is_unavailable(self):
        (self.root / "approvals/SYN-DEC-002.md").unlink()
        self.assertEqual(self.read()["status"], "UNAVAILABLE")

    def test_approval_document_must_match_even_with_a_valid_hash(self):
        path = self.root / "approvals/SYN-DEC-002.md"
        decision = path.read_text(encoding="utf-8").replace("tenant-a.", "tenant-b.")
        path.write_text(decision, encoding="utf-8")
        digest = sha256(path.read_bytes()).hexdigest()
        self.update_manifest(lambda rows: rows[1]["approval"].update(sha256=digest))
        self.assertEqual(self.read()["status"], "BLOCKED")

    def test_conflicting_decision_lines_block(self):
        path = self.root / "approvals/SYN-DEC-002.md"
        with path.open("a", encoding="utf-8") as approval:
            approval.write("\nDecision: Revoked.\n")
        digest = sha256(path.read_bytes()).hexdigest()
        self.update_manifest(lambda rows: rows[1]["approval"].update(sha256=digest))
        self.assertEqual(self.read()["status"], "BLOCKED")

    def test_conflicting_approval_source_link_blocks(self):
        path = self.root / "approvals/SYN-DEC-002.md"
        decision = path.read_text(encoding="utf-8").replace("invoice-tenant-a.md", "invoice-shared.md")
        path.write_text(decision, encoding="utf-8")
        digest = sha256(path.read_bytes()).hexdigest()
        self.update_manifest(lambda rows: rows[1]["approval"].update(sha256=digest))
        self.assertEqual(self.read()["status"], "BLOCKED")

    def test_snapshot_digest_remains_bound_after_change(self):
        original_pin = self.digest
        self.assertEqual(self.read()["status"], "RESOLVED")
        self.update_manifest(lambda rows: rows.clear())
        self.digest = original_pin
        self.assertEqual(self.read(), {"status": "UNAVAILABLE"})
