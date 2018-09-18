'''
改变id的计算方法
'''
import json
from pyspider .libs .utils import  md5string


from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
        'headers':{
            'User-Agent':'GoogleBot',
        }
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://movie.douban.com/subject/1292720/',fetch_type='js', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('div.article.list-wp a').items():
            print(each.attr.href)
            self.crawl(each.attr.href, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }

    def get_taskid(self, task):
        return md5string (task['url']+json.dumps(task['fetch'].get('data','')) )
