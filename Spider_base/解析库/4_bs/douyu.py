''''
任务：
爬去斗鱼直播内容
https://www.douyu.com/directory/all
'''
from bs4 import BeautifulSoup
import json
import requests


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    # 'Cookies':'ll="118254"; bid=ZVfTsIDvL18; _vwo_uuid_v2=9EF09FC0D84D430A20E2F0E73E097701|8b61b357e31d8edb531ddd37ba48ffc4; __yadk_uid=zXxx21iKkPXxrm8xsxr4khDCt4qRhXs9; __utma=30149280.1867949008.1514354002.1517149528.1518581734.4; __utma=223695111.534571572.1514354008.1517149528.1518581734.4; ap_v=1,6.0; _pk_id.100001.4cf6=d4486e89e48d4306.1514354008.5.1535128264.1518581746.; _pk_ses.100001.4cf6=*'
}


def get_html(url):
    '''获取首页html'''
    try:
        rsp = requests.get(url,headers= headers)
        if rsp.status_code ==200:
            return rsp.text
    except Exception as e:
        print('[Error]... ',e.args )


def parse_html(html):
    '''bs4解析html内容'''
    soup = BeautifulSoup (html,'lxml')
    items = soup.select('#live-list-contentbox li')
    for item in items :
        href = 'https://www.douyu.com'+ item.select('a.play-list-link')[0] .attrs['href']
        img = item .select('img.JS_listthumb')[0].attrs['data-original'].strip('\n')
        ellipsis = item .select('h3') [0].text.strip()
        tag = item.select('.tag')[0].text.strip()
        name = item.select('.dy-name')[0] .text.strip()
        num = item .select('.dy-num')[0].text
        # print(href,img,ellipsis,tag,name,num)
        result = {
            'ellipsis':ellipsis ,
            'tag':tag,
            'name':name,
            'href':href,
            'img':img,
            'num':num
        }
        save_to_json(result)
        print(result)

def save_to_json(result):
    '''存储为json文件'''
    if result:
        with open('douyu.json','a',encoding= 'utf-8') as f:
            f.write(json.dumps(result,indent= 2,ensure_ascii= False ))

if __name__ == '__main__':
    url = 'https://www.douyu.com/directory/all'
    html = get_html(url)
    parse_html(html)
