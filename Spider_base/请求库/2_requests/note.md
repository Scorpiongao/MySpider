# Requests-献给人类
- HTTP for Humans，更简洁更友好
- 继承了urllib的所有特征
- 底层使用的是urllib3
- 开源地址： https://github.com/requests/requests
- 中文文档： http://docs.python-requests.org/zh_CN/latest/index.html   
- 安装： conda install requests
- get请求
    - requests.get(url,parmas=parmas,headers=headers,proxies=proxies,timeout=None,**kwargs)
    - requests.request("get", url)
    - 可以带有headers、parmas、proxies参数
    - 案例v1
- get返回内容
    - 案例v2
    - 二进制数据保存 `response.content` 案例v3
    
- post
    - rsp = requests.post(url, data=data,headers=headers,**kwargs)
    - 参看案例4
    - date, headers要求dict类型

- proxy
   - 
        ```
        proxies = {
        "http":"address of proxy",
        "https": "address of proxy"
        }
        
        rsp = requests.request("get", "http:xxxxxx", proxies=proxies)
        ```
   - 代理有可能报错，如果使用人数多，考虑安全问题，可能会被强行关闭
   - 案例v5

- 用户验证
    - 代理验证
    
            #可能需要使用HTTP basic Auth， 可以这样
            # 格式为  用户名:密码@代理地址：端口地址
            proxy = { "http": "http://username:password@192.168.1.123：4444"}
            rsp = requests.get("http://baidu.com", proxies=proxy)

- web客户端验证
    - 如果遇到web客户端验证，需要添加auth=（用户名，密码）
    
            auth=("username", "password")#授权信息
            rsp = requests.get("http://www.baidu.com", auth=auth)

- cookie
    - requests可以自动处理cookie信息
    ```
      rsp = requests.get("http://xxxxxxxxxxx")
      # 如果对方服务器给传送过来cookie信息，则可以通过反馈的cookie属性得到
      # 返回一个cookiejar实例
      cookiejar = rsp.cookies   
      
      
      #可以讲cookiejar转换成字典
      cookiedict = requests.utils.dict_from_cookiejar(cookiejar)         
    ```
    - 案例v6
    
- session
    - 跟服务器端session不是一个东东
    - 模拟一次会话，从客户端浏览器链接服务器开始，到客户端浏览器断开
    - 能让我们跨请求时保持某些参数，比如在同一个session实例发出的 所有请求之间保持cookie
    - 通常用于模拟登录成功之后再进行下一步操作（模拟在同一个浏览器中打开同一站点的不同页面）
    ```
    # 创建session对象，可以保持cookie值
    ss = requests.session()
    
    headers = {"User-Agetn":"xxxxxxxxxxxxxxxxxx"}
    
    data = {"name":"xxxxxxxxxxx"}
    
    # 此时，由创建的session管理请求，负责发出请求，
    ss.post("http://www.baidu.com", data=data, headers=headers)
    
    rsp = ss.get("xxxxxxxxxxxx")
    ```      
    - 案例v7
    
- https请求验证ssl证书
    - 参数verify负责表示是否需要验证ssL证书，默认是True
    - 如果不需要验证ssl证书，则设置成False表示关闭
    - 案例v8
        
            rsp = requests.get("https://www.baidu.com", verify=False)
            # 如果用verify=True访问12306，会报错，因为他证书有问题 