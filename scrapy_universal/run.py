'''
入口文件，根目录下，作用：启动spider
'''

import sys
from scrapy .utils .project import  get_project_settings
from scrapy_universal .utils import  get_config
from scrapy .crawler import  CrawlerProcess

def run():
    #获取命令行的参数并赋值给name ,name就是Json文件名，也就是要爬取的目标网站的名称
    name = sys.argv [1]
    cuttom_settings = get_config(name)

    #爬取使用的Spider名称
    spider = cuttom_settings .get('spider','universal')
    project_settings = get_project_settings()
    settings = dict(project_settings .copy() )

    #合并配置
    settings.update(cuttom_settings .get('settings'))
    process = CrawlerProcess (settings )

    #启动爬虫
    process .crawl(spider,**{'name':name})
    process .start()

if __name__ == '__main__':
    run()

