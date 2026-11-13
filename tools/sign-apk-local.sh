#!/usr/bin/env bash
# Owner-only local APK signing. No network or GitHub signing.
set -euo pipefail
umask 077

if (( $# != 4 )); then
  printf 'Usage: %s UNSIGNED.apk KEYSTORE.jks KEY_ALIAS SIGNED_OUTPUT.apk\n' "$0" >&2
  exit 2
fi

input="$1"
keystore="$2"
alias="$3"
output="$4"

for cmd in zipalign apksigner sha256sum mktemp; do
  command -v "$cmd" >/dev/null 2>&1 || {
    printf 'Missing local Android SDK tool: %s\n' "$cmd" >&2
    exit 1
  }
done

[[ -s "$input" ]] || { echo "Unsigned input APK not found" >&2; exit 1; }
[[ -f "$keystore" ]] || { echo "Keystore not found" >&2; exit 1; }
[[ "$input" == *.apk && "$output" == *.apk ]] || {
  echo "This helper signs APK files only, not AAB files" >&2
  exit 1
}
[[ "$(realpath -m "$input")" != "$(realpath -m "$output")" ]] || {
  echo "Refusing to overwrite input APK" >&2
  exit 1
}
[[ ! -e "$output" ]] || {
  echo "Refusing to overwrite existing signed output" >&2
  exit 1
}
if apksigner verify "$input" >/dev/null 2>&1; then
  echo "Input APK appears to be signed already; refusing to re-sign" >&2
  exit 1
fi

outdir="$(dirname "$output")"
[[ -d "$outdir" ]] || { echo "Output directory missing: $outdir" >&2; exit 1; }
temp="$(mktemp "$outdir/.trialum-aligned-XXXXXXXX.apk")"
trap 'rm -f -- "$temp"' EXIT

zipalign -p -f 4 "$input" "$temp"
zipalign -c -p 4 "$temp"
# Prompts for passwords interactively, no passwords on CLI or in repository.
apksigner sign --ks "$keystore" --ks-key-alias "$alias" --out "$output" "$temp"
apksigner verify --verbose --print-certs "$output"
sha256sum "$output"
echo "Local APK signing and verification complete. No GitHub signing performed."
