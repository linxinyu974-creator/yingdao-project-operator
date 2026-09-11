# 运行、入口、观察与额度

`console task run --app-id` 才证明整应用入口；`studio app run --flow-id` 只证明指定流程；独立 Python 只证明模块。控制台 task ID、Studio run ID、CLI 会话号不可混用。

提交前先 `system state`，已有任务就查 status/logs，不因“继续”重跑；查 app detail、实际启动 flow、版本/同步和输入。空入口、秒结束、无预期副作用判定为空跑风险。编辑会话先保存，必要时 `studio current sync`；不得覆盖他人未保存修改。

提交：`console task run --app-id <id> [--inputs-file <json>] [--async]`；响应必须记录真实 task ID/接受状态/错误码。观察：`console task status/logs --task-id`，logs 使用响应游标。CLI 等待超时不等于任务停止；每次轮询不超过 60 秒。验证码由用户处理，完成后观察原 task/页面；已终止则不冒充继续。

额度按本次原始 QuotaGate 或拒绝响应判断。`usedToday=4,dailyLimit=5,Allowed=True` 是当时允许且观察到余 1，不是耗尽；业务失败也不能推导额度耗尽；只有明确 quota_limited/CLI quota denied/额度拒绝才停止重复提交。5 次不是全版本承诺。

整应用成功须同时有正确入口、目标 Profile/业务页、对应输入的业务结果和内容校验；人工验证码/补步需标记受干预。
