# Security policy

**No credentials or signing operations in GitHub Actions.**

Never commit or attach:
- `*.jks`, `*.keystore`, `*.p12`, private keys or signing passwords;
- Play Console credentials, Firebase service-account credentials or tokens;
- real personal backups, users' messages, server secrets or private deployment data.

The unsigned CI runner uses `GITHUB_TOKEN` with `contents: read` only,
never private-repository access and never official Android signing.

To report a vulnerability, use private vulnerability reporting in this
repository when enabled. Otherwise open an Issue asking for a private
contact channel, WITHOUT describing the flaw publicly.

Only the owner may authorize source publication, official signing and release.
