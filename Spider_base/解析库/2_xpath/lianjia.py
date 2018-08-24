import requests
from lxml import etree
import os
import pandas
from multiprocessing import Pool

# os.chdir(r'F:\all-result')

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
def get_page_index(url):
    try:
        r=requests .get(url,headers=header )
        r.raise_for_status()
        r.encoding ='utf-8'
        return r.text
    except :
        print('异常！')
        return None
def get_page_url(html):
    s=etree .HTML(html)
    #titles=s.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/ul/li/div[2]/h2/a/text()')
    hrefs=s.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/ul/li/div[2]/h2/a/@href')
    return hrefs

def parse_page_details(html):
    s=etree .HTML(html)
    try:
        titles=s.xpath('/html/body/div[4]/div[1]/div/div[1]/h1/text()')[0]
        price=s.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/span[1]/text()')[0]
                     #/html/body/div[4]/div[2]/div[2]/div[1]/span[1]
        lf_size=s.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/p[1]/text()')[0]
        lf_type=s.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/p[2]/text()')[0]
        lf_hight=s.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/p[3]/text()')[0]
        lf_direction=s.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/p[4]/text()')[0]
        lf_subway=s.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/p[5]/text()')[0]
        if len(s.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/p[6]/a[2]/text()'))>0 :
            lf_community=s.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/p[6]/a[1]/text()')[0]+'-'+s.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/p[6]/a[2]/text()')[0]

        lf_address=s.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/p[7]/a[1]/text()')[0]+'-'+s.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/p[7]/a[2]/text()')[0]
        lf_date=s.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/p[8]/text()')[0]
        lf_num=s.xpath('/html/body/div[8]/div[2]/div[2]/text()')[0]
                      #/html/body/div[8]/div[2]/div[2]
                      #/html/body/div[8]/div[2]/div[2]
        #print(lf_num )
        return titles,price,lf_size,lf_type,lf_hight,lf_direction,lf_subway,lf_community,lf_address,lf_date,lf_num
    except IndexError :
        pass
hrefs_list = []

title_list=[]
price_list=[]
size_list=[]
type_list=[]
hight_list=[]
direction_list=[]
subway_list=[]
community_list=[]
address_list=[]
date_list=[]
num_count=[]

def main():
    try:
    #https: // wh.lianjia.com / zufang / pg2 /
    #https: // wh.lianjia.com / zufang / pg100 /
        for i in range(1,15):
            url='https://wh.lianjia.com/zufang/pg'+str(i)+"/"
            html= get_page_index(url)

            for url in get_page_url(html):
                #print(url )
                html=get_page_index(url)
                title,price,size,type,hight,direction,subway,community,address,date,num=parse_page_details(html)
                hrefs_list .append(url )
                title_list .append(title )
                price_list .append(price )
                size_list .append(size )
                type_list .append(type )
                hight_list .append(hight )
                direction_list .append(direction)
                subway_list .append(subway )
                community_list .append(community )
                address_list .append(address )
                date_list .append(date)
                num_count .append(num)

            print(len(hrefs_list), len(title_list), len(price_list), len(size_list), len(type_list),
                  len(hight_list),len(direction_list ),len(subway_list ),len(community_list ),
                  len(address_list),len(date_list),len(num_count )      )
    except :
        pass



if __name__ =='__main__':

   # pool=Pool ()
   # pool.map(main,[i*1 for i in range(1,11)])
    main()
    data={
        'href':hrefs_list,'title':title_list,'price':price_list ,'size':size_list ,'type':type_list ,
        'hight':hight_list,'direction':direction_list ,'subway':subway_list ,'community':community_list ,
        'address':address_list ,'date':date_list,'num_count':num_count
    }
    zu_fang=pandas .DataFrame (data)
    zu_fang .to_csv ('zu_fang.csv',encoding= 'utf_8_sig')
    zu_fang .info()
    zu_fang .head(5)
