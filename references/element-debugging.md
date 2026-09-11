# 元素、iframe、弹窗与调试

先确认网页对象、Profile、页面和 frame，再读 selector。已有 selector 可复用但不是唯一来源；稳定属性优先，动态 class/index 谨慎。元素未找到按对象/页面/iframe/遮挡/展开/等待/匹配数量顺序排查。

可用 `studio selector list/details` 读已有元素；`browser-use snapshot/screenshot/api-reference` 做当前观察。snapshot refid 和临时 AI 定位不等于永久写回；捕获/修改后重新读取、验证唯一匹配并保存。

弹窗分流：广告/引导可按当前可见关闭控件处理；导出确认按业务步骤；登录/验证码/滑块保留交给用户；错误/权限提示记录而非点掉；未知重叠弹窗逐层识别。不要用坐标猜测或批量点“关闭”。区分页面加载等待和局部元素等待，动作后刷新观察。
