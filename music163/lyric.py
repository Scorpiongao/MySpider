'''
GET songs'lyric and songs'url
'''
import requests
from urllib .parse import  urlencode
from cracker import Cracker
import json
import re
from singer_id import SingerId
from config import *
from song_id import SongId


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

class Song():
    def __init__(self,id):
        self.headers=headers
        self.id=id
        self.cracker = Cracker()


    def get_lyric_html(self):
        url='http://music.163.com/api/song/lyric'
        # base_url ='http://music.163.com/weapi/v1/resource/comments/R_SO_4_30953009/?csrf_token='
        # 'http://music.163.com/api/song/lyric'
        # https://music.163.com/weapi/song/lyric?csrf_token=
        params={
            'id':self.id,
            'lv':1,
            'kv':1,
            'tv':-1
        }
        try:
            response=requests .post(url,data =params,headers=self.headers  )
            if response .status_code ==200:
                # return response .text
                self.parse_json(response .text)
        except requests.ConnectionError as e:
            print('post lyric error',e.args )


    def parse_json(self,html):
        j = json.loads(html)
        if j['lrc']['lyric']:
            lrc = j['lrc']['lyric']
            pat = re.compile(r'\[.*\]')
            lrc1 = re.sub(pat, "", lrc)
            lrc = lrc1.strip()
            # print(pat,lrc1,lrc ,sep= '\n' )
            print(lrc)
        else:
            lrc = u"暂无歌词"
            print(lrc)

    def get_song_data(self,base_url):
        params = {
            'ids': [self.id],
            'br': 320000,
            'csrf_token': ''
        }
        post_data=self.cracker.get(params )
        try:
            response = requests.post(base_url, data=post_data, headers=self.headers)
            if response.status_code == 200:
                # return response.json()
                # print(response .text)
                self.get_down_song_url(response .json() )
        except requests.ConnectionError as e:
            print('post lyric error', e.args)

    def get_down_song_url(self,data):
        if data:
            song_url=data['data'][0]['url']
            print(song_url )
            return song_url

    def run(self):
        # self.get_lyric_html()
        self.get_song_data(base_url= GET_SONG_URL)

if __name__=="__main__":
    # id='210049'
    # songs = SongId()
    # for data in songs.get_song_id():
    #     song_id = data['song_id']
    #     # singerId = data['singerId']
    #     # singername = data['singername']
    #     # song = data['song']
    #     song=Song (song_id)
    #     song .run()
    song_id='185694'
    song = Song(song_id)
    song .run()
