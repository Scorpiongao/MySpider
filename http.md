# HTTP协议
## 1. 超文本（HyperText）
- 包含超链接（Link）和各种媒体元素标记（Markup）的文本。这些超文本文件彼此链接，形成网状(Web)，因此也被称为网页（Web Page）
这些链接使用URL表示，最常见的超文本标记语言HTML。
- URL
    - 统一资源定位符，用来唯一标识万维网中的某个文档
    - 由协议、主机和端口（默认为80）以及文件名三部分组成
    - 如：https://github.com/fengzi258/MyWeb
        - https://        协议
        - github.com(:80) 主机和端口
        - fengzi258/MyWeb 文件名及路径

- 超文本传输协议HTTP
    - 是一种按照URL指示，将超文本文档从一台主机（Web服务器）传输到另一台主机（浏览器）的应用层协议，以实现超链接功能

## 2.HTTP工作原理
- 请求/响应模型
    - 在用户点击URL为https://github.com/fengzi258/MyWeb/blob/master/flask/6_%E7%A8%8B%E5%BA%8F%E7%BB%93%E6%9E%84.md的链接后，浏览器和Web服务器执行以下动作：
    - 浏览器分析链接中的URL
    - 浏览器向DNS请求解析github.com的IP地址
    - NDS将解析出的IP地址52.74.223.119返回给浏览器
    - 浏览器与服务器建立TCP连接（80端口）
    - 浏览器请求文档：GET/fengzi258/MyWeb/blob/master/flask/6_%E7%A8%8B%E5%BA%8F%E7%BB%93%E6%9E%84.md
    - 服务器给出响应，将文档fengzi258/MyWeb/blob/master/flask/6_%E7%A8%8B%E5%BA%8F%E7%BB%93%E6%9E%84.md发给浏览器
    - 释放TCP连接
    - 浏览器显示文档

- 连接方式
    - 持久连接
    - 非持久连接

- 无状态性
    - 同一个客户端（浏览器）第二次访问同一个Web服务器上页面时，服务器无法知道这个客户曾经访问过
    - HTTP的无状态性简化了服务端的设计，使其更容易支持大量并发的HTTP请求。

## 3.HTTP报文结构
- 请求报文
    - 从客户端（浏览器）向服务器发送的请求报文，报文的所有字段都是ASCII码
    - 请求行
        - 方法(空格)URL 协议版本CRLF(换行)
        - 如：GET /index.html HTTP/1.1
    - 首部行
        - 用来说明浏览器、服务器或报文主体的一些信息
        - ```
            首部字段名：值CRLF
            首部字段名：值CRLF
            ....
            ```
        - F12（开发人员工具可查看请求头）
    - 请求报文

- 返回报文
    - 从Web服务器到客户机（浏览器）的应答，报文的所有字段都是ASCII码
    - 状态行
        - 版本 状态码 短语CRLF
        - 如：HTTP/1.1 200 OK
    - 首部行
        - 与请求首部行类似
    - 响应报文

- 请求中的方法
    - GET      请求读取一个Web页面
    - POST     附加一个命名资源（如Web页面）
    - DELETE   删除Web页面
    - CONNECT  用于代理服务器
    - HEAD     请求读取一个Web页面的首部
    - PUT      请求存储一个Web页面
    - TRACE    用于测试，要求服务器送回收到的请求
    - OPTION    查询特定选项

- 响应中的状态码
    - 响应报文状态行中包含的一个3位数字，指明特定的请求是否被满足，如果没有满足，原因是什么
    - 状态码分五类
    
    
        状态码    含义         例子
        1xx      通知消息      100=服务器正在处理客户请求
        2xx      成功         200=请求成功（OK）
        3xx      重定向        301=页面改变了位置
        4xx      客户错误      403=禁止的页面；404=页面未找到
        5xx      服务器错误     500=服务器内部错误；503=以后重试

- 首部字段或消息头
    
    
    Host：github.com
    User-Agent：Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/56.0
    Accept：text/html
    Accept-Language：zh-CN,en-US;q=0.7,en;q=0.3
    Accept-Encoding：gzip, deflate, br
    Referer：https://github.com/fengzi258/M…E5%BA%8F%E7%BB%93%E6%9E%84.md
    x-requested-with：XMLHttpRequest
    origin：https://github.com
    Cookie：logged_in=yes; _octo=GH1.1.760…3; tz=Asia%2FShanghai; _gat=1
    Connection：keep-alive

