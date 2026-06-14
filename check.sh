#!/usr/bin/env bash
set -uo pipefail; cd "$(dirname "$0")"; fail=0
report(){ if [ "$2" -eq 0 ]; then echo "  PASS  $1"; else echo "  FAIL  $1"; fail=1; fi; }
out=$(python3 legibility_kit.py audit demo_system); code=$?
{ [ "$code" -eq 1 ] && grep -q "6 findings" <<<"$out"; }; report "Demo shows the planted defects" $?
python3 - <<'PY'
import sys; sys.exit(0 if all(ord(c)<127 for c in open("legibility_kit.py",encoding="utf-8").read()) else 1)
PY
report "ASCII core" $?
[ "$fail" -eq 0 ] && echo GREEN || echo FAIL; exit $fail
