'''
模拟登陆-豆瓣
'''

import requests
from pyquery import PyQuery as pq
import re

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}

def captcha():
    '''获取验证码及其id'''
    url = 'https://accounts.douban.com/login'
    html = requests .get(url,headers =headers ).text
    doc = pq(html)
    captcha_url = doc('.item-captcha img').attr('src')
    print(captcha_url )
    pattern = re.compile(r'id=(.*?)&size')
    captcha_id = pattern .search(captcha_url)
    # print(captcha_id.group(1))
    with open('captcha.png','wb')as f:
        f.write(requests .get(captcha_url ).content )
    # captcha = input('Please input captcha: ')
    return captcha_id.group(1)


captcha_id = captcha()
captcha = input('Please input captcha: ')

def login():
    url = 'https://accounts.douban.com/login'
    form_data = {
        'source': 'None',
        'redir': 'https://www.douban.com',
        'form_email': '1456586096@qq.com',
        'form_password': 'mlf123456',
        'captcha-solution': captcha,
        'captcha-id': captcha_id ,
        'login': '登录'
    }

    rsp = requests .post(url,data=form_data,headers =headers )
    if rsp.status_code ==200:
        print('登录成功！')
        return rsp.text


if __name__ == '__main__':
    html = login()
    print(html)