# QQ空间说说爬取说明
## 好友qq来源
- 从qq邮箱中的联系中导出
- 涉及到好友qq的隐私，没有全部显示到QQemail.csv中，但格式类似
- 需要从导出的csv中读取qq

## 爬取思路
- 先扫码登录得到必要的参数
    - 具体看代码说明
- 再根据得到的参数模拟用户浏览
- 爬取与数据存储
- 代码的异常处理不是很完善，中途出现过异常报错退出，
  于是我增加了过滤部分，即爬过的不再爬取
