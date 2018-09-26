'''
Request的常见属性
'''
from mitmproxy import ctx

def request(flow):

    request = flow .request
    info = ctx.log.info

    info (request .url)
    info (str(request .headers))
    info (str(request.cookies))
    info (request .host)
    info (request .method)
    info (str(request .port))
    info (request .scheme)

    #对属性进行修改，直接赋值
    url = 'https://httpbin.org/get'
    flow.request .url = url
    info (request .url)