## Charles
> Charles是常用的截取网络封包的工具(俗称抓包)。
> Charles 通过将自己设置成系统的网络访问代理服务器，使得所有的网络访问请求都通过它来完成，从而实现了网络封包的截取和分析。 
- 网络抓包工具，跨平台支持更好
- 官网：https://www.charlesproxy.com


### 功能
1. 支持SSL代理。可以截取分析SSL的请求。

2. 支持流量控制。可以模拟慢速网络以及等待时间（latency）较长的请求。

3. 支持AJAX调试。可以自动将json或xml数据格式化，方便查看。

4. 支持AMF调试。可以将Flash Remoting 或 Flex Remoting信息格式化，方便查看。

5. 支持重发网络请求，方便后端调试。

6. 支持修改网络请求参数。

7. 支持网络请求的截获并动态修改。

8. 检查HTML，CSS和RSS内容是否符合W3C标准。

### charles 两种查看封包的视图
1. Structure 
    - 视图将网络请求按访问的域名分类
2. Sequence 
    - 视图将网络请求按访问的时间排序


### 基本使用
- 参考教程
    - [抓包神器之Charles--常用功能](https://blog.csdn.net/mxw2552261/article/details/78645118)
    - [charles使用教程](https://blog.csdn.net/Naruto_22/article/details/72900708)
    - [催庆才PY3--Charles安装](https://cuiqingcai.com/5255.html)
    
- **证书配置（window）**
    - Help --> SSL Proxying --> Install Charles Root Certificate
    - 点击安装证书 --> 下一步 --> 将所有的证书放入下列存储 --> 浏览 --> 受信任的根证书颁发机构 --> 确定 --> 下一步
    
- **解决contents乱码问题**
    - [抓包工具 Charles Response Contents中文乱码解决方法（新）](https://blog.csdn.net/intelrain/article/details/79655410)
    1. 先按上述配置好证书
    2. 再Proxy —-> SSL Proxy Settings —-> Add，Host: *,Port: 443

- **手机端安装证书(Android)**
    1. 电脑的charles代理开启
        - Proxy --> Proxy Settings --> 端口号：8888
    2. 手机与电脑同一局域网下
        - 电脑 IP：cmd --> ipconfig --> IPv4
        - 设置手机代理：IPv4:8888
    3. Allow(信任此设备)，可以抓取流经App的数据包了
    4. 安装Charles的HTTPS证书
        - Help --> SSL Proxying --> Install Charles Root Certificate on a Mobile Device or Remote Browser --> OK
    5. 手机浏览器打开：chls.pro/ssl --> 提示框 --> 添加证书名称（charles）--> 确定
    注：iOS系统需要第四步，Android不需要
    