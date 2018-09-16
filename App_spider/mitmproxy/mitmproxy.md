## mitmproxy
- 支持HTTP和HTTPS的抓包程序，类似Fiddler/Charles的功能，控制台形式操作
- 两个组件
    - Windows上不支持mitmproxy的控制台接口，但可以使用mitmdump和mitmweb
    - mitmdump
        - 命令行接口，可以对接python脚本，利用python实现监听后的处理
    - mitmweb
        - web程序，可以观察mitmproxy捕获的请求
        
### 安装
- 最简单的安装方式
    - `pip install mitmproxy`
- Windows 下安装
    - [Github-Releases页面](https://github.com/mitmproxy/mitmproxy/releases)
    - 下载Windows下的exe安装包即可

### 功能
- 拦截HTTP/HTTPS请求和响应
- 保存HTTP会话并进行分析
- 模拟客户端发起请求，模拟服务端返回响应
- 利用反向代理将流量转发给指定的服务器
- 利用python对HTTP请求和响应进行实时处理

### CA证书配置
- 参考
    - [python3.6安装mitmproxy](https://blog.csdn.net/weixin_42216838/article/details/80835781)
- 配置电脑和手机 
    1. 电脑和手机连接到同一个wifi环境下（同一局域网） 
    2. 修改浏览器代理服务器地址为运行mitmproxy的那台机器（本机）ip地址，端口设定为你启动mitmproxy时设定的端口，如果没有指定就使用8080 
    3. 手机做同样操作，修改wifi链接代理为 【手动】，然后指定ip地址和端口 (IPv4:8080)
    4. 安装证书
        - 在手机或pc机上打开浏览器访问 mitm.it 这个地址，选择当前平台的图标，点击安装证书。
        
### 抓包原理
> 和Charles一样，mitmproxy运行于自己的PC上，mitmproxy会在PC的8080端口运行，然后开启一个代理服务，这个服务实际上是一个HTTP/HTTPS的代理

> 手机和PC在同一个局域网内，设置代理为mitmproxy的代理地址，这样手机在访问互联网的时候流量数据包就会流经mitmproxy，
> mitmproxy再去转发这些数据包到真实的服务器，服务器返回数据包时再由mitmproxy转发回手机，这样mitmproxy就相当于起了中间人的作用，抓取到所有Request和Response，
> 另外这个过程还可以对接mitmdump，抓取到的Request和Response的具体内容都可以直接用Python来处理，比如得到Response之后我们可以直接进行解析，然后存入数据库，这样就完成了数据的解析和存储过程。

### mitmdump的使用
- mitmdump是mitmproxy的命令行接口，同时可以对接python对请求进行处理
- 截取的数据保存到文件中(-w参数)
    - `mitmdump -w outfile` outfile为文件名
- 指定脚本处理截获的数据(-s参数)
    - `mitmdump -s script.py` script.py为脚本文件名，在当前命令执行的目录中