# Ajax
- [W3School-ajax](http://www.w3school.com.cn/ajax/ajax_intro.asp)
> AJAX = Asynchronous JavaScript and XML（异步的 JavaScript 和 XML）。

> AJAX 不是新的编程语言，而是一种使用现有标准的新方法。

> AJAX 是与服务器交换数据并更新部分网页的艺术，在不重新加载整个页面的情况下。
> 通过在后台与服务器进行少量数据交换，AJAX 可以使网页实现异步更新。这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新。
> 传统的网页（不使用 AJAX）如果需要更新内容，必需重载整个网页面。

- 异步请求（页面下拉，加载新内容或有加载更多按钮）
- 一定会有url，请求方法，可能有数据
- 请求类型：XHR
- request headers中 x-requested-with: XMLHttpRequest，标记该请求为ajax请求
- 一般使用json格式