## 模拟登录
- 很多情况下，页面的一些信息只有登录才可以查看
- 爬取的信息如果需要登录才能看，就需要模拟登录

### 核心
- 获取登录后的Cookies，一般用`session.post(url,data=data,headers=headers)`完成登录后维持会话，解决Cookies问题
- 重点转化为from_data的构造
    - 一些字段固定
    - 一些变化
        - 页面源码提取
            - **github_login**
        - js加密生成（如sign,salt等），这需要找到相关js并阅读，模拟生成
            - youdao(urllib_v19)
   
- 也可使用selenium来登录
    - 密码用户名登录
        - douban-login
    - 扫码登录
        - zhihu_login
- 有时需要登录之后，访问其他页面要根据登录后页面信息构造参数 
    - mood_qq
    - music163