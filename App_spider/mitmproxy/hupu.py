'''
虎扑app抓取
'''

import requests
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 7.1.2; MI 5X Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36 kanqiu/7.2.10.16757/7241 isp/1 network/WIFI',
    'cookie':'_gamesu=NDE3MTYyNQ%3D%3D%7CMTUyNTY2OTU4Mw%3D%3D%7Ca899341c3156d132f7f53d61a8adccb0; u=30171472%7C5bOw5a2Q5piO%7C4c4b%7C4fdcf52a7a96b55ee9e37495c9aa1717%7C7a96b55ee9e37495%7CaHVwdV81ZWM5OTU1ZmIyMDY0YzVi; cpck=eyJwcm9qZWN0SWQiOiIxIiwiY2xpZW50IjoiODY4MDg0MDMxMDA5ODAxIiwiaWRmYSI6IiJ9; __dacevid3=0x98b5d49c51dd7ba8; __dacevid3=0x98b5d49c51dd7ba8; ua=21058481; cid=33739677',
    'authority':'bbs.mobileapi.hupu.com'
}

proxies = {
    'https':'http://192.168.23.5:8888',
    'http':'http://192.168.23.5:8888'
}


#分析过后crt,sign为变化值
params = {
    'nav':'buffer,nba,video,follow,cba,kog,lol,lrw,digital',
    'clientId':'33739677',
    'crt':'1537271946290',
    'night':'0',
    'lastTid':'0',
    'sign':'fffbec465037ba3d83cc17e84f84cff4',
    'stamp':'0',
    '_ssid':'IkFERVNLVE9QLTNIOTI5RFEi',
    'isHome':'1',
    'time_zone':'Asia/Shanghai',
    'additionTid':'-1',
    'token':'NDE3MTYyNQ==|MTUyNTY2OTU4Mw==|a899341c3156d132f7f53d61a8adccb0',
    'client':'868084031009801',
    'android_id':'87de9508fdd18f7b',
    'unfollowTid':''

}

# url ='https://bbs.mobileapi.hupu.com/1/7.2.10/recommend/getThreadsList?nav=buffer%2Cnba%2Cvideo%2Cfollow%2Ccba%2Ckog%2Clol%2Clrw%2Cdigital&clientId=33739677&crt=1537270515017&night=0&lastTid=23640720&sign=57c718149b5e4b70b928befe035cf00f&stamp=1537270202&_ssid=IkFERVNLVE9QLTNIOTI5RFEi&isHome=0&time_zone=Asia%2FShanghai&additionTid=&token=NDE3MTYyNQ%3D%3D%7CMTUyNTY2OTU4Mw%3D%3D%7Ca899341c3156d132f7f53d61a8adccb0&client=868084031009801&android_id=87de9508fdd18f7b&unfollowTid=23638019'
# url = 'https://bbs.mobileapi.hupu.com/1/7.2.10/recommend/getThreadsList'
def get_json(url):
    try:
        rsp =requests .get(url,params= params ,headers=headers ,proxies =proxies, verify=False)
        if rsp.status_code ==200:
            print(rsp.text)
            return rsp.json()
    except Exception as e:
        print('[ERROR]...',e.args )

def parse_json(data):
    if data:
        result = data.get('result')
        if result  and 'data' in result .keys():
            items = result .get('data')
            # print(len(items) )
            for item in items :
                # print(item)
                tid = item.get('tid')
                title = item.get('title')
                puid = item.get('puid')
                fid = item.get('fid')
                replies = item.get('replies')
                userName = item.get('userName')
                time = item.get('time'),
                if item.get('imgs') and len(item.get('imgs')) > 0:
                    imgs = [img for img in item.get('imgs') ]
                else:
                    imgs = []
                lightReply = item .get ('lightReply')
                forum = item.get('forum')
                forum_name = item .get('forum_name')
                yield {
                    'tid':tid,
                    'title':title,
                    'puid':puid,
                    'fid':fid,
                    'replies':replies ,
                    'userName':userName ,
                    'time':time,
                    'imgs':imgs,
                    'lightReply':lightReply ,
                    'forum':forum ,
                    'forum_name':forum_name
                }


if __name__ == '__main__':
    url = 'https://bbs.mobileapi.hupu.com/1/7.2.10/recommend/getThreadsList'
    json_data = get_json(url)
    for data in parse_json(json_data ):
        print(data)

