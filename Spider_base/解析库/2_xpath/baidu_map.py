import json
from urllib .request import  urlopen,quote
import pandas as pd
import csv
import requests

def get_lng_lat(address):
    base_url='http://api.map.baidu.com/geocoder/v2/'
    output='json'
    ak='eiBsqVc0S5kzztKhU1vwM2WWdTGYQteL'#申请的秘钥
    add=quote(address ) #城市名为中文，防止出现乱码，先用quote编码
    url=base_url +'?'+'address='+add +'&output='+output +'&ak='+ak
    # req=urlopen(url)
    req=requests .get(url)

    temp=req.json()
    # print(temp )
    # res=req.read().decode()#将其它编码的字符串解码成unicode
    # temp=json .loads(res)#对json数据进行解析
    return temp

file=open(r'武汉住房.json','w')#j建立json数据文件
with open(r'F:\all-result\zu_fang2.csv','r')as csvfile:#打开csv
    reader=csv.reader(csvfile )
    for line in reader :
        if reader .line_num==1:#忽略第一行
            continue
        b=line[0].strip()#将第一列address读取出来
        c=line[7].strip()

        lng=get_lng_lat(b)['result']['location']['lng']#经度
        lat = get_lng_lat(b)['result']['location']['lat']#纬度
        str_semp='{"lat":'+str(lat)+',"lng":'+str(lng)+',"count":'+str(c)+'},'
        print(str_semp )
        file.write(str_semp )
file .close()