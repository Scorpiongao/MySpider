import requests
from cracker import Cracker

cracker=Cracker ()

search_url='http://music.163.com/weapi/cloudsearch/get/web?csrf_token='
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


def search( keyword, search_type, limit=10):
    params = {
        's': keyword,
        'type': search_type,
        'offset': 0,
        'sub': 'false',
        'limit': limit
    }
#  s: 搜索词
# limit: 返回数量
# sub: 意义不明(非必须参数)；取值：false
# type: #搜索类型,取值意义
#     1 单曲
#     10 专辑
#     100 歌手
#     1000 歌单
#     1002 用户
# offset: 偏移数量，用于分页
    post_data=cracker .get(params )
    try:
        res = requests.post(search_url, data=post_data,headers =headers )
        if res.status_code ==200:
            return res.json()
    except:
        print('[ERROR]:<search> error...')
        return None


# 根据歌名搜索
def search_by_songname( songname, limit=10):
    result = search(songname, search_type=1, limit=limit)
    print(result )
    if result['result']['songCount'] < 1:
        print('[INFO]: Song {} inexistence...'.format(songname))
        return None
    else:
        songs = result['result']['songs']

        print(songs )

        for s in songs:
            songid, songname = s['id'], s['name']
            print(songid ,songname )

# 根据歌手搜索
def search_by_singername( singername, limit=10):
    result = search(singername, search_type=100, limit=limit)
    print(result )
    if result['result']['artistCount'] < 1:
        print('[INFO]: Singer {} inexistence...'.format(singername))
        return None
    else:
        artist = result['result']['artists']

        print(artist )

if __name__ =="__main__":
    # html=search('林俊杰','100')
    # print(html)
    # search_by_songname('我们')
    search_by_singername('林俊杰')
