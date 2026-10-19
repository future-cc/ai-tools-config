#!/bin/sh
# Report the state of a run started by scripts/exec-launch.py.
# Usage: sh scripts/exec-status.sh <TASK_DIR>
# Prints one of:
#   NOT_STARTED        no EXEC.pid in TASK_DIR
#   RUNNING            the process is still alive
#   FINISHED <json>    the process ended and the last line of EXEC.out is the kit's JSON summary
#   ABNORMAL           the process ended without a JSON summary (killed or crashed)
KIT=$(cd "$(dirname "$0")/.." && pwd -P)
D="$1"
[ -n "$D" ] && [ -d "$D" ] || { echo "ERROR TASK_DIR missing"; exit 2; }
D=$(cd "$D" && pwd -P)
case "$D" in
  "$KIT"/.multica/tasks/*) ;;
  *) echo "ERROR TASK_DIR must be inside $KIT/.multica/tasks"; exit 2 ;;
esac
PID=$(cat "$D/EXEC.pid" 2>/dev/null)
if [ -z "$PID" ]; then
  echo NOT_STARTED
elif kill -0 "$PID" 2>/dev/null; then
  echo RUNNING
else
  LAST=$(tail -n 1 "$D/EXEC.out" 2>/dev/null)
  case "$LAST" in
    \{*) echo "FINISHED $LAST" ;;
    *) echo ABNORMAL ;;
  esac
fi
