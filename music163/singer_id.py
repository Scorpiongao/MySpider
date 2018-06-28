'''
GET singers id
'''

import requests
import json
from config import *

headers={
        # 'Cookie':'vjuids=-b0fea809.1589f5c4f7c.0.fb20b0cc241b1; vjlast=1480142377.1480142377.30; _ntes_nuid=f2b8a3974eee64fd587db47fd213fcc2; __gads=ID=975756820220faec:T=1480142311:S=ALNI_Mb6iRbIQorOw21nQrAblHjCFb-VEw; _ga=GA1.2.909029746.1480142389; mail_psc_fingerprint=d73c7c79e0588d8b4a65b8242c354022; _ntes_nnid=f2b8a3974eee64fd587db47fd213fcc2,1516539426408; P_INFO=xiaoming__1228@163.com|1522298351|0|mail163|00&99|null&null&null#hub&420100#10#0#0|&0||xiaoming__1228@163.com; nts_mail_user=xiaoming__1228@163.com:-1:1; _ngd_tid=lHuWnlHIUCtJ5m42BYBGnIa1QDhWx3cm; WM_TID=feZwCVC6B9V3wnJvDy5GE6SRNbp8K9VI; JSESSIONID-WYYY=TrDUMIT0o%2FKq%2FfJtpSwzb%2FwHz8z%5CzPF8sntrm4OCR3CABTkCvBfhsjYCjMkKRePuw1NGV3h0rf%5CnaEfzyD6H86DKQh2BRkZ5VAjz24nr1FJcsaM359v1Klqc75qfQh%2BV4NGjy5MW80v9BayJb%2B7REcqDjjSPlS%5C8NIceh7fvwHInXY60%3A1528176162353; _iuqxldmzr_=32; __utma=94650624.909029746.1480142389.1528127754.1528172628.17; __utmb=94650624.16.10.1528172628; __utmc=94650624; __utmz=94650624.1517401171.1.1.utmcsr=sogou.com|utmccn=(referral)|utmcmd=referral|utmcct=/link',
        'Host': 'music.163.com',
        'Referer': 'https://music.163.com/discover/artist',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.32 Safari/537.36'
}

data1={
        'params':PARAMS1 ,
        'encSecKey':ENCSECKEY1
    }

data2 = {
    'params': PARAMS2,
    'encSecKey': ENCSECKEY2
}



class SingerId():
    def __init__(self,url):
        self.headers=headers
        self.data=[data1,data2]
        self.url=url

    def get_json(self):
        try:
            for data in self.data :
                response=requests .post(self.url,data= data,headers =self.headers )
                if response .status_code ==200:
                    # print(response .text )
                    for artist in self.parse_json(response.text):
                        yield artist

        except requests .ConnectionError as e:
            print('Request get json error',e.args )


    def parse_json(self,html):
        try:
            json_obj=json .loads(html)
            if json_obj ['artists']:
                for artist_dict in json_obj ['artists']:
                    artist={}
                    artist['name'] = artist_dict['name']
                    artist['id'] = artist_dict['id']
                    artist['alias'] = artist_dict['alias']
                    artist['musicSize'] = artist_dict['musicSize']
                    artist['albumSize']=artist_dict ['albumSize']
                    artist['picUrl']=artist_dict ['picUrl']

                    yield artist

        except json .JSONDecodeError as e:
            print('Parse json error',e.args )

if __name__ =="__main__":
    singer=SingerId(GET_SINGER_URL)
    for artist in singer .get_json():
        print(artist)
    # for artist in singer .get_json() :
    #     print(artist )


    # url='https://music.163.com/weapi/artist/top?csrf_token='


