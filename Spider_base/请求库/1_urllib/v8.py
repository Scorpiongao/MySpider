'''
URLError的使用
'''

from urllib import request, error


if __name__ == '__main__':

    url1 = "http:iiiiiiiiidu//www.baidu.com/welcome.html"##urlerror

    url2 = "http://www.sipo.gov.cn/www"#httperror
    try:

        req = request.Request(url2)
        rsp = request.urlopen( req )
        html = rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print("HTTPError: {0}".format(e.reason))
        print("HTTPError: {0}".format(e))
        print('code: %s'%e.code)
        print('headers: %s'%e.headers )

    except error.URLError as e:
        print("URLError: {0}".format(e.reason))
        print("URLError: {0}".format(e))

    except Exception as e:
        print(e)
