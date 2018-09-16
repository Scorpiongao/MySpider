## Fiddler 4
- 简介
> Fiddler（中文名称：小提琴）是一个HTTP的调试代理，以代理服务器的方式，监听系统的Http网络数据流动，
> Fiddler可以也可以让你检查所有的HTTP通讯，设置断点，以及Fiddle所有的“进出”的数据（我一般用来抓包）,Fiddler还包含一个简单却功能强大的基于JScript .NET事件脚本子系统，它可以支持众多的HTTP调试任务。

- 工作原理
    - ![原理图](https://upload-images.jianshu.io/upload_images/947566-f51654e6f0018748.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)
    - ![原理图](https://pic002.cnblogs.com/images/2012/263119/2012020409075327.png)
    - Fiddler是以代理WEB服务器的形式工作的,浏览器与服务器之间通过建立TCP连接以HTTP协议进行通信，浏览器默认通过自己发送HTTP请求到服务器，它使用代理地址:127.0.0.1, 端口:8888. 
    - 当Fiddler开启会自动设置代理， 退出的时候它会自动注销代理，这样就不会影响别的程序。不过如果Fiddler非正常退出，这时候因为Fiddler没有自动注销，会造成网页无法访问。解决的办法是重新启动下Fiddler。
    
- 界面
    - 工具面板
        - 说明注释、重新请求、删除会话、继续执行、流模式/缓冲模式、解码、保留会话、监控指定进程、寻找、保存会话、切图、计时、打开浏览器、清除IE缓存、编码/解码工具、弹出控制监控面板、MSDN、帮助
        - 两种模式
            - 缓冲模式（Buffering Mode）
                - Fiddler直到HTTP响应完成时才将数据返回给应用程序，可以控制响应，修改响应数据。但是时序图有时候会出现异常
            - 流模式（Streaming Mode）
                - Fiddler会即时将HTTP响应的数据返回给应用程序。更接近真实浏览器的性能。时序图更准确,但是不能控制响应。
    - 会话面板
        - ![会话面板图标说明](https://upload-images.jianshu.io/upload_images/947566-5fbf69350a526432.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/389)
    - 监控面板
    - 状态面板

- 基本使用
    - 参考教程
        - [Fiddler教程—1](https://www.cnblogs.com/conquerorren/p/8472285.html)
        - [Fiddler教程-2](http://www.cnblogs.com/TankXiao/archive/2012/02/06/2337728.html)
        
    - Fiddler配置
        - Tool --> Options --> Https --> 勾选 “CaptureHTTPS CONNECTs”,“Decrypt HTTPS traffic”, Ignore servercertificate errors --> OK
        - Tool --> Options --> Connections --> Allow remote computers to connect
    - 手机配置
        - 手机（Android）与PC同一局域网
        - wifi设置界面
            - 手动设置代理：IPv4:port  (port=8888)
        - 下载安全证书
            - 手机浏览器访问：IPv4:port
            - 点击安装证书：FiddlerRoot certificate