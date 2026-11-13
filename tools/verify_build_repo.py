#!/usr/bin/env python3
"""Basic main-branch CI policy gate. Never a substitute for manual security review."""
from pathlib import Path
import subprocess
import sys
import re

root = Path(__file__).resolve().parents[1]
tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=root).split(b"\0")
paths = [Path(x.decode("utf-8")) for x in tracked if x]
errors = []

for path in paths:
    text = path.as_posix()
    if path.parts[0] == "snapshot":
        errors.append("Game snapshot must not be committed to tooling main: " + text)
    if any(p in {".ssh", "secrets", "backups"} for p in path.parts):
        errors.append("Forbidden private directory: " + text)
    if path.suffix.lower() in {".apk", ".aab", ".jks", ".keystore", ".p12", ".pfx", ".pem", ".key"}:
        errors.append("Forbidden binary/signing file: " + text)
    if path.name.startswith(".env") or path.name in {"google-services.json", "service-account.json"}:
        errors.append("Forbidden credential file: " + text)

for required in [
    "README.md", "LICENSE", "BUILD_POLICY.md", "SECURITY.md",
    ".github/workflows/android-unsigned.yml", "tools/sign-apk-local.sh",
    "docs/LOCAL_SIGNING.md"
]:
    if Path(required) not in paths:
        errors.append("Required build-center file missing: " + required)

wf = root / ".github/workflows/android-unsigned.yml"
if wf.exists():
    content = wf.read_text(encoding="utf-8")
    for bad in ["pull_request_target:", "contents: write", "secrets.", "apksigner sign", "gradle publish"]:
        if bad in content:
            errors.append("Forbidden CI functionality in workflow: " + bad)
    for need in ["workflow_dispatch:", "persist-credentials: false", "contents: read", "unsigned-apks:", "build-policy:"]:
        if need not in content:
            errors.append("Missing expected CI restriction: " + need)

print("Android build infrastructure policy:", "FAIL" if errors else "PASS")
for err in errors:
    print(err)
if not errors:
    print("Basic policy gate PASS. Not a source, licensing or secret-audit certification.")
sys.exit(bool(errors))
