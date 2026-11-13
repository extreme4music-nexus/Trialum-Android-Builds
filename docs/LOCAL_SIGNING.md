# Local APK signing / Локално потпишување

**Local owner-only process; nothing is signed by public GitHub Actions.**

Prerequisites: an existing owner-controlled Android keystore and alias,
Android SDK Build Tools 36 (or a compatible later version) with
`zipalign` and `apksigner`. Install the SDK tools on your trusted computer.

1. Download the unsigned artifact from the GitHub Actions run.
2. Verify the included SHA256SUMS and inspect `build-info.txt`.
3. Confirm package ID and version; use the correct keystore for that
   package's update history. NEVER reuse the wrong signing key.
4. Run the local helper from a private directory, **outside a publicly
   committed checkout**:

```bash
# On WSL/Linux with Android SDK build-tools on PATH:
bash tools/sign-apk-local.sh \
  /private/downloads/release-unsigned.apk \
  /private/keys/trialum-release.jks \
  YOUR_EXISTING_KEY_ALIAS \
  /private/output/Trialum-release-signed.apk
```

The script does NOT store passwords. `apksigner` asks interactively
for the keystore password/key password. It aligns the unsigned input,
signs the aligned APK, verifies the signature and prints SHA-256.

5. Record the signing certificate fingerprint; compare it with the
   certificate expected for the specific installed package and Play
   App Signing setup. Do not install an APK signed with a different key
   over an existing application.
6. Test update/install and data recovery locally before distribution.

**Android App Bundles (.aab)** require a different signing/upload process;
this APK helper must not be used for AABs.

Never put keystore path/password, signature keys or private signing output
in GitHub Issues, workflow secrets or this public repository.
