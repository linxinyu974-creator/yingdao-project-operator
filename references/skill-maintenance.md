# 技能维护、同步与验收

同时区分源仓库、远端分支、Codex 安装副本。先读状态，再写入：

~~~powershell
git -C $repo status -sb
git -C $repo log -1 --oneline
git -C $repo ls-remote origin refs/heads/master
& $python .\scripts\verify_skill.py --root $repo --installed $installed
~~~

内容版本以文件哈希为准，不以目录名或聊天记录为准。先提交给用户查看；用户明确要求发布后才 commit/push。dirty tree 有用户改动时不覆盖。源仓库更新后将同一组文件复制到安装副本，随后再次 verify；复制不等于 GitHub 发布，push 不等于当前 Codex 进程已经重载。

每次维护前先读 [持续改进机制](continuous-improvement.md)，检查本次候选项的证据和适用范围。只采纳经过门槛的最小规则；候选项没有事实支撑、仅适用于某个业务页面或与现有规则重复时，记录拒绝原因而不改技能。不得把候选项队列当作自动发布队列。

验收层级：frontmatter/链接；脚本 py_compile 和回归测试；当前 CLI help 契约；情景审查（额度、运行中任务、验证码、弹窗、旧文件、空入口）；必要时才做最小整应用测试。离线通过不冒充 E2E。

报告源目录、安装目录、哈希比较、测试、未做的发布/运行/跨电脑验证。不得自动删除旧副本或用户历史文件。
