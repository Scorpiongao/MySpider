import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'Cookies':'ll="118254"; bid=ZVfTsIDvL18; _vwo_uuid_v2=9EF09FC0D84D430A20E2F0E73E097701|8b61b357e31d8edb531ddd37ba48ffc4; __yadk_uid=zXxx21iKkPXxrm8xsxr4khDCt4qRhXs9; __utma=30149280.1867949008.1514354002.1517149528.1518581734.4; __utma=223695111.534571572.1514354008.1517149528.1518581734.4; ap_v=1,6.0; _pk_id.100001.4cf6=d4486e89e48d4306.1514354008.5.1535128264.1518581746.; _pk_ses.100001.4cf6=*'
}

def get_page_text(url):
    '''获取html'''
    try:
        r=requests .get(url,headers =headers ,timeout=30)
        r.encoding = 'utf-8'
        return r.text
    except :
        print("异常！")

def parse_html(html):
    '''解析html'''
    soup = BeautifulSoup (html,'lxml')
    lis = soup.select('ol.grid_view li')
    # print(lis )
    if lis :
        for li in lis:
            rate = li.select('.item .pic em')[0].string
            href = li.select ('.item .pic a')[0].attrs['href']
            src = li.select ('.item .pic a img')[0].attrs['src']

            name = li.select('.item .info .hd .title')[0].get_text ()
            info = li.select('.item .info .bd p')[0].get_text ().strip()
            score = li.select('.item .info .bd .rating_num')[0].string
            commment_count = li.select('.item .info .bd .star span')[-1].string [:-3]
            inq = li.select('.item .info .inq') [0].string
            yield {
                'rate':rate,
                'name' : name,
                'href':href,
                'src':src,
                'score':score ,
                'comment_count':commment_count ,
                'inq':inq,
                'info':info
            }


def main(offset):
    '''主函数'''
    url = "https://movie.douban.com/top250?start=" + str(offset*25)
    html = get_page_text(url)
    for movie in parse_html(html):
        print(movie)
if __name__ == '__main__':
    for i in range(10):
        main(i)
