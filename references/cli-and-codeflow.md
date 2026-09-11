# 应用与流程操作

前置：完成 [环境发现](environment-and-state.md)，$cli 为已验证路径。Studio 命令所在 shell 设置 SWITCH_STUDIO_MCP_CLI_SUPPORT=1。本页标为“写”的操作仅用于用户已授权的开发，不在只读诊断中执行。具体帮助与本机不一致时停止该操作。

## 发现应用与打开编辑器

~~~powershell
& $cli console app --search $appName --page 1 --page-size 20
& $cli console app detail --app-id $appId
~~~

读取实际 app ID、名称、类型、输入定义和版本信息；同名多条先结合路径/类型消歧。分页只返回一页，不得据首屏声称应用不存在。detail 的 inputs（如有）包含 name/type/direction/kind/description/value；只展示本次输入，过滤密码字段。

**打开已有应用（写 UI 状态）：**

~~~powershell
& $cli studio current get
& $cli studio open --app-id $appId
& $cli studio app get
~~~

先读当前应用和任务占用。另一个应用未保存时不覆盖/关闭。必须已在 help 中确认 --app-id；不带它可能创建新应用。打开后验证返回的 app ID 正是目标；不只依据窗口标题。

## 读流程、参数和变量（只读）

~~~powershell
& $cli studio flow list
& $cli studio flow blocks-list --flow-id $flowId --offset 0 --limit 100
& $cli studio flow list-parameters --flow-id $flowId
& $cli studio codeflow read --flow-id $codeFlowId
& $cli studio app globals list
~~~

按 flow 的真实类型选择 blocks-list 或 codeflow read。必要时翻页直到读取完整入口；只读开头几块不能判入口完整。app/flow/codeflow ID 从查询返回取得，不使用演示 ID。全局变量响应可能含秘密，先筛选所需变量。

调用链：app 的实际启动设置 → visual/CodeFlow 内容 → process.run 或模块入口 → 被调函数/selector。启动字段的实际名字随版本变化，以输出或 package.json 为准，不假设一定有 startup_flow_id。

## 修改 CodeFlow（写源码）

局部修改优先精确替换；旧文本必须唯一。大段源码先用允许的文件编辑工具创建 UTF-8 临时源文件，然后：

~~~powershell
& $cli studio codeflow edit --flow-id $codeFlowId --old $oldText --new $newText
# 仅新/空流程或用户要求完整重写时：
& $cli studio codeflow write --flow-id $codeFlowId --content ('@' + $sourcePath)
~~~

write 整体覆盖，不用它掩盖未读取的用户改动；复杂引号/换行不硬塞 shell 参数。新增代码流程使用已确认的 studio flow create --kind code --name $flowName，记录返回 ID；文件存在并不证明已被注册/调用。

## 修改可视化流程（写结构）

1. 读取 catalog blocks --help 和当前目标块；prototype_name 必须来自实际目录/已验证块。
2. 插入 edit-blocks --op insert 的 blocks 仅接受 prototype_name、comment；不在此步猜 inputs。
3. 对返回 block ID 用 blocks-forms 读取实例字段契约，再 fill-blocks。
4. 重新 blocks-list、blocks-forms 验证结构/字段，保存并诊断。

~~~powershell
& $cli studio flow blocks-forms --flow-id $flowId --ranges ('@' + $rangesPath)
& $cli studio flow fill-blocks --flow-id $flowId --fills ('@' + $fillsPath)
~~~

ranges JSON 为 [{start_block_id,end_block_id}]；fills 为 [{block_id,inputs?,outputs?}]，其中字段名只能来自实际表单。接口禁用则停止此条编辑路径，不能凭模块显示名造 prototype 或参数。

## 保存、编译与同步（不同副作用）

~~~powershell
& $cli studio app save
& $cli studio diagnostics snapshot
# 需要关闭本次目标编辑会话并同步时才执行：
& $cli studio current sync
~~~

app save 在本机帮助中说明“保存并编译”；随后检查诊断错误和重读修改内容。current sync 明确是 sync-close，会关闭当前编辑会话，不只是磁盘 flush。保存与关闭不等于发布到云端、订阅者或其他电脑。

修改本地辅助 Python 前阅读 [Python 与生效路径](python-runtime.md)。整应用运行转到 [运行操作](application-entrypoint.md)，不能把 Studio 当前流程默认运行误当整应用。

## 查询不到的其他操作

发布/版本/协作/触发器/扩展等，从当前 console app、console trigger、console extension、mode、ui 的 help 发现。删除、发布、安装扩展、修改触发器有额外影响，不能作为“检查应用”的附带步骤。未经实际帮助验证不提供可直接执行的参数。
