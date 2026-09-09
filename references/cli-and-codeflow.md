# 影刀 CLI 与 CodeFlow 参考

## 能力边界

公开的影刀 `shadowbot.shell-cli` 主要用于运行应用、查看任务/日志、管理触发任务和账号；官方 CLI 技能文档明确说明当前版本暂不支持修改应用内部代码，流程开发通常应在影刀客户端完成。本机可能额外启用 Studio/MCP CLI，因此必须先运行当前二进制的 `--help` 并以实际输出为准：只有明确存在且成功返回的编辑命令才能写入。

官方 CLI 规则：只执行真实存在的命令；不猜 flag、app ID 或 task ID；命令不存在时保留原始错误并停止；不确定参数先查 `-h`；路径含空格时加英文引号；运行前确认认证状态。运行应用前先发现 app ID，运行结果取 task ID，再查询状态/日志/停止。优先请求结构化 JSON 输出；向用户只汇报已执行命令和关键字段，不输出 token。

## 个人版运行额度

影刀社区/个人版 CLI 可能限制每日整应用运行次数。任务提交返回 `quota_limited`、`CLI quota denied` 或“今日体验额度已用尽”时，视为任务未被接受：记录原始错误和日期，不重复重试、不改用单个 CodeFlow 冒充整应用验证，也不把此前的静态诊断或旧输出报告为本次成功。若用户仍要求继续，先完成代码、保存和静态诊断等不消耗运行额度的工作；待额度重置或用户切换到有额度的运行环境后，再从整应用入口重新测试。

## 本机入口

默认安装入口：`D:\Program Files\ShadowBot\shadowbot.shell-cli.exe`。

执行前：

```powershell
$env:SWITCH_STUDIO_MCP_CLI_SUPPORT='1'
```

启用 Studio/MCP 支持后，某些本机版本可能提供以下操作：

```powershell
shadowbot.shell-cli studio open --app-id <应用ID>
shadowbot.shell-cli studio app get
shadowbot.shell-cli studio flow list
shadowbot.shell-cli studio flow blocks-list --flow-id <流程ID>
shadowbot.shell-cli studio codeflow read --flow-id <流程ID>
shadowbot.shell-cli studio codeflow write --flow-id <流程ID> --content '@<源文件路径>'
shadowbot.shell-cli studio app save
shadowbot.shell-cli studio diagnostics snapshot
```

以上命令不是公开 CLI 的通用保证，以当前版本的 `--help` 输出为准。需要复制流程时，先准备临时源文件，再执行 copy，避免把业务源文件覆盖到新流程。若命令返回 `unknown command`、`TOOL_DISABLED` 或参数表单不可读，停止猜测并转到影刀客户端。

## CodeFlow 约束

- 顶层入口使用严格形式 `def main(args):`。不要给入口增加参数注解、默认值或多个形参，除非当前版本诊断明确支持。
- 让 `main` 兼容影刀调用模块常见的字典参数；对网页对象、超时、输出目录等做明确校验并给出可读错误。
- 使用影刀提供的 `xbot`、`xbot_visual`、`package`、`glv` 能力时，先确认当前应用已有依赖和版本；不要假定普通 Python 环境等价于影刀运行环境。
- 写入后固定执行“保存 → 静态诊断”。诊断通过后才运行。

## 浏览器与网页

- 需要登录态时，使用指定 Chrome Profile/浏览器环境；不要通过输入账号密码替代用户已有登录态，除非用户明确要求并授权。
- 页面交互使用影刀浏览器元素（稳定 selector、`element.input`、`element.click` 等）。需要下载时，使用保存对话框处理与文件轮询。
- 影刀 CLI 不能可靠读取当前浏览器 DOM 时，读取已有 selector 资源、需求截图或请用户提供页面截图；不要因为“能点击”就猜测页面路径。
- 页面成功打开不代表业务成功。必须确认 URL/页面标题/关键表格标题和数据表头。

## 失败经验固化

- “打开网页”报多个 Chrome 用户环境/插件冲突时，改为明确激活目标 Profile，或由 Python/浏览器连接逻辑直接创建网页对象；不要继续叠加影刀打开网页模块。
- CLI 标准模块目录接口被禁用时，不要用未知参数强行插入模块；保留应用，采用已有模块、CodeFlow 或人工完成一次不可替代的可视化配置。
- 下载得到“订单号（可发货）”等明显不符需求的文件时，判定为错误页面/错误导出，不得报告为成功。重新核对业务入口、表格标题、日期条件和下载按钮，再继续。
- 下载目录可能残留旧的 Excel/CSV，不能按“目录中任意新发现的文件”认定为本次下载；在点击导出前建立目录快照，或用导出调用的时间窗口、文件名模式、大小稳定性和业务表头共同确认文件属于本次任务。目标文件已存在时，必须检测文件 stat 变化或先安全改名，避免把旧文件当新文件或覆盖被占用文件。
- 多账号循环中，Excel 缺少浏览器 ID 的记录要跳过并记录原因；不得借用其他店铺的 Profile。
- 运行卡在浏览器连接时，先关闭重复的目标站点窗口和冲突实例，再做一次最小重试；不要无限等待。

## 最小验证清单

1. `auth current`（或当前 CLI 等价命令）确认会话；不要输出 token。
2. 应用发现命令确认目标 app ID，再读取 flow/CodeFlow。
3. 能力确认后才尝试写入；写入后 `app save`，若支持则执行静态诊断。
4. `static_errors` 为空只代表静态检查通过，不代表运行逻辑正确。
5. 单 Profile、单店铺、单日期跑通。
6. 检查页面上下文和下载文件内容，再扩展到多店铺循环。

## 官方资料

- [影刀 CLI 技能文档](https://www.yingdao.com/yddoc/rpa/zh-CN/958294294025375744?source=cli)
- [影刀官方 shadowbot-cli skill](https://github.com/ying-dao/skills/tree/main/shadowbot-cli)
