'''
返回当前页面的URL和内容
'''

def response(flow):
    flow.response .encoding = 'utf-8'
    print(flow .request.url)
    print(flow.response.text)