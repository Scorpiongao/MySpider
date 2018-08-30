'''
分析ajax请求，抓取街拍美图
'''

import requests
from urllib.parse  import  urlencode
import pymongo
import os
from hashlib import md5
from multiprocessing .pool import  Pool

client = pymongo .MongoClient ('localhost')
db = client ['photo']


def get_html(url,offset,keyword):
    '''
    获取索引页面
    :param url: https://www.toutiao.com/search_content/?offset=0&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&cur_tab=1&from=search_tab
    :return: json数据
    '''
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1,
        'from': 'search_tab'
    }

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }
    try:
        rsp = requests .get(url,params= data,headers =headers )
        if rsp.status_code ==200:
            return rsp.json()
    except Exception as e :
        print('[Error]: ',e.args )

def parse_json(data):
    '''
    解析json数据
    :param data: 返回的json数据类型
    :return:
    '''
    if data and 'data' in data.keys():
        items = data.get('data')
        for item in items :
            if 'image_list' in item.keys():
                title = item.get('title')
                image_list = item .get('image_list')
                #图片链接中为list时，得到的是小图，将list换成origin转为原图replace('list','origin')
                image_list = ['https:'+image.get('url').replace('list','origin') for image in image_list ]
                # print(title,image_list )
                yield {
                    'title':title ,
                    'image_list':image_list
                }


# def save_to_mongo(result):
#     '''
#     存储到mongodb
#     :param result:
#     :return:
#     '''
#     if db['jiepai'].insert(result ):
#         print('Save to MongoDB successfully.')
#     else:
#         print('Failed to save image.')

def save_image(result):
    '''存储为文件'''
    #文件的存储路径(可自定义路径)
    try:
        #根目录
        root = keyword
        if not os.path .exists(root) :
            os.mkdir(root)
            print(u'%s 文件夹创建成功'%root )

        title = result.get('title')
        #每个图集目录
        file_path = '{root}\{title}'.format(root=root,title=title)
        if not os.path .exists(file_path) :
            os.mkdir(file_path)
            print(u'%s 文件夹创建成功'%title)
    except Exception as e:
        print('[Error]: ',e.args )
    else:
        for image_url in result .get('image_list'):
            rsp = requests .get(image_url )
            if rsp.status_code ==200:
                images_path = '{0}\{1}.{2}'.format(file_path ,md5(rsp.content).hexdigest(),'jpg')
                if not os.path .exists(images_path ):
                    with open(images_path ,'wb')as f:
                        f.write(rsp.content )
                        print('保存图片成功。')
                else:
                    print('Already download %s'%image_url )
    # except :
    #     print('Failed to save images %s'%title)


def main(offset):
    url = 'https://www.toutiao.com/search_content/?'
    html = get_html(url,offset,keyword  )
    for result in parse_json(html):
        save_image(result)


#搜索关键字
keyword = '街拍'

Start_page = 0
End_page = 6

if __name__ == '__main__':

    # for offset in range(Start_page ,End_page ):
    #     main(offset*20)
    #开启多进程，进程池
    pool = Pool ()
    groups = [x*20 for x in range(Start_page ,End_page +1)]
    #pool.map(func,iterable)
    pool.map(main,groups )
    pool.close()
    pool.join()
