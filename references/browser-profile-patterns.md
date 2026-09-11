# 浏览器与 Profile

账号与 Profile 映射只取用户 Excel/配置或当前应用实际输入；区分昵称、Profile 目录、browser ID。缺失/重复映射默认停止该账号，不借用第一条或其他账号。

Profile 已打开则连接，不重复启动竞争实例；多个 Chrome 进程不自动证明冲突。先查连接对象、重复启动块和目标用户目录，不自动关闭所有浏览器/WPS。业务网站登录与影刀 auth 独立判断。

`browser-use get-active` 只是连接当前活跃浏览器，不是激活目标 Profile；snapshot/screenshot 只能做当前页面观察。验证码、扫码、二次验证交给用户；用户完成后重新观察原 Profile、页面和 task，不重发导出。

验收需配置目标、网页连接、业务身份/页面三项均有证据。不要复制 Cookie、密码或票据。
