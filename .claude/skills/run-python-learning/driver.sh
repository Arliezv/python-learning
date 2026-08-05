#!/usr/bin/env bash
# Smoke driver for the python-learning repo.
# Runs every lesson script and checks exit codes (all must be 0).
#
# Usage (paths relative to repo root):
#   .claude/skills/run-python-learning/driver.sh                 # run all lessons
#   .claude/skills/run-python-learning/driver.sh control_flow    # only lessons with "control_flow" in the name
#
# Any script that fails (nonzero exit) makes this driver exit nonzero,
# so it can gate CI or just give a quick "everything works?" check.

set -u
cd "$(dirname "$0")/../../.." || exit 1   # repo root: files here are python-learning/*.py

filter="${1:-}"
scripts=(
  belajar_variabel.py
  belajar_tipedata.py
  belajar_casting.py
  belajar_aritmatika.py
  belajar_operasi_komparasi.py
  operator_assignment.py
  belajar_control_flow.py
)

fail=0
ran=0
outfile="$(mktemp)"

for f in "${scripts[@]}"; do
  if [ -n "$filter" ] && [[ "$f" != *"$filter"* ]]; then
    continue
  fi
  ran=1
  python "$f" >"$outfile" 2>&1
  code=$?
  if [ "$code" -eq 0 ]; then
    printf 'PASS  %s\n' "$f"
  else
    printf 'FAIL  %s (exit %s)\n' "$f" "$code"
    sed 's/^/      /' "$outfile"
    fail=1
  fi
done

rm -f "$outfile"

if [ "$ran" -eq 0 ]; then
  echo "No lesson matched filter: '$filter'"
  exit 1
fi

if [ "$fail" -eq 0 ]; then
  echo "All lesson scripts ran cleanly."
else
  exit 1
fi