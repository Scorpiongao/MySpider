import requests
from cracker import Cracker
import os


class Downloader():
    def __init__(self,id,name,type):
        self.id=id
        self.name=name
        #type==0--->song,
        #type==1--->mv
        self.type=type
        self.headers={
            'Accept': '*/*',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'music.163.com',
            'Referer': 'http://music.163.com/search/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.32 Safari/537.36'
    }

        self.song_url='http://music.163.com/weapi/song/enhance/player/url?csrf_token='

        self.mv_url='https://music.163.com/weapi/song/enhance/play/mv/url?csrf_token='

        self.cracker=Cracker ()

    def get_data(self):
        if self.type =="0" or self.type==0:
            params = {
                'ids': [self.id],
                'br': 320000,
                'csrf_token': ''
            }
            post_data=self.cracker.get(params )
            url=self.song_url

        elif self.type=="1" or self.type==1:
            params = {
                # 'id':'375130',#mv_id
                'id': self.id,
                'r': 1080,
                # 'csrf_token':''
            }
            post_data = self.cracker.get(params)
            url=self.mv_url
        try:
            response=requests .post(url,data=post_data ,headers=self.headers)
            if response.status_code == 200:
                    new_url=self.get_down_url(response .json() )
                    return new_url
        except requests.ConnectionError as e:
            print('post lyric error', e.args)

    def get_down_url(self,data):
        if data:
            if self.type == "0" or self.type == 0:

                down_url=data['data'][0]['url']

            if self.type=="1" or self.type==1:
                down_url = data['data']['url']
            # print(song_url )
            return down_url

    # 根据歌曲下载地址下载歌曲
    def download( self,url):
        if self.type =="0" or self.type==0:
            save_file=r'D:\Media\music'
            if not os.path.exists(save_file):
                os.makedirs(save_file)
            fpath = '{0}/{1}.{2}'.format(save_file,self.name,'mp3')

        if self.type=="1" or self.type==1:
            save_file = r'D:\Media\video'
            if not os.path.exists(save_file):
                os.makedirs(save_file)
            fpath = '{0}/{1}.{2}'.format(save_file, self.name, 'mp4')
        if not os.path.exists(fpath):
            with open(fpath, 'wb') as f:
                response=requests .get(url)
                if response .status_code ==200:
                    f.write(response.content)
                    print('Download %s successfully'%self.id,self.name)

        else:
            print('%s already exists'%self.id,self.name)

    def run(self):
        url=self.get_data()
        self.download(url)

if __name__ =="__main__":
    song_id='298317'
    # url=get_song_data(song_id)
    # download(url,name= '屋顶')

    mv_id='186025'
    # url=get_mv_url(mv_id )
    # download_mv(url,name="布拉格广场")
    app=Downloader (mv_id,name='布拉格广场',type=1)
    app.run()
