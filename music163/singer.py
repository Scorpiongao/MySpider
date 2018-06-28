'''
GET singers' info
'''
import requests
from pyquery import PyQuery as pq
from urllib .parse import  urlencode
from config import *
import re
from singer_id import SingerId
from db import MongoDB
import time
import random

mongoDB=MongoDB (MONGO_TABLE2)


class Singer():

    def __init__(self,id,name):

        self.id=id
        self.name=name
        self.base_url=Base_URL
        self.headers={
                    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Encoding':'gzip, deflate, sdch',
                    'Accept-Language':'zh-CN,zh;q=0.8',
                    'Connection':'keep-alive',
                    'Cookie':'vjuids=-b0fea809.1589f5c4f7c.0.fb20b0cc241b1; vjlast=1480142377.1480142377.30; _ntes_nuid=f2b8a3974eee64fd587db47fd213fcc2; __gads=ID=975756820220faec:T=1480142311:S=ALNI_Mb6iRbIQorOw21nQrAblHjCFb-VEw; _ga=GA1.2.909029746.1480142389; mail_psc_fingerprint=d73c7c79e0588d8b4a65b8242c354022; _ntes_nnid=f2b8a3974eee64fd587db47fd213fcc2,1516539426408; P_INFO=xiaoming__1228@163.com|1522298351|0|mail163|00&99|null&null&null#hub&420100#10#0#0|&0||xiaoming__1228@163.com; nts_mail_user=xiaoming__1228@163.com:-1:1; _ngd_tid=lHuWnlHIUCtJ5m42BYBGnIa1QDhWx3cm; WM_TID=SHHA2olDRArzY6gkv0JBCZ%2FYHgxEvA4l; JSESSIONID-WYYY=q%5CFmfjP1VjBvJTVAqKt6E0oTK7SPw7D6U926M02YwPvCvKsApxq7NBgQn7Woc%5CMymi%5CTR7%2F1etY2%2Btr8Ejg4%5CVAE%2Bm4OWVc7xr%5C1qKRknX07jW022pNaJePFlj61%2BVvOij9%2B2dSgHgRRFvMPjb2HJkfrQdN%2Bv0u%5C799PKk2pszImhyYb%3A1528031143985; _iuqxldmzr_=32; playerid=46589295; __utma=94650624.909029746.1480142389.1528027602.1528029759.9; __utmb=94650624.5.10.1528029759; __utmc=94650624; __utmz=94650624.1517401171.1.1.utmcsr=sogou.com|utmccn=(referral)|utmcmd=referral|utmcct=/link',
                    'Host':'music.163.com',
                    'Referer':'http://music.163.com/',
                    'Upgrade-Insecure-Requests':'1',
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
                }


    def get_singer_url(self):
        url = self.base_url +'/artist/desc?id={}'.format(self.id)
        return url

    def request(self,url):
        try:
            response=requests .get(url,headers =self.headers )
            if response .status_code ==200:
                return response .text
            else:
                return None
        except requests.ConnectionError as e:
            print('request error : ',url ,e.args )


    def parse_singer_html(self,html):
        h2s=[]
        ps=[]
        singer={}
        doc=pq (html)
        container=doc('div .n-artdesc')
        # print(container )
        if container :
            try:
                for p in container ('p').items() :
                    ps.append(p.text())
                for h2 in container ('h2').items():
                    h2s.append(h2.text())
                for h2,p in zip(h2s ,ps ):
                    singer[h2]=p
                print(singer )
                #
                return singer
            except :
                print('parse singer_info error')

    def get_songs_url(self):
        url = self.base_url + '/artist?id={}'.format(self.id)
        return url

    def parse_songs_html(self,html):
        songs_list=[]
        doc=pq (html)
        container=doc('ul.f-hide')
        # print(container )
        for a in container ('a').items() :
            song_dict={}
            song=a.text()
            href=self.base_url +a.attr('href')
            # print(song ,href)
            song_dict ['name' ]=song
            song_dict ['href' ]=href
            songs_list.append(song_dict )
        print(songs_list)
        return songs_list

    def get_album_url(self):
        url = self.base_url + '/artist/album?id={}'.format(self.id)
        return url


    def parse_album_html(self,html):
        ablum_list=[]
        ablum_detail=[]
        if html:
            doc=pq (html)
            container=doc('#m-song-module')
            for a in container ('a.tit.s-fc0').items():
                album_dict={}
                ablum=a.text()
                href=a.attr('href')
                album_dict ['ablum' ]=ablum
                album_dict ['href' ]=self.base_url +href

                ablum_list .append(album_dict )

                html=self.request(album_dict ['href' ])
                ablum_detail.append(self.parse_ablum_detail(album_dict ['href' ],html))

            ablum_detail_list.append(ablum_detail)
            # yield self.parse_ablum_detail(album_dict ['href' ],html)
            # yield ablum_detail_list
            # print(ablum_list )
            # return ablum_list

            # for time in container ('.s-fc3').items() :
            #     time_list .append(time.text())
            # print(time_list )

            next_url=doc('.zbtn.znxt')
            if next_url :
                url=self.base_url +next_url.attr('href')
                if not 'javascript' in url:
                    html=self.request(url)
                    self.parse_album_html(html)
                    time.sleep(random.randint(1, 4))


    def parse_ablum_detail(self,url,html):
        result={}
        songs_list=[]
        if html:
            doc=pq(html)
            try:
                ablum=doc('h2.f-ff2').text()
                # print('ablum:',ablum)
                artist=doc('p.intr a').text()
                time=doc('p.intr').text().strip().split(' ')[1][5:]
                company=doc('p.intr').text().strip().split(' ')[-1]
                # print(artist ,time,company )
                desc=doc('#album-desc-dot').text()

                container=doc('.f-hide')
                for song in container('a').items() :
                    song_dict={}
                    name=song.text()
                    href=song .attr('href')
                    song_dict ['name']=name
                    song_dict ['href']=self.base_url+href
                    songs_list .append(song_dict )
                # print(songs_list)
                result['ablum']=ablum
                result['href']=url
                result['artist']=artist
                result['time']=time
                result['company']=company
                result['desc']=desc
                result['total']=len(songs_list)
                result['songslist']=songs_list
                print(result )
                return result
            except:
                print('parse ablum detail error',url)



    def get_mv_url(self):
        url = self.base_url + '/artist/mv?id={}'.format(self.id)
        print(url)
        return url

    def parse_mv_html(self,html):
        mv_list=[]
        mv_detail=[]
        if html:
            doc=pq (html)
            container=doc('.tit.f-thide.s-fc0')
            for a in container ('a').items() :
                mv_dict={}
                mv=a.text()
                href=self.base_url+a.attr('href')
                mv_dict ['mv']=mv
                mv_dict ['href']=href
                # mv_list .append(mv_dict )
                # print(mv_dict)
                html=self.request(mv_dict['href'])
                mv_detail.append(self.parse_mv_detail(mv_dict ['mv'],mv_dict['href'],html))

            mv_detail_list.append(mv_detail)
                # yield self.parse_mv_detail(mv_dict ['mv'],mv_dict['href'],html)
            # print(mv_detail_list)
            # print(mv_list )
            # yield mv_list

            next_url=doc ('.zbtn.znxt')
            if next_url :
                new_url=self.base_url +next_url .attr('href')
                if not 'javascript' in new_url:
                    html=self.request(new_url)
                    self.parse_mv_html(html)
                    time.sleep(random .randint (1,4))


    def parse_mv_detail(self,mv,url,html):
        result={}
        if html:
            doc=pq(html)
            try:
                time=doc ('.m-mvintr .s-fc4').text().split(' ')[0][5:]
                playcount=doc ('.m-mvintr .s-fc4').text().split(' ')[1][5:]
                # print(time,playcount )
                desc=doc('.intr').text()
                # print(desc )
                result['href']=url
                result ['mv']=mv
                result ['time']=time
                result ['playcount']=playcount
                result ['desc']=desc

                print(result)
                return result
            except IndexError:
                print('IndexError',mv)




    def main(self):
        singer_data={}
        singer_data ['id']=self .id
        singer_data['name'] = self.name
        singer_data['alias']=alias
        singer_data['musicSize']=musicSize
        singer_data['albumSize']=albumSize
        singer_data['picUrl']=picUrl

        print('---' * 10)
        print(u'歌手信息')
        print('---' * 10)
        singer_url=self.get_singer_url()
        html=self.request(singer_url)
        singer_data['singer_intr']=self.parse_singer_html(html)

        print('---'*10)
        print(u'歌手的50首热门歌曲')
        print('---' * 10)
        song_url=self.get_songs_url()
        html=self.request(song_url )
        singer_data['songs_list']=self.parse_songs_html(html)
        # print(singer_data['songs_list'])

        print('---' * 10)
        print(u'歌手的所有专辑')
        print('---' * 10)
        album_url = self.get_album_url()
        html = self.request(album_url)
        self.parse_album_html(html)
        print(ablum_detail_list )
        singer_data['singer_ablums']=ablum_detail_list
        # singer_data ['singer_ablums']=[ablum for ablum in self.parse_album_html(html)]
        # singer_data['singer_ablums']=ablums
        print('---' * 10)
        print(u'歌手的所有MV')
        print('---' * 10)
        mv_url=self.get_mv_url()
        html=self.request(mv_url)
        self.parse_mv_html(html)
        print(mv_detail_list )
        singer_data['singer_mvs']=mv_detail_list
        self.parse_mv_html(html)

        print(singer_data )
        mongoDB.save_to_mongo(singer_data)

if __name__ =='__main__':
    # id = '3684'
    sleep=random .randint (1,5)
    ablum_detail_list = []
    mv_detail_list = []

    singer_id=SingerId (GET_SINGER_URL)
    for artist in singer_id .get_json():
        id=artist ['id']
        name=artist['name']
        alias=artist['alias']
        musicSize=artist['musicSize']
        albumSize=artist['albumSize']
        picUrl=artist['picUrl']

        if mongoDB.filter(id):
            print('%s already in mongodb'%id ,name)
        else:
            singer = Singer(id,name )
            singer.main()
        time.sleep(sleep)