# 'https://user.qzone.qq.com/1404950929/main'
'''
好友的个人信息
'''
import re
import requests
import time
import json
from config import *

from get_qq import get_qq
import pymongo
import pandas as pd

client=pymongo .MongoClient (MONGO_URL ,connect= False)#声明MONGODB数据库对象，connect=False是为了消除MONGODB有关多线程的提示
db=client [MONGO_DB]

# cookie,gtk,g_qzonetoken=login_qq()
# uin_list=[]
# nickname_list=[]
# spacename_list=[]
# desc_list=[]
# avatar_list=[]
# sex_list=[]
# age_list=[]
# animalsign_list=[]
# birthday_list=[]
# address_list=[]
# home_address_list=[]
# marriage_list=[]
# lover_list=[]
# career_list=[]
# company_list=[]

re_uin_list=[]
# rz_list=[]
# ss_list =[]
# xc_list =[]
# intimacyScore_list =[]
# visit_count_list=[]
# fb_visit_count_list=[]


def get_html(uin):
    url='https://user.qzone.qq.com/{uin}/main'.format(uin=uin )
    headers={
        'authority':'user.qzone.qq.com',
        'method':'GET',
        'path':url.replace('https://user.qzone.qq.com','') ,
        'scheme':'https',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'accept-encoding':'gzip, deflate, sdch',
        'accept-language':'zh-CN,zh;q=0.8',
        'cache-control':'max-age=0',
        # 'cookie':cookie ,
        'cookie':COOKIE,
        'if-modified-since':'Sat, 02 Jun 2018 06:34:08 GMT',
        'upgrade-insecure-requests':'1',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    try:
        response=requests .get(url,headers=headers )
        if response .status_code ==200:
            # print(response .text )
            return response .text
    except requests.ConnectionError as e:
        print('get html failed',e.args)

def parse_html(uin,html):
    if html:
        pattern=re.compile(r'g_userProfile.*?({.*?})',re .S )
        try:
            data=re.findall(pattern ,html )[0]
            if data:
                data=data.replace('+','')
                return data
            else:
                return None
        except IndexError :
            print('IndexError',uin)
            re_uin_list .append(uin)


def parse_data(data):
    if data:
        try:
            data=json.loads(data)
            # print(type(data))
            result = {}
            uin=data.get('uin')
            nickname=data.get('nickname')
            spacename=data.get('spacename')
            desc=data.get('desc')
            avatar=data.get('avatar')
            sex=data.get('sex')
            age=data.get('age')
            animalsign=data.get('animalsign')
            birthday=data.get('birthyear')+'-'+data.get('birthday')
            address=data.get('country')+" "+data.get('province')+' '+data.get('city')
            home_address=data.get('hco')+' '+data.get('hp')+' '+data.get('hc')
            marriage=data.get('marriage')
            lover=data.get('lover')
            career=data.get('career')
            company=data.get('company')
            # print('--'*10)
            # print(uin,nickname ,spacename ,desc ,avatar,sex ,
            #       age,animalsign ,birthday,address ,home_address ,
            #       marriage,lover ,career ,company ,sep= '\n'  )
            result ['uin']=uin
            result ['nickname']=nickname
            result ['spacename']=spacename
            result ['desc']=desc
            result ['avatar']=avatar
            result ['sex']=sex
            result ['age']=age
            result ['animalsign']=animalsign
            result ['birthday']=birthday
            result ['address']=address
            result ['home_address']=home_address
            result ['marriage']=marriage
            result ['lover']=lover
            result ['career']=career
            result ['company']=company

            # uin_list.append(uin)
            # nickname_list.append(nickname)
            # spacename_list.append(spacename )
            # desc_list .append(desc )
            # avatar_list .append(avatar )
            # sex_list .append(sex )
            # age_list .append(age )
            # animalsign_list .append(animalsign )
            # birthday_list .append(birthday )
            # address_list.append(address )
            # home_address_list .append(home_address )
            # marriage_list .append(marriage )
            # lover_list .append(lover )
            # career_list .append(career )
            # company_list .append(company )
            # return result,uin_list,nickname_list ,spacename_list  ,desc_list ,avatar_list,sex_list ,age_list ,animalsign_list,birthday_list ,address_list ,home_address_list ,marriage_list ,lover_list ,career_list ,company_list
            return result
        except :
            print('json.decoder.JSONDecodeError')

def save_to_mongodb(result):
    if db[MONGO_TABLE2].update({'uin':result ['uin']},{'$set':result },True ) :
    # if db[MONGO_TABLE2 ].insert(result):
        print('Saved to MongoDB Successful',result ['uin'])
    else:
        print('Saved to MongoDB Failed', result['uin'])

def run(qqlist):
    for uin in qqlist :
        html=get_html(uin)
        # print(html)
        data=parse_html(uin,html)
        result =parse_data(data)
        if result :
            save_to_mongodb(result)
        time.sleep(2)


if __name__=="__main__":
    uinlist=get_qq()
    run(uinlist)
    print(re_uin_list )
    a=len(list(set(re_uin_list)) )
    print(u'从失败的列表中重新开始新一轮请求')
    run(list(set(re_uin_list)))
    if a==len(list(set(re_uin_list ))):
        print(u'这些qq的主人设置了访问权限，访问%s被禁止！！！'%re_uin_list )

        # qq, html = user_info.get_html(uin)
        # result['mood_count'] = user_info.parse_html(qq, html)
        # rz_list .append(result ['mood_count '].get('rz'))
        # ss_list .append(result ['mood_count '].get('ss'))
        # xc_list .append(result ['mood_count '].get('xc'))
        # visit_count_list .append(result ['mood_count '].get('visitcount'))
        # fb_visit_count_list .append(result ['mood_count '].get('fb_visitcount'))

    # df = pd.DataFrame({
    #     # 'visit_count':visit_count_list ,'fb_visit_count':fb_visit_count_list ,'rz': rz_list, 'ss': ss_list, 'xc': xc_list,'intimacyScore':intimacyScore_list,
    #     'qq': uin_list,'nickname':nickname_list ,'spacename':spacename_list ,'desc':desc_list ,
    #     'avatar':avatar_list,'sex':sex_list ,'age':age_list ,'animalsign':animalsign_list,
    #     'address':address_list ,'home_address':home_address_list ,'birthday':birthday_list ,
    #     'marriage':marriage_list ,'lover':lover_list,'career':career_list ,'company':company_list
    # })
    # df.to_csv('qq_mood.csv',encoding= 'utf_8_sig')
    # df.info()
    # df.head()
'tvfe_boss_uuid=427f58974b3be55a; pac_uid=1_1456586096; mobileUV=1_1587a986661_413f5; _ga=GA1.2.1735770227.1479276331; pgv_pvi=1966100480; RK=uwWv1932Ob; o_cookie=1456586096; __Q_w_s__QZN_TodoMsgCnt=1; __Q_w_s_hat_seed=1; pgv_pvid=6264063782; _qpsvr_localtk=0.6042907023058073; pgv_si=s4574054400; pgv_info=ssid=s4451016985; ptisp=cm; ptcz=b0e601e63fda08c3f8afebeee333f36a347fbf2b0ebf7817aff5b159299186d8; uin=o1456586096; skey=@KtEz3DlJm; pt2gguin=o1456586096; p_uin=o1456586096; pt4_token=Hm3z50bdGNXkxJ4IQ-aRGrmZasgeI5WFVoG025Eus*A_; p_skey=qC-Kzu2FFEifZfcWrpxW7hplR-9g08jcVMZ6iQlUZII_; scstat=2; qz_screen=1366x768; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=15; Loading=Yes; rv2=802E08A83030FDABAB99B10DFD325E83380A579AEF27410822; property20=174B8D1F6B344BF01B27E07F62941B41778CB5B24B389E9B245F6EE66773223C9AD97C75E141634B; qzspeedup=sdch'
'tvfe_boss_uuid=427f58974b3be55a; pac_uid=1_1456586096; mobileUV=1_1587a986661_413f5; _ga=GA1.2.1735770227.1479276331; pgv_pvi=1966100480; RK=uwWv1932Ob; o_cookie=1456586096; __Q_w_s__QZN_TodoMsgCnt=1; __Q_w_s_hat_seed=1; pgv_pvid=6264063782; _qpsvr_localtk=0.6042907023058073; pgv_si=s4574054400; pgv_info=ssid=s4451016985; ptisp=cm; ptcz=b0e601e63fda08c3f8afebeee333f36a347fbf2b0ebf7817aff5b159299186d8; uin=o1456586096; skey=@KtEz3DlJm; pt2gguin=o1456586096; p_uin=o1456586096; pt4_token=Hm3z50bdGNXkxJ4IQ-aRGrmZasgeI5WFVoG025Eus*A_; p_skey=qC-Kzu2FFEifZfcWrpxW7hplR-9g08jcVMZ6iQlUZII_; scstat=2; qz_screen=1366x768; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=15; rv2=802E08A83030FDABAB99B10DFD325E83380A579AEF27410822; property20=174B8D1F6B344BF01B27E07F62941B41778CB5B24B389E9B245F6EE66773223C9AD97C75E141634B; Loading=Yes; qzspeedup=sdch'
'tvfe_boss_uuid=427f58974b3be55a; pac_uid=1_1456586096; mobileUV=1_1587a986661_413f5; _ga=GA1.2.1735770227.1479276331; pgv_pvi=1966100480; RK=uwWv1932Ob; o_cookie=1456586096; __Q_w_s__QZN_TodoMsgCnt=1; __Q_w_s_hat_seed=1; pgv_pvid=6264063782; _qpsvr_localtk=0.6042907023058073; pgv_si=s4574054400; pgv_info=ssid=s4451016985; ptisp=cm; ptcz=b0e601e63fda08c3f8afebeee333f36a347fbf2b0ebf7817aff5b159299186d8; uin=o1456586096; skey=@KtEz3DlJm; pt2gguin=o1456586096; p_uin=o1456586096; pt4_token=Hm3z50bdGNXkxJ4IQ-aRGrmZasgeI5WFVoG025Eus*A_; p_skey=qC-Kzu2FFEifZfcWrpxW7hplR-9g08jcVMZ6iQlUZII_; scstat=2; qz_screen=1366x768; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=15; Loading=Yes; rv2=802E08A83030FDABAB99B10DFD325E83380A579AEF27410822; property20=174B8D1F6B344BF01B27E07F62941B41778CB5B24B389E9B245F6EE66773223C9AD97C75E141634B; qzspeedup=sdch'
'tvfe_boss_uuid=427f58974b3be55a; pac_uid=1_1456586096; mobileUV=1_1587a986661_413f5; _ga=GA1.2.1735770227.1479276331; pgv_pvi=1966100480; RK=uwWv1932Ob; o_cookie=1456586096; __Q_w_s__QZN_TodoMsgCnt=1; __Q_w_s_hat_seed=1; pgv_pvid=6264063782; _qpsvr_localtk=0.6042907023058073; pgv_si=s4574054400; pgv_info=ssid=s4451016985; ptisp=cm; ptcz=b0e601e63fda08c3f8afebeee333f36a347fbf2b0ebf7817aff5b159299186d8; uin=o1456586096; skey=@KtEz3DlJm; pt2gguin=o1456586096; p_uin=o1456586096; pt4_token=Hm3z50bdGNXkxJ4IQ-aRGrmZasgeI5WFVoG025Eus*A_; p_skey=qC-Kzu2FFEifZfcWrpxW7hplR-9g08jcVMZ6iQlUZII_; scstat=2; qz_screen=1366x768; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=15; Loading=Yes; rv2=80965937798F367ACA698365A7E7DF0BAB684678C5102A6797; property20=33CA6F957A5668DAF67F3F74AB42CE303A9BB80375D67E82C0DD0D48809F661B306FBEAEC7E55ACB; qzspeedup=sdch'
'tvfe_boss_uuid=427f58974b3be55a; pac_uid=1_1456586096; mobileUV=1_1587a986661_413f5; _ga=GA1.2.1735770227.1479276331; pgv_pvi=1966100480; RK=uwWv1932Ob; o_cookie=1456586096; __Q_w_s__QZN_TodoMsgCnt=1; __Q_w_s_hat_seed=1; pgv_pvid=6264063782; _qpsvr_localtk=0.6042907023058073; pgv_si=s4574054400; pgv_info=ssid=s4451016985; ptisp=cm; ptcz=b0e601e63fda08c3f8afebeee333f36a347fbf2b0ebf7817aff5b159299186d8; uin=o1456586096; skey=@KtEz3DlJm; pt2gguin=o1456586096; p_uin=o1456586096; pt4_token=Hm3z50bdGNXkxJ4IQ-aRGrmZasgeI5WFVoG025Eus*A_; p_skey=qC-Kzu2FFEifZfcWrpxW7hplR-9g08jcVMZ6iQlUZII_; scstat=2; qz_screen=1366x768; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=15; rv2=80965937798F367ACA698365A7E7DF0BAB684678C5102A6797; property20=33CA6F957A5668DAF67F3F74AB42CE303A9BB80375D67E82C0DD0D48809F661B306FBEAEC7E55ACB; Loading=Yes; qzspeedup=sdch'