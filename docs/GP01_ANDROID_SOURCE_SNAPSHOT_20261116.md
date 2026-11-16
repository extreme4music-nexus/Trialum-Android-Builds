# GP-01 Android source snapshot

This branch contains a clean file export of public Trialum beta source only; no Git history was transferred. Source origin: extreme4music-nexus/trialum-beta, branch beta/gp-01-living-flora-phyto-20261116, commit 5d0b8f86d37bc79750f22312cc797562238224f4. Exported application/build files are under snapshot/. Private repo history, signing materials, credentials, and server secrets are excluded. The official workflow remains unsigned-only and requires a full SHA plus owner acknowledgment before a manual build. No build was started from this staging operation.

The Android snapshot includes the existing app runtime, assets, locales, Android template, dialogue regression, and GP-01 plant lifecycle regression. The GP-01 test is wired into the branch copy of the build workflow. VersionCode is deliberately unchanged; check the live Play Console track before preparing any candidate.

See docs/GP01_LIVING_FLORA_PHYTOLAB_20261116.md for source provenance and QA boundaries.