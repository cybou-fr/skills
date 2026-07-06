#!/bin/bash
set -e

SCRIPTS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="$(dirname "$SCRIPTS_DIR")"

echo "=== Running all skill validation scripts ==="
cd "$SKILLS_DIR"

failed=0

for script in "$SCRIPTS_DIR"/validate_*.py; do
    echo "Running $(basename "$script")..."
    if ! python3 "$script"; then
        echo "❌ $(basename "$script") FAILED"
        failed=1
    else
        echo "✓ $(basename "$script") PASSED"
    fi
    echo "----------------------------------------"
done

if [ $failed -ne 0 ]; then
    echo "=== Validation FAILED! ==="
    exit 1
else
    echo "=== All validations PASSED! ==="
    exit 0
fi
