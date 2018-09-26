def request(flow):
    #参数为flow，它其实是一个HTTPFlow对象
    #request属性可获得当前请求对象
    #改变请求头
    flow.request.headers['User-Agent'] = 'MitmProxy'
    print(flow .request .headers)