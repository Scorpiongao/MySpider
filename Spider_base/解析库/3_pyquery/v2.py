import requests

from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'cookie':'_zap=4eec8bbb-20cb-4f69-9691-25cb072281ff; __utma=155987696.421456121.1521704982.1521704982.1521704982.1; __utmz=155987696.1521704982.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __DAYU_PP=eZEEFAr7eZAAvbFUZuFQ37118d08a955; d_c0="ALDl5omnBw6PTpeW2jt2dq6oEKZnJRyWMJ0=|1533811849"; q_c1=ed722b4c33f545eb8677c555b40ebc16|1533811851000|1517058531000; tgw_l7_route=860ecf76daf7b83f5a2f2dc22dccf049; _xsrf=366a2d3c3d4dd3e3614cffe6daac5ef4; l_n_c=1; l_cap_id="ZDJhMTE3OTA5YzU0NDUwOTg0NGE5OTdmMjk1MTRjOTM=|1535296077|814ecee200b54b36fa4a3a5956e4e2ccd363f682"; r_cap_id="OGU1NzQzYjI1OTkwNDFlMjhlOTZiNmFjM2M5ZjYyNTk=|1535296077|8280662ab9a6ee37adfda0c3e06a42e63a0736d3"; cap_id="YjhlZTFiMDZmMGEwNDg2ZDkyOTg3OTgwZTc1NGYwNGU=|1535296077|bbba3971e7be4cccee7102daaf828b1f4222e0a3"; n_c=1'
}

html = requests .get(url,headers =headers ).text
# print(html)

doc = pq (html)
items = doc('.explore-tab .feed-item').items()
for item in items :
    question = item ('h2').text()
    author = item ('.author-link-line').text()
    answer = pq(item ('.content').html() ).text()
    # print(question ,author ,answer )
    file = open('zhihu.txt','a',encoding= 'utf-8')
    file .write('\n'.join([question ,author ,answer ]) )
    file.write('\n'+ '='*50+'\n')
    file .close()