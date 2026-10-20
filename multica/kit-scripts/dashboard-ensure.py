#!/usr/bin/env python3
"""Make sure the Dashboard is running on 127.0.0.1:4750; start it detached if not.

Usage: python3 scripts/dashboard-ensure.py   (takes no arguments)

Unlike scripts/dashboard-start.sh this does not open a browser, and the server
is double-forked into its own session so it keeps running after the calling
agent session ends. The pid goes to .data/dashboard-4750.pid, so
`npm run dashboard:stop` still works.

Prints one line: DASHBOARD_UP <url> | DASHBOARD_STARTED <url> pid=<pid> | DASHBOARD_FAILED <reason>
"""
import os
import sys
import time
import urllib.request

KIT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
PORT = "4750"
HOST = "127.0.0.1"
URL = "http://%s:%s/runs" % (HOST, PORT)
DATA_DIR = os.path.join(KIT_DIR, ".data")
PID_FILE = os.path.join(DATA_DIR, "dashboard-%s.pid" % PORT)
LOG_FILE = os.path.join(DATA_DIR, "dashboard-%s.log" % PORT)

if len(sys.argv) > 1:
    print("DASHBOARD_FAILED this script takes no arguments")
    sys.exit(2)


def is_up():
    try:
        with urllib.request.urlopen(URL, timeout=2) as r:
            return r.status == 200
    except Exception:
        return False


if is_up():
    print("DASHBOARD_UP " + URL)
    sys.exit(0)

os.makedirs(DATA_DIR, exist_ok=True)
if os.fork() == 0:
    os.setsid()
    if os.fork() == 0:
        os.chdir(KIT_DIR)
        out = os.open(LOG_FILE, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
        os.dup2(os.open(os.devnull, os.O_RDONLY), 0)
        os.dup2(out, 1)
        os.dup2(out, 2)
        with open(PID_FILE, "w") as f:
            f.write(str(os.getpid()))
        env = dict(os.environ, DASH_PORT=PORT, DASH_HOST=HOST)
        os.execvpe("node", ["node", "dashboard/src/server.js"], env)
    os._exit(0)
os.wait()

for _ in range(30):
    if is_up():
        print("DASHBOARD_STARTED %s pid=%s" % (URL, open(PID_FILE).read().strip()))
        sys.exit(0)
    time.sleep(1)
print("DASHBOARD_FAILED did not answer within 30s, see " + LOG_FILE)
sys.exit(1)
