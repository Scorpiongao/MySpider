import requests
import re
import json
from multiprocessing import Pool  #多进程秒爬数据

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'Cookies':'__mta=210680106.1535102473518.1535102473518.1535102473518.1"; uuid_n_v=v1; uuid=F0C76F40A77E11E8B64BAF79690B7FDA8B0D53718B9940698F7AC6687B56514D; _csrf=5c8c61bd467a67c69f23df42a85f03cc6477a2bfb0e51d9e0a7901f40c6e0a73; _lxsdk_cuid=1656b3cbf24c8-0ac970f0a825f8-f373567-100200-1656b3cbf2bc8; _lxsdk=F0C76F40A77E11E8B64BAF79690B7FDA8B0D53718B9940698F7AC6687B56514D; _lxsdk_s=1656b3cbf44-510-e6c-766%7C%7C2'
}

def get_one_page(url):
    try:

        r=requests .get(url,headers =headers )
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except :
        print("异常！")

def print_one_page(html):
    pattern=re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                       +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                       +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
                         #re.S可以匹配换行符，必须加
    items=re.findall(pattern ,html)
    for item in items :
        yield {
            "index":item [0],
            "image":item [1],
            "title":item [2],
            "actor":item[3].strip() [3:],
            "time":item [4].strip() [5:],
            "score":item [5]+item [6]
        }

def write_to_file(content):
    with open("result.txt","a",encoding= "utf-8") as f:
        f.write(json.dumps(content,ensure_ascii= False   )+"\n")
        f.close()
        #1.字典转化文件，2.中文输出
def main(offset):
    url="http://maoyan.com/board/4?offset="+str(offset )
    html=get_one_page(url)
    print(html)
    for item in print_one_page(html ):
        print(item )
        write_to_file(item )
if __name__=="__main__":
    #for i in range(10):
     #    main(i*10)
    pool =Pool()
    pool.map(main,[i*10 for i in range(10)])