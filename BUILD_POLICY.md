# Android-only build policy

## Repositories

- `extreme4music-nexus/Trialum` — PRIVATE development, tests and unfinished LW phases.
- `extreme4music-nexus/trialum-beta` — PUBLIC only after owner-approved beta-source release.
- `extreme4music-nexus/Trialum-Android-Builds` — PUBLIC build infrastructure and
  specifically approved already-public source snapshots for unsigned Android QA.

## Boundary

The default branch is only tooling and documentation. Do NOT automatically copy
private source, complete Git history, private branches, worklogs, credentials,
home-server configs, users' backups or model packages into this repository.

The build workflow is manually initiated by the GitHub account owner only.
Input is the immutable full commit SHA of a snapshot ALREADY PUBLIC in this
repository. Snapshot visibility/rights review must happen BEFORE any push.
The workflow cannot fetch or inspect the private repository.

Public runners must not possess, create, import, reuse or rotate any official
release-signing keys. Build tools may run unsigned compilation and tests.
Only locally controlled `zipalign` / `apksigner` may sign official artifacts.

## Output

The build produces candidate unsigned APK files for these application IDs:
- `com.trialum.ziivaiskra` — release candidate, UNSIGNED
- `com.trialum.ziivaiskra.signqa` — signing QA candidate, UNSIGNED
- `com.trialum.ziivaiskra.signdebug` — friends debug candidate, UNSIGNED

These are NOT approved public releases. Check version, signing identity,
backup/restore migration and install/update behavior on owner devices before
distribution. Never auto-deploy to Play Console or a home server.

## Older branch and historical licenses

The public `ci/lw-c-android-unsigned-20261113` branch contains source
from an earlier experiment. It cannot be made confidential merely by changing
the default branch or deleting the workflow. Review it before reuse.

Historical GPL-3.0 and MIT notices and any earlier grants continue to apply
where legally effective. See docs/PRIOR_LICENSES.md.
