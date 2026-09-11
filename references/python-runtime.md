# Python、CodeFlow 与生效路径

区分低代码块、CodeFlow、辅助 Python 模块、影刀 SDK 和独立 Python。用户要求 Python 化时按其架构实现，不把低代码偏好写成平台硬规则；用户要求整应用测试时仍从影刀入口运行。

定位 app 实际目录、package.json/package.py、main、CodeFlow 和 import 调用链；排除 venv、site-packages、cef、缓存。常见入口为 `def main(args):`，但以当前平台诊断和既有代码为准。应用环境解释器必须从日志/依赖确认；普通 Python 的 import 结果不能证明影刀运行。

生效链：CodeFlow read → edit/write → read 回验 → app save（保存并编译）→ diagnostics；本地辅助模块修改后再确认实际加载副本、版本/同步和运行日志。保存不等于发布，发布不等于其他电脑更新；运行中不热改。

静态 py_compile/AST 只检查语法。文件、工作簿、网络响应使用上下文管理/显式关闭；PermissionError 先查自身句柄，再查外部占用；保留异常类型和阶段。
