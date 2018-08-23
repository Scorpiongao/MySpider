from urllib import request, parse
from urllib .parse import  quote

'''
掌握对url进行参数编码的方法
需要使用parse模块
'''

if __name__ == '__main__':

    url = 'http://www.baidu.com/s?'
    wd = input("Input your keyword:")


    # 要想使用data， 需要使用字典结构
    qs = {
        "wd": wd
    }

    print(type(qs))
    # 转换url编码
    qs = parse.urlencode(qs)
    print(qs)

    fullurl = url + qs
    print(fullurl)

    #另一种解决中文乱码方式
    wd = quote(wd)
    print(wd)
    fullurl = url + 'wd='+wd
    print('quote解决方式: ',fullurl )

    # 如果直接用可读的带参数的url，是不能访问的
    #fullurl = 'http://www.baidu.com/s?wd=大熊猫'

    #相对网址变为绝对网址

    from urllib .parse import  urljoin
    base_url = 'http://www.baidu.com/s?wd='
    full_url = urljoin(base_url, wd)
    print('urljoin: ',full_url )

    rsp = request.urlopen(fullurl)

    html = rsp.read()


    # 使用get取值保证不会出错
    html = html.decode()

    print(html)