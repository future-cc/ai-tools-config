# maestro-testing-kit 里新增的三个脚本

测试执行员靠这三个固定脚本把测试脱离自己的会话运行（结束回复会终止子进程）、检查是否跑完、确保 Dashboard 在运行。它们放在 maestro-testing-kit 的 `scripts/` 目录下，这里是备份副本。

- `exec-launch.py`：`python3 scripts/exec-launch.py <TASK_DIR> -- <npm run execute 的参数>`。只会执行 `npm run execute --silent -- <参数>`，TASK_DIR 必须在工具包的 `.multica/tasks/` 下；双重 fork 脱离会话，输出写到 `<TASK_DIR>/EXEC.out`、`EXEC.err`、`EXEC.pid`。
- `dashboard-ensure.py`：`python3 scripts/dashboard-ensure.py`（不带参数）。Dashboard 已在 4750 端口运行就输出 `DASHBOARD_UP <地址>`，否则脱离会话启动并输出 `DASHBOARD_STARTED …`，失败输出 `DASHBOARD_FAILED …`；不打开浏览器，pid 写入 `.data/dashboard-4750.pid`，`npm run dashboard:stop` 仍可停止。
- `exec-status.sh`：`sh scripts/exec-status.sh <TASK_DIR>`，输出 `NOT_STARTED`、`RUNNING`、`FINISHED <json>` 或 `ABNORMAL`。

恢复到新电脑时：把这三个文件复制回新电脑上工具包的 `scripts/` 目录，并把执行员指令里的工具包路径改成新路径。这两个脚本是放行执行员权限的前提：放行规则只允许运行这几个文件，见执行员 `custom_args`。
