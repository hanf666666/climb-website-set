import scrapy

"""

scrapy genspider SelfDemoSpider SelfDemoSpider

scrapy crawl SelfDemo2
scrapy crawl SelfDemo2 --nolog
Abc_JwtToken_Demo
"""
class Selfdemo2Spider(scrapy.Spider):
    name = 'SelfDemo2'
    allowed_domains = ['47.95.216.113:8888']
    start_urls = ['http://47.95.216.113:8888/getIpAddr']

    def parse(self, response):
        print(response.text)
        pass
