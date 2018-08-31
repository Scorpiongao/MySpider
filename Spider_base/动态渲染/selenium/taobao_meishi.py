from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium .common .exceptions import  TimeoutException
import time
from pyquery import PyQuery as pq
import pymongo
from urllib .parse import  quote

MONGO_URL='localhost'#设置MONGODB配置
MONGO_DB='taobao'#数据库名
MONGO_TABLE= 'food'

client=pymongo .MongoClient (MONGO_URL )#连接MONGODB
db=client [MONGO_DB ]

#chrome无界面配置，像phantomJS一样
chrome_options = webdriver .ChromeOptions ()
chrome_options .add_argument('--headless')

browser = webdriver .Chrome (chrome_options=chrome_options)
#屏幕最大化
# browser .maximize_window()
#指定最长等待时间
wait=WebDriverWait (browser ,10)


def index_page(page):
    '''
    抓取索引页
    :param page: 页码
    :return:
    '''
    print('正在抓取第 ',page,' 页')
    try:
        url = "https://s.taobao.com/search?q=" + quote(KEYWORD)
        browser  .get(url)
        #EC.presence_of_element_located（）是确认元素是否已经出现了
        #EC.element_to_be_clickable（）是确认元素是否是可点击的
        if page > 1:
            input=wait.until(EC.presence_of_element_located ((By.CSS_SELECTOR ,'#mainsrp-pager div.form .J_Input')))
            submit=wait .until(EC .element_to_be_clickable ((By.CSS_SELECTOR ,'#mainsrp-pager div.form .J_Submit')))
            input.clear()
            input .send_keys(page)
            submit .click()
        wait.until(EC.text_to_be_present_in_element ((By .CSS_SELECTOR ,'#mainsrp-pager li.item.active .num'),str(page)))
        wait .until(EC .presence_of_element_located((By .CSS_SELECTOR ,'#mainsrp-itemlist .items .item')) )
        get_products()
    except TimeoutException  :
        #抛出超时异常后，再调用函数本身
        return index_page(page)


def get_products():
    '''
    商品数据解析，pq库
    :return:
    '''
    html = browser .page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    try:
        for item in items:
            product = {
                'image': 'https:'+item('.pic .img').attr('data-src') ,
                'href': 'https:'+item ('.title .J_ClickStat').attr('href'),
                'price': item('.price').text().replace('\n','') ,
                'deal': item('.deal-cnt').text(),
                'title':item ('.title').text().replace('\n','')  ,
                'shop':item ('.shop').text() ,
                'location': item ('.location').text()

            }
            print(product)
            # save_to_mongodb(product)
    except TypeError:
        print('[TypeError]....')



def save_to_mongodb(result):
    try:
        if db[MONGO_TABLE ].insert(result ):
            print('保存到MONGODB成功！',result )
    except Exception :
        print('保存到MONGODB失败！',result)

def main():
    '''循环遍历'''
    for i in range(START_PAGE,END_PAGE+1):
        time.sleep(1)
        index_page(i)


KEYWORD = '美食'
START_PAGE = 1
END_PAGE = 100

if __name__ =="__main__":
    main()