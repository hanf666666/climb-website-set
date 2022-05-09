import scrapy

"""

scrapy genspider SelfDemoSpider SelfDemoSpider

scrapy crawl selfdemo
scrapy crawl selfdemo --nolog
Abc_JwtToken_Demo
"""
class SelfDemoSpider(scrapy.Spider):
    name = 'selfdemo'
    allowed_domains = ['localhost']
    start_urls = ['http://47.95.216.113:8888/login2']
    # http://47.95.216.113:8888/getIpAddr
    def start_requests(self):
        if not self.start_urls and hasattr(self, 'start_url'):
            raise AttributeError(
                "Crawling could not start: 'start_urls' not found "
                "or empty (but found 'start_url' attribute instead, "
                "did you miss an 's'?)")
        # for url in self.start_urls:
        #     yield Request(url, dont_filter=True)

        data = {"name": "韩静",
                "password": "123xyz",
              }

        # 重写父类的方法start_urls
        for url in self.start_urls:
            # 直接发送get请求
            yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse)
    def parse(self, response):
        print(f"parse response.text:{response.text}")
        data = {"name": "韩静2",
                "password": "123xyz",
                }
        yield scrapy.Request(url='http://47.95.216.113:8888/getIpAddr', callback=self.parse2)
        # yield scrapy.FormRequest(url=self.start_urls[0], formdata=data, callback=self.parse)
    def parse2(self, response):
            print(f"parse2 response.text:{response.text}")
            data = {"name": "韩静2",
                    "password": "123xyz",
                    }
            # yield scrapy.Request(url='http://47.95.216.113:8888/getIpAddr', callback=self.parse2)
            # yield scrapy.FormRequest(url=self.start_urls[0], formdata=data, callback=self.parse)

