# 调研来源与使用边界

## 影刀官方资料

- [影刀产品介绍](https://www.yingdao.com/product/)（访问于 2026-09-07）：官方页面将影刀描述为可视化流程设计器，并列出 Python/JavaScript 接入、流程录制、元素库/图像库、捕获元素器、云端流程管理、触发器和异常处理。
- [影刀帮助中心](https://www.yingdao.com/qa/)（访问于 2026-09-07）：官方入口指向帮助文档和视频教程。具体 CLI 参数和版本行为仍以本机 `--help`、当前应用输出和官方版本资料为准。
- [影刀 CLI 技能文档](https://www.yingdao.com/yddoc/rpa/zh-CN/958294294025375744?source=cli) 与 [官方 shadowbot-cli skill](https://github.com/ying-dao/skills/tree/main/shadowbot-cli)（访问于 2026-09-07）：CLI 适合运行应用、查看日志、管理任务和账号；公开 CLI 不应被假定为应用内部代码编辑器。要求先认证、再发现 app ID、再运行并用 task ID 查询结果；命令和参数以当前 `--help` 为准。

按需参考的官方操作页：

- [打开网页](https://www.yingdao.com/yddoc/rpa_zh-CN/doc/711591442174164992) · [激活浏览器用户/环境](https://www.yingdao.com/yddoc/rpa_zh-CN/doc/774909497621127168)
- [元素捕获](https://www.yingdao.com/yddoc/rpa_zh-CN/doc/711641172621627392) · [元素锚点](https://www.yingdao.com/yddoc/rpa_zh-CN/doc/752352327687397376) · [AI 辅助定位](https://www.yingdao.com/yddoc/rpa_zh-CN/doc/894823712016261120)
- [调试应用](https://www.yingdao.com/yddoc/rpa_zh-CN/doc/710409639833317376) · [运行日志](https://www.yingdao.com/yddoc/rpa_zh-CN/doc/711834441099194368)
- [未找到元素](https://www.yingdao.com/yddoc/rpa_zh-CN/doc/710832999459700736) · [匹配到多个元素](https://www.yingdao.com/yddoc/rpa_zh-CN/doc/710832037509971968) · [捕获元素变化精确定位](https://www.yingdao.com/yddoc/rpa_zh-CN/doc/710829446672101376)
- [子流程](https://www.yingdao.com/yddoc/rpa_zh-CN/doc/711633902772916224) · [编码模式](https://www.yingdao.com/yddoc/rpa_zh-CN/doc/711632985106923520) · [Python 编码版](https://www.yingdao.com/yddoc/rpa_zh-CN/doc/710947295618007040)
- [调用流程](https://www.yingdao.com/yddoc/rpa_zh-CN/doc/711372669525671936) · [调用模块](https://www.yingdao.com/yddoc/rpa_zh-CN/doc/711371956415758336) · [流程参数](https://www.yingdao.com/yddoc/rpa_zh-CN/doc/711634731514933248)
- [等待网页加载完成](https://www.yingdao.com/yddoc/rpa_zh-CN/doc/711569512514437120) · [点击元素(web)](https://www.yingdao.com/yddoc/rpa_zh-CN/doc/711588345207832576)

从这些页面提炼的可迁移规则是：先确认网页对象和浏览器环境，再定位元素并校验唯一性；区分页面整体加载等待与元素等待；元素未找到时检查对象、属性变化、悬停状态和等待，而不是直接猜 XPath；AI 辅助定位是运行时临时兜底，不能被报告为已永久写入源文件。

这些页面用于确认产品能力边界，不用于推断某个业务站点的 URL、DOM 或 API。业务页面变化时，重新读取当前 selector、网络请求和运行日志。

## AI skill 设计资料

- [Claude Code Skills 文档](https://code.claude.com/docs/en/skills)（访问于 2026-09-07）：说明 description 是触发路由，详细内容应按需放入 supporting files，主 `SKILL.md` 保持简洁，并建议分别评估“是否触发”和“输出是否正确”。

据此将本 skill 设计为：主文件只放任务路由、调用链和安全边界；平台细节放 references；验证报告要求区分观察、修改、证据和未验证项。

## 证据等级

1. 当前应用代码、CLI 输出和实际运行结果：最高优先级。
2. 影刀官方文档/帮助中心：用于平台能力和术语边界。
3. 社区文章、搜索摘要和历史对话：只用于形成假设，必须回到前两级验证后才能写入稳定规则。
