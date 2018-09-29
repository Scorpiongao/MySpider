'''
app-JD 商品信息和评论抓取
'''

import json
import re
from urllib .parse import  unquote

def response(flow):
    #商品接口
    url = 'cdnware.m.jd.com'
    if url in flow.request.url:
        text = flow.response.text
        data = json .loads(text)
        if data.get('wareInfo') and data.get('wareInfo').get('basicInfo'):
            info = data.get('wareInfo').get('basicInfo')
            name = info.get('name')
            share_url = info.get('shareUrl')
            id = info.get('wareId')
            wareImage = info.get('wareImage')
            service = info.get('service')
            print(id,name,share_url ,wareImage ,service )
    #评论接口
    url = 'api.m.jd.com/client.action?functionId=getCommentListWithCard'
    if url in flow.request .url:
        #Request请求参数中含商品ID
        print(flow .request .text )
        body = unquote(flow .request .text)
        print(body)
        #提取商品ID
        pattern = re.compile('sku.*?"(\d+)"')
        id = re.search(pattern ,body).group(1) if re.search(pattern,body) else None
        #提取 Response Body
        text = flow.response.text
        data = json.loads(text)
        if data.get('commentInfoList') :
            for moment in data.get('commentInfoList'):
                if moment.get('commentInfo') and moment.get('commentInfo').get('commentData'):
                    info = data.get('commentInfo')
                    text = info.get('commentData')
                    nickname = info.get('userNickName')
                    pictures = info.get('pictureInfoList')
                    date = info.get('orderDate')
                    print(id,text,nickname ,pictures ,date)

