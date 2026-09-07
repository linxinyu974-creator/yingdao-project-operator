# 影刀 CLI 与 CodeFlow 参考

## 本机入口

默认安装入口：`D:\Program Files\ShadowBot\shadowbot.shell-cli.exe`。

执行前：

```powershell
$env:SWITCH_STUDIO_MCP_CLI_SUPPORT='1'
```

常用操作：

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

以当前 CLI 版本的 `--help` 输出为准；不要凭旧记忆编造参数。需要复制流程时，先准备临时源文件，再执行 copy，避免把业务源文件覆盖到新流程。

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
- 多账号循环中，Excel 缺少浏览器 ID 的记录要跳过并记录原因；不得借用其他店铺的 Profile。
- 运行卡在浏览器连接时，先关闭重复的目标站点窗口和冲突实例，再做一次最小重试；不要无限等待。

## 最小验证清单

1. `flow list` 与 `codeflow read` 确认修改的是目标流程。
2. `codeflow write` 后 `app save`。
3. `diagnostics snapshot` 的 `static_errors` 为空。
4. 单 Profile、单店铺、单日期跑通。
5. 检查下载文件存在、大小合理、能读取、表头正确。
6. 再扩展到多店铺循环，并输出成功/失败/跳过统计。
