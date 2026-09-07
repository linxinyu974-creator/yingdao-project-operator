# yingdao-project-operator

给 AI 智能体使用的影刀/ShadowBot 项目修改说明书。重点是帮助智能体找到真正执行目标行为的流程节点，区分 CodeFlow、可视化流程、网页元素、Profile、数据库和文件层，并在修改后提供可核对的证据。

## 使用方式

将本目录作为 skill 的 supporting files 提供给 AI。触发后先读取 `SKILL.md`，再按任务类型按需读取 `references/`，不要一次性加载全部参考资料。

## 设计原则

- 先确认 app、flow 和调用链，再修改最小真实节点。
- 不按流程名称或注释推断行为，追踪 `process.run`、模块调用和 selector。
- 区分 Profile、页面内、API、direct-URL 四种店铺切换模式。
- 静态诊断通过不等于运行成功；页面打开或文件存在也不等于业务完成。
- 不提交密码、Cookie、验证码、完整账号、数据库连接串、Profile 登录态或真实业务文件。

## 目录

- `SKILL.md`：主路由和执行闭环。
- `references/`：CLI、浏览器、导出、数据完整性、店铺切换和报告模板。
