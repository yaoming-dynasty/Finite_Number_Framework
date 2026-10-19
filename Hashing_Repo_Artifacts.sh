#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$repo_root"

echo "============================================="
echo "Running SHA-256 Hashing for Repository Artifacts"
echo "============================================="

while IFS= read -r -d '' file; do
    hash_val=$(sha256sum -- "$file" | awk '{print $1}')
    printf '[+] %s -> %s\n' "$file" "$hash_val"
done < <(
    find . -type f \( -name '*.md' -o -name 'gates.py' \) -print0 | sort -z
)

echo "============================================="
echo "Hashing complete. Update fingerprint tables with computed values."
