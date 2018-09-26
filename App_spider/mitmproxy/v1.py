'''
日志输出
'''

from mitmproxy import ctx

def request(flow):
    flow .request.headers['User-Agent'] = 'Google'
    ctx.log.info(str(flow .request .headers ))
    ctx.log.warn(str(flow.request.headers))
    ctx.log.error(str(flow.request.headers))