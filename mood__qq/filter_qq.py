'''
这个是因为之前那个qq_mood运行一部分后报错了，
现在想看哪些qq已经爬取了，还有哪些没爬，
整个运行完后，这个可以查看列表中哪些好友设置了访问权限
'''

import pymongo
from config import *
from get_qq import get_qq


qqlist=get_qq()
print(u'好友总数%s'%len(qqlist))
print(qqlist)
get_list=[]

def filter():

    client=pymongo .MongoClient (MONGO_URL )
    db=client [MONGO_DB ]

    for qq in qqlist :
        uin=db[MONGO_TABLE1 ].find_one({'uin':qq})
        if uin:
            # print(uin.get('uin'),uin.get('name'))
            get_list .append(uin.get('uin'))

    print(u'已经爬取了%s位好友qq'%len(get_list ))

    sx_qq_list=list(set(qqlist )-set(get_list ))
    print(sx_qq_list )
    print(u'还剩下%s位好友qq没爬，这些好友设置了访问权限。。。。'%len(sx_qq_list))
    return sx_qq_list
filter()
# l1=[1,3,6,9,0,4]
# l2=[1,2,3,4,5,6,7,8,9,0]
# l3=set(l2)-set(l1)
# print(list(l3))