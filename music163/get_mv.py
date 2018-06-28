import requests
from cracker import Cracker

mv_url='https://music.163.com/weapi/song/enhance/play/mv/url?csrf_token='

headers={
        'Accept': '*/*',
        'Accept-Encoding': 'gzip,deflate,sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'music.163.com',
        'Referer': 'http://music.163.com/search/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.32 Safari/537.36'

}
def get_mv_url(mv_id):
    try:
        params={
            # 'id':'375130',#mv_id
            'id':mv_id,
            'r':1080,
            # 'csrf_token':''
        }
        post_data=cracker.get(params)

        res=requests .post(mv_url ,data=post_data,headers =headers  )
        if res.status_code ==200:
            print(res.text )

    except requests .ConnectionError as e:
        print('request error',e.args )

if __name__ =="__main__":
    cracker=Cracker ()
    mv_id='375130'
    get_mv_url(mv_id)