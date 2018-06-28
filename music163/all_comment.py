'''
GET song or mv'all COMMENTS
'''
from Crypto.Cipher import AES
import base64
import requests
import json
from singer_id import SingerId
from db import MongoDB
from config import *
import pymongo
from singer import Singer
from song_id import SongId,MvId
import time
import random


class AllComment():
    def __init__(self,id,type):
        self.id=id
        self.type=type

        self.headers={
                'Host': 'music.163.com',
                'Referer': 'http://music.163.com/search/',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.32 Safari/537.36'
        }


    # first_param = '{rid:"", offset:"20", total:"false", limit:"20", csrf_token:""}'
        self.second_param = "010001"
        self.third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
        self.forth_param = "0CoJUm6Qyw8W8jud"

    def get_first_params(self,page):
        if page==0:
            first_param ='{rid:"", offset:"0", total:"true", limit:"20", csrf_token:""}'
            return first_param
        else:
            first_param ='{rid:"", offset:"%s", total:"false", limit:"20", csrf_token:""}'%(page*20)
            return first_param

    def get_params(self,page):
        iv = "0102030405060708"
        first_key = self.forth_param
        second_key = 16 * 'F'
        h_encText = self.AES_encrypt(self.get_first_params(page), first_key, iv)
        h_encText = self.AES_encrypt(h_encText, second_key, iv)
        return h_encText


    def get_encSecKey(self):
        encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
        # encSecKey ='09c44c314cd30b914ae5b499eb7fb760e10e7a2cd98fd156e41955bd3ab2224299d7a7bd5fbb63a9028c589d4a06714902bac766c26a9d7ec3294ba693ca2d6f7d3186938f002365ac9d6ad2bf0bd118f2741f4be941cbf8c240ed0a958cc1e74586989fa1b787967c192d47f3f8169a0085c19aea85fd34c56a841c01960568'
        return encSecKey


    def AES_encrypt(self,text, key, iv):
        pad = 16 - len(text) % 16
        if isinstance(text, bytes):
            text = text.decode('utf-8')
        text = text + str(pad * chr(pad))
        encryptor = AES.new(key, AES.MODE_CBC, iv)
        encrypt_text = encryptor.encrypt(text)
        encrypt_text = base64.b64encode(encrypt_text)
        return encrypt_text


    def get_json(self, params, encSecKey):
        if self.type=='song':
            url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_{song_id}/?csrf_token=".format(song_id =self.id )
        elif self.type == 'mv':
            url="https://music.163.com/weapi/v1/resource/comments/R_MV_5_{song_id}/?csrf_token=".format(song_id =self.id )
        else:
            print('type error',self.type )
        data = {
            "params": params,
            "encSecKey": encSecKey
        }
        response = requests.post(url, headers=self.headers, data=data)
        return response.text

    def get_total(self):
        json_text=self.get_json_text(0)
        print(json_text)
        total = int(json_text['total'])
        return total

    def get_json_text(self,page):
        params = self.get_params(page)
        # print(params)
        encSecKey = self.get_encSecKey()
        json_text = self.get_json(params, encSecKey)
        print(json_text)
        json_dict = json.loads(json_text)
        return json_dict

    def get_comments(self,json_text):
        if json_text :
            if json_text.get ('comments'):
                for item in json_text['comments']:
                    comment = {}
                    comment['commentId'] = item['commentId']
                    comment['content'] = item['content']
                    comment['likedCount'] = item['likedCount']
                    comment['time'] = item['time']
                    comment['avatarUrl'] = item['user']['avatarUrl']
                    comment['nickname'] = item['user']['nickname']
                    comment['userId'] = item['user']['userId']
                    comment['vipType'] = item['user']['vipType']
                    print(comment)

                    self.save_to_mongo(comment )


    def get_all_comments(self):
        total = self.get_total()
        for page in range(total // 20 + 1):
            json_text=self.get_json_text(page)
            self.get_comments(json_text)
            time.sleep(random .random )


    def save_to_mongo(self,result):
        if self.type =='song':
            print("Those are songs'comments" )
            if db[self .id ].update({'commentId':result ['commentId']},{'$set':result },True ):
                print('save to mongodb successfully',result ['content'])
            else:
                print('save to mongodb failed', result['content'])
        if self.type =='mv':
            print("Those are mvs'comments" )
            if db[self .id ].update({'commentId':result ['commentId']},{'$set':result },True ):
                print('save to mongodb successfully',result ['content'])
            else:
                print('save to mongodb failed', result['content'])



if __name__ =="__main__":
    client=pymongo .MongoClient (MONGO_URL ,connect= False )
    db=client [MONGO_DB ]
    type='mv'
    app=AllComment ('5876126','mv')
    app.get_all_comments()
