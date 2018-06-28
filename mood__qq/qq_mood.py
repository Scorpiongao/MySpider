'''
爬取好友说说
'''
import requests
from urllib .parse import  urlencode
import json
import pymongo
from json.decoder import JSONDecodeError
from login import login_qq
from config import *
from get_qq import get_qq
import pandas as pd
import time
from filter_qq import filter


client=pymongo .MongoClient (MONGO_URL ,connect= False)#声明MONGODB数据库对象，connect=False是为了消除MONGODB有关多线程的提示
db=client [MONGO_DB]
# db[MONGO_TABLE1 ].delete_many({'uin':'1456586096'})
# db.drop_collection(MONGO_TABLE1)


cookie,gtk,g_qzonetoken=login_qq()
print(cookie ,gtk ,g_qzonetoken,sep= '\n')

create_time_list=[]
source_name_list=[]
comment_count_list=[]

def get_html(offset,uin):
    try:
    # uin='1456586096'
        base_url='https://user.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?uin={uin}'.format(uin=uin)

        query={
        'uin':uin,
        'ftype':'0',
        'sort':'0',
        'pos':offset,
        'num':'20',
        'replynum':'100',
        'g_tk':gtk,
        'callback':'_preloadCallback',
        'code_version':'1',
        'format':'jsonp',
        'need_private_comment':'1',
        'qzonetoken':g_qzonetoken,
        'g_tk':gtk
        }
        requests_url=base_url.format(uin=uin)  +urlencode(query )
        headers = {
            'authority': 'user.qzone.qq.com',
            'method': 'GET',
            'path': requests_url.replace('https://user.qzone.qq.com','') ,
            'scheme': 'https',
            'accept-encoding': 'gzip, deflate, sdch',
            'accept-language': 'zh-CN,zh;q=0.8',
            'cookie': cookie,
            'referer': 'https://user.qzone.qq.com/{uin}'.format(uin=uin),
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
        }
        r=requests .get(base_url ,params= query ,headers =headers )
        # print(r.text )
        html=(r.text).replace('_preloadCallback(','').replace(');','')
        print(html)
        return uin,html
    except :
        print('request error')

def get_total(uin,html):
    try:
        data=json .loads(html)
        if data:
            total = data.get('total')
            print(u'好友：', uin, u'的说说总数为：', total)
            return total
    except :
        print('get total error',uin)
        black_list .append(uin)

def parse_html(uin,html):
    try:
        data=json .loads(html)
        if data:
            result = {}
            total = data.get('total')
            # print(u'好友：', uin, u'的说说总数为：', total)

            # if data['message']=='':
            #     print(u'不好意思，你被%s拉黑了。。。或者您没有权限查看'%uin )
            #     black_list .append(uin)
            # else:
            if data['msglist']:
                for msg in data['msglist']:


                    comment_list=[]
                    re_printed_dict={}
                    pic_list=[]
                    name=msg.get('name')
                    createTime=msg['createTime']
                    # create_time_list .append(createTime)
                    content=msg.get('content')
                    source_name = msg.get('source_name')
                    tid=msg.get('tid')
                    # source_name_list.append(source_name)
                    commentlist=msg.get('commentlist')
                    if commentlist :
                        # comment_count_list.append(len(commentlist))
                        for comment in commentlist:
                            comment_dict = {}
                            comment_dict['name']=comment .get('name')
                            comment_dict ['content']=comment.get('content')
                            comment_dict ['createTime']=comment .get('createTime2')
                            comment_dict ['qq_uin']=comment .get('uin')
                            comment_list .append(comment_dict )
                    piclist=msg.get('pic')
                    if piclist :
                        for pic in piclist :
                            pic_list .append(pic['url3'])

                    lbs=msg.get('lbs')

                    if msg.get('rt_con'):
                        is_printed=True
                        re_printed_dict['rt_content']=msg['rt_con']['content']
                        re_printed_dict['rt_createTime']=msg['rt_createTime']
                        re_printed_dict['rt_fwdnum']=msg['rt_fwdnum']
                        re_printed_dict['rt_source_name']=msg['rt_source_name']
                        re_printed_dict['rt_uin']=msg['rt_uin']
                        re_printed_dict['rt_uinname']=msg=['rt_uinname']
                    else:
                        is_printed=False
                    result ['tid']=tid
                    result['name']=name
                    result['uin']=uin
                    result ['total']=total
                    result ['createTime ']=createTime
                    result['content']=content
                    result ['source_name']=source_name
                    result ['is_printed']=is_printed
                    result['pic_list']=pic_list
                    result ['lbs']=lbs
                    result ['comment']=comment_list
                    result['re_printed_dict']=re_printed_dict
                    print(result )
                    save_to_mongodb(result)

    except JSONDecodeError:
        print('parse error',uin)
        black_list.append(uin)

def save_to_mongodb(result):
    if db[MONGO_TABLE1].update({'tid':result ['tid']},{'$set':result },True ) :
    # if db[MONGO_TABLE1 ].insert(result):
        print('Saved to MongoDB Successful',result ['tid'])
    else:
        print('Saved to MongoDB Failed', result['tid'])


if __name__=="__main__":
    qq_list = get_qq()
    # qq_list=filter()
    black_list = []
    for qq in qq_list:
        uin,html=get_html(str(0),qq)
        if get_total(uin,html):
            total=int(get_total(uin,html) )
            try:

                for offset in range(int(total//20)+1):
                    new_uin,html=get_html(str(offset*20),uin )
                    parse_html(uin=new_uin,html= html)
                    time.sleep(1)
            except TypeError:
                print('TypeError',uin)
                black_list .append(uin)

    print('被哪些好友拉黑了？ ',black_list )
    # df=pd.DataFrame ({
    #     'qq':qq_list,'create time':create_time_list ,'source name':source_name_list ,'comment count':comment_count_list
    # })
    # df.to_csv('mood.csv', encoding='utf_8_sig')
    # df.info()
    # df.head(5)