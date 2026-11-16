# GP-01 Android source snapshot

This branch contains a clean file export of public Trialum beta source only; no Git history was transferred. Source origin: extreme4music-nexus/trialum-beta, branch beta/gp-01-living-flora-phyto-20261116, commit 5803d3cd9c9bcf10761b2383f3e7e405881b1c79. Exported application/build files are under snapshot/. Private repo history, signing materials, credentials, and server secrets are excluded. CI tooling remains on main and retains its unsigned-only, full-source-SHA, explicit-acknowledgment gate. No build was started from this staging operation.

The Android snapshot includes the existing app runtime, assets, locales, Android template, dialogue regression, and GP-01 plant lifecycle regression. The main-branch workflow currently runs the dialogue regression; the GP-01 regression is wired into the beta repository Actions workflow. Do not use this snapshot until its exact source SHA has been selected in the Android Build workflow and the Play Console version code has been checked. VersionCode is deliberately unchanged.

See docs/GP01_LIVING_FLORA_PHYTOLAB_20261116.md for source provenance and QA boundaries.
