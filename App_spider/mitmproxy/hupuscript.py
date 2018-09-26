'''
虎扑app脚本
'''
import json
from mitmproxy import ctx
##数据可以抓取，但存储到mongoDB出现问题，有待解决。。。
import pymongo

client = pymongo .MongoClient (host= 'localhost',port= 27017)
db = client ['hupu']
collection = db['followd']

def response(flow):
    global collection
    url = 'https://bbs.mobileapi.hupu.com/1/7.2.10/recommend/getThreadsList'
    if flow .request.url.startswith(url):
        text = flow.response.text
        data = json .loads(text)
        if data:
            result = data.get('result')
            if result and 'data' in result.keys():
                items = result.get('data')
                # print(len(items) )
                for item in items:
                    # print(item)
                    tid = item.get('tid')
                    title = item.get('title')
                    puid = item.get('puid')
                    fid = item.get('fid')
                    replies = item.get('replies')
                    userName = item.get('userName')
                    time = item.get('time'),
                    if item.get('imgs') and len(item.get('imgs')) > 0:
                        imgs = [img for img in item.get('imgs')]
                    else:
                        imgs = []
                    lightReply = item.get('lightReply')
                    forum = item.get('forum')
                    forum_name = item.get('forum_name')
                    result = {
                        'tid': tid,
                        'title': title,
                        'puid': puid,
                        'fid': fid,
                        'replies': replies,
                        'userName': userName,
                        'time': time,
                        'imgs': imgs,
                        'lightReply': lightReply,
                        'forum': forum,
                        'forum_name': forum_name
                    }
                    ctx.log.info(str(result))
                    collection .update({'tid':result ['tid'],'title':result ['title']},{'$set':result },True )

