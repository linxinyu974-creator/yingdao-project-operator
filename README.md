# yingdao-project-operator

给 AI 智能体使用的技能集合。目前包含影刀/ShadowBot 项目修改说明书，以及独立的结构化思考工具箱。影刀技能重点是帮助智能体找到真正执行目标行为的流程节点，区分 CodeFlow、可视化流程、网页元素、Profile、数据库和文件层，并在修改后提供可核对的证据。

## 使用方式

使用影刀技能时，将仓库根目录作为 skill 的 supporting files 提供给 AI。触发后先读取 `SKILL.md`，再按任务类型按需读取 `references/`，不要一次性加载全部参考资料。

使用结构化思考工具箱时，将 `structured-thinking-toolkit/` 作为独立 skill 提供给 AI，并从其 `SKILL.md` 开始按需读取参考资料。

## 设计原则

- 先确认 app、flow 和调用链，再修改最小真实节点。
- 不按流程名称或注释推断行为，追踪 `process.run`、模块调用和 selector。
- 区分 Profile、页面内、API、direct-URL 四种店铺切换模式。
- 静态诊断通过不等于运行成功；页面打开或文件存在也不等于业务完成。
- 整应用运行前先验证 startup flow 真实编排；空入口的成功结束、短耗时和“开始/结束”日志只能判定为空跑风险。
- 不提交密码、Cookie、验证码、完整账号、数据库连接串、Profile 登录态或真实业务文件。
- 每次任务终态进行可审计的学习检查；只有可复现、可泛化且经授权的结论才会进入技能规则。

## 目录

- `SKILL.md`：主路由和执行闭环。
- `references/`：CLI、浏览器、元素调试、导出、数据完整性、店铺切换、应用入口和报告模板。
- `CHANGELOG.md`：版本变更记录。
- `references/continuous-improvement.md`：每次调用后的学习候选、证据门槛与采纳规则。
- `structured-thinking-toolkit/`：独立的澄清、学习研究、解题验证、决策实验与反思技能。
