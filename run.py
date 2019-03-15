import sys
from scrapy.utils.project import get_project_settings
from scrapyuniversal.spiders.universal import UniversalSpider
from scrapyuniversal.utils import get_config
from scrapy.crawler import CrawlerProcess

def run():
    name = sys.argv[1]
    custom_settings = get_config(name)  # 爬虫spider的名称
    spider = custom_settings.get('spider', 'universal')
    project_settings = get_project_settings()
    setting = dict(project_settings.copy()) # 合并配置
    setting.update(custom_settings.get('setting'))
    process = CrawlerProcess(setting)
    process.crawl(spider, **{'name': name})
    process.start() # 启动爬虫

if __name__ == '__main__':
    run()

