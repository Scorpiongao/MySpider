'''
爬去丑事百科， xpath解析页面
'''

import requests
import json
from lxml import etree


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}

def get_html(page):
    '''获取索引页面'''
    try:
        url = 'https://www.qiushibaike.com/hot/page/{page}/'.format(page=str(page))
        rsp = requests .get(url,headers= headers)
        if rsp.status_code ==200:
            print('正在爬取第 %s 页'%page)
            return rsp.text
    except Exception as e :
        print('[Error] ',e.args )

    # html = rsp.text

# print(html)
#解析页面，形成标签树
def parse_html(html):
    '''解析页面'''
    data = {}
    doc = etree.HTML(html)
    articles = doc.xpath('//div[@id="content-left"]')[0]

    articles = articles .xpath('./div[contains(@class,"article")]')

    for article in articles  :
        # print(article )
        #作者信息
        author = article .xpath('.//div[contains(@class,"author")]/a')
        # print(author)
        if len(author) >0 :
            href = 'https://www.qiushibaike.com'+author [0].xpath('./@href')[0].strip('\n')
            img = 'https:'+author [0].xpath('./img/@src')[0].replace('thumb','medium').split('?')[0]
            name = author[1].xpath('./h2/text()')[0].strip('\n')
            # print(href,img,name)
            data['href'] = href
            data['img'] =img
            data['name'] =name
        #性别和年龄
        gender_age = article .xpath('.//div[contains(@class,"articleGender")]')
        # print(gender_age )
        if len(gender_age):
            gender = gender_age [0].xpath('./@class')[0].strip('articleGender ')[:-3]
            age = gender_age [0].xpath('./text()')[0]
            # print(gender ,age )
            data['gender'] = gender
            data['age'] = age
        #文章内容
        contents = article .xpath('./a/div[@class="content"]/span/text()')
        if len(contents ) > 0:
            # print(contents[0].strip('\n'))
            content = contents [0].strip('\n')
            data['content'] =content
        #文章链接
        article_href = article .xpath('./a')
        if len(article_href ) > 0:
            # print(article_href [0].xpath('./@href')[0])
            article_href = article_href [0].xpath('./@href')[0]
            data['article_href'] = 'https://www.qiushibaike.com'+article_href
        #文章的图片
        article_pic = article .xpath ('./div[@class="thumb"]/a')
        if len(article_pic) > 0 :
            article_pic ='https:'+ article_pic [0].xpath('./img/@src')[0]
            data['article_pic'] = article_pic
        #文章好笑数与评论数
        stats = article.xpath('./div[@class="stats"]')
        # print(stats)
        if len(stats ) > 0:
            vote = stats [0].xpath('./span[@class="stats-vote"]/i/text()')[0]
            comments_count = stats [0].xpath('./span[@class="stats-comments"]/a/i/text()')[0]
            # print(vote,comments_count)

            data['vote'] = vote
            data['comments_count'] = comments_count

        print(data)
        save_to_json(data)

def save_to_json(data):
    '''存储为json文件'''
    if data:
        file_name = 'qiushibaike.json'
        with open(file_name ,'a',encoding= 'utf-8') as f:
            f.write(json .dumps(data,indent=2,ensure_ascii= False ))

START_PAGE = 1
END_PAGE = 5

if __name__ == '__main__':
    for page in range(START_PAGE ,END_PAGE +1):
        html = get_html(page)
        parse_html(html)