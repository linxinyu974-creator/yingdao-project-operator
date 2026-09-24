# yingdao-rpa-operator

面向 Windows 影刀/ShadowBot 的统一操作技能。它把官方 CLI 的命令纪律、社区技能的机器人管理/API/可视化块经验，以及本地 `yingdao-project-operator` 的调用链、运行证据和交付边界合并为一个独立入口。

技能只负责指导代理如何发现、修改、运行、诊断和交付影刀应用；不会自动保存账号密码、Cookie 或验证码，也不会把社区版、企业 API 和特定安装路径混为一谈。

## 使用

将本目录作为独立 skill 安装到 Codex/Claude 的 skills 目录，入口为 `SKILL.md`。先按任务路由读取主文件，再按需读取 `references/`。脚本均为只读或离线校验：

```powershell
python scripts/operator_probe.py
python scripts/validate_skill.py --root .
python scripts/test_operator_tools.py
```

详细内容位于 `references/`；来源取舍记录在 `references/cli-mcp-and-runtime.md`。
