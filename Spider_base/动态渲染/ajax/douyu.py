'''
爬取斗鱼直播
'''

import requests
import pymongo
from multiprocessing import Pool


client = pymongo .MongoClient ('localhost')
db = client ['zhibo']
table = db['douyu']


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'Cookie':'dy_did=4f39aa9be11899c57d12efc600091501; acf_did=4f39aa9be11899c57d12efc600091501; smidV2=20180902230838348b8546def01cc0e55ba2151159eabd00547101a7cb48830; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1535900695,1535970288; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1535971018'
}


def get_html(url):
    try:
        rsp = requests .get(url,headers=headers)
        if rsp .status_code ==200:
            return rsp.json()
    except Exception as e:
        print('[Error...] ',e.args )


def parse_html(html):
    if html and 'data' in html.keys():
        data = html.get('data')
        if data and 'rl' in data .keys():
            results = data['rl']
            # print(results)
            # print(len(results))
            for result in results :
                result_data = {}
                # print(result)
                result_data['author'] = result .get('nn')
                result_data['tag'] = result .get('c2name')
                result_data['num'] = result .get('ol')
                result_data['desc_title'] = result .get('rn')
                result_data['img'] = result .get ('rs1')
                result_data['url'] = 'https://www.douyu.com'+result .get('url')
                result_data['uid'] = result .get('uid')
                result_data['rid'] = result .get('rid')

                print(result_data)
                save_to_mongo(result_data)

def save_to_mongo(data):
    if data :
        #去重处理
        if table .update_one({'rid':data['rid']},{'$set':data},True ):
            print('Save to mongodb successfully : %s'%data)
        else:
            print('Failed to save  %s.'%data)

def main(page):
    url = 'https://www.douyu.com/gapi/rkc/directory/0_0/{page}'.format(page=str(page) )
    html = get_html(url)
    parse_html(html)

START_PAGE = 1
END_PAGE = 50

if __name__ == '__main__':
    #开启多进程
    pool = Pool ()
    groups = [page for page in range(START_PAGE ,END_PAGE +1)]
    pool .map(main,groups)

    pool.close()
    pool.join()