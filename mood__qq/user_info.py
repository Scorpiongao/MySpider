'''
好友说说数（日志，说说，图片，访问量）
'''
from login import login_qq
import requests
from urllib .parse import  urlencode
import json
from get_qq import get_qq
import pandas as pd
import pymongo
from config import *
import time

client=pymongo .MongoClient (MONGO_URL ,connect= False)#声明MONGODB数据库对象，connect=False是为了消除MONGODB有关多线程的提示
db=client [MONGO_DB]


cookie,gtk,g_qzonetoken=login_qq()


# intimacyScore_list=[]
# rz_list=[]
# ss_list=[]
# xc_list=[]

black_qq_list=[]
def get_html(uin):
    try:
    # uin='1456586096'
        base_url='https://user.qzone.qq.com/proxy/domain/r.qzone.qq.com/cgi-bin/main_page_cgi?'

        query={
        'uin':uin,
        'param':'3_{uin}_0|8_8_{login_uin}_0_1_0_0_1|15|16'.format(uin=uin,login_uin =login_uin),
        'g_tk':gtk,
        'qzonetoken':g_qzonetoken,
        'g_tk':gtk
        }
        requests_url=base_url  +urlencode(query )
        headers = {
            'authority': 'user.qzone.qq.com',
            'method': 'GET',
            'path': requests_url.replace('https://user.qzone.qq.com','') ,
            'avail-dictionary':'XprLfaXG',
            'cache-control':'max-age=0',
            'accept-encoding': 'gzip, deflate, sdch',
            'accept-language': 'zh-CN,zh;q=0.8',
            'cookie': cookie,
            'referer': 'https://user.qzone.qq.com/{uin}'.format(uin=uin),
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
        }
        r=requests .get(base_url ,params= query ,headers =headers )
        # print(r.text )
        html=(r.text).replace('_Callback(','').replace(')','')
        # print(html)
        return uin,html
    except :
        print('request error',uin)
        black_qq_list .append(uin)

def parse_html(uin,html):
    try:
        data=json .loads(html)
        if data and data['data']:
            result={}
            data=data['data']
            if data.get('module_3'):
                modvisitcount=data.get('module_3').get('data').get('modvisitcount')
                visitcount=modvisitcount [0]['totalcount']
                fb_visitcount=modvisitcount [1]['totalcount']
                print('parse module_3 successfully')
            else:
                visitcount =None
                fb_visitcount =None

            if data.get('module_16'):
                rz=data['module_16']['data']['RZ']
                ss=data['module_16']['data']['SS']
                xc=data['module_16']['data']['XC']
                print('parse module_16 successfully',rz,ss,xc)
                # rz_list .append(rz)
                # ss_list .append(ss)
                # xc_list .append(xc)

            if data.get('module_15'):
                intimacyScore=data['module_15']['data']['intimacyScore']
                print('parse module_15 successfully',intimacyScore )
                # intimacyScore_list .append(intimacyScore )
            else:
                print(u'这是自己的qq号: ',uin)
                intimacyScore =100
            result ['uin']=uin
            result['visicount']=visitcount
            result ['fb_visitcount']=fb_visitcount
            result ['rz']=rz
            result ['ss']=ss
            result ['xc']=xc
            result['intimacyScore']=intimacyScore
            print(result )
            # return result
            save_to_mongodb(result )

    except:
        print('parse data error',uin)
        black_qq_list .append(uin)

def save_to_mongodb(result):
    if db[MONGO_TABLE3].update({'uin':result ['uin']},{'$set':result },True ) :
    # if db[MONGO_TABLE2 ].insert(result):
        print('Saved to MongoDB Successful',result ['uin'])
    else:
        print('Saved to MongoDB Failed', result['uin'])


def run(qq_list):
    for qq in qq_list :
        uin,html=get_html(qq)
        print('uin: ',uin)
        parse_html(uin,html)
        time.sleep(2)

if __name__=="__main__":
    login_uin='1456586096'
    qq_list=get_qq()
    run(qq_list )
    a = len(list(set(black_qq_list)))
    print(u'从失败的列表中重新开始新一轮请求')
    run(list(set(black_qq_list)))
    if a == len(list(set(black_qq_list))):
        print(u'这些qq的主人设置了访问权限，访问%s被禁止！！！' % black_qq_list)
    # df=pd.DataFrame ({
    #     'qq':qq_list ,'rz':rz_list ,'ss':ss_list ,'xc':xc_list
    # })
    # df.to_csv('count.csv')
    # df.info()
    # df.head()