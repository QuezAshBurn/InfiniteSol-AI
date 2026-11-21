from hashlib import sha256
from pathlib import Path
import argparse
import json


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('expected_sha256', help='Manifest SHA-256 from the approved handoff')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    manifest = root / 'manifest.json'
    actual_hash = digest(manifest)
    if actual_hash != args.expected_sha256.lower():
        parser.exit(1, 'BLOCKED: manifest SHA-256 differs from the handoff.\n')
    record = json.loads(manifest.read_text(encoding='utf-8'))
    files = {p.relative_to(root).as_posix(): digest(p) for p in root.rglob('*')
             if p.is_file() and p != manifest}
    if files != record['files']:
        parser.exit(1, 'BLOCKED: installed skill files differ from the manifest.\n')
    print(json.dumps({'skill': record['skill'], 'version': record['version'],
                      'manifestSha256': actual_hash, 'sourcePack': record['sourcePack']}))


if __name__ == '__main__':
    main()
