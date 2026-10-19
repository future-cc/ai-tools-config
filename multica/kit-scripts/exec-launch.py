#!/usr/bin/env python3
"""Start `npm run execute` detached from the caller's session.

Usage: python3 scripts/exec-launch.py <TASK_DIR> -- <npm run execute arguments...>

The only command this script ever runs is `npm run execute --silent -- <args>`
in the kit directory. It double-forks into a new session so the test run keeps
going after the calling agent session (and its process group / process tree)
is terminated. stdout (which ends with the one-line JSON summary) goes to
<TASK_DIR>/EXEC.out, stderr to <TASK_DIR>/EXEC.err, the pid to <TASK_DIR>/EXEC.pid.

Prints LAUNCHED pid=<pid> or ALREADY_RUNNING pid=<pid>. Check progress with
scripts/exec-status.sh <TASK_DIR>.
"""
import os
import sys
import time

KIT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
TASKS_ROOT = os.path.join(KIT_DIR, ".multica", "tasks")


def fail(message):
    print("ERROR " + message)
    sys.exit(2)


if len(sys.argv) < 4 or sys.argv[2] != "--":
    fail("usage: exec-launch.py <TASK_DIR> -- <npm run execute arguments...>")

task_dir = os.path.realpath(sys.argv[1])
if not task_dir.startswith(TASKS_ROOT + os.sep):
    fail("TASK_DIR must be inside " + TASKS_ROOT)
if not os.path.isdir(task_dir):
    fail("TASK_DIR does not exist: " + task_dir)

args = sys.argv[3:]
cmd = ["npm", "run", "execute", "--silent", "--"] + args

pid_file = os.path.join(task_dir, "EXEC.pid")
if os.path.exists(pid_file):
    try:
        old = open(pid_file).read().strip()
        os.kill(int(old), 0)
        print("ALREADY_RUNNING pid=" + old)
        sys.exit(0)
    except (ProcessLookupError, ValueError):
        pass

for name in ("EXEC.out", "EXEC.err", "EXEC.pid"):
    try:
        os.remove(os.path.join(task_dir, name))
    except FileNotFoundError:
        pass

if os.fork() == 0:
    os.setsid()
    if os.fork() == 0:
        os.chdir(KIT_DIR)
        flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC
        out = os.open(os.path.join(task_dir, "EXEC.out"), flags, 0o644)
        err = os.open(os.path.join(task_dir, "EXEC.err"), flags, 0o644)
        os.dup2(os.open(os.devnull, os.O_RDONLY), 0)
        os.dup2(out, 1)
        os.dup2(err, 2)
        with open(pid_file, "w") as f:
            f.write(str(os.getpid()))
        os.execvp(cmd[0], cmd)
    os._exit(0)
os.wait()

for _ in range(50):
    if os.path.exists(pid_file) and open(pid_file).read().strip():
        break
    time.sleep(0.1)
print("LAUNCHED pid=" + open(pid_file).read().strip())
