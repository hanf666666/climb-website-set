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

        headers = {
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
        }
        return scrapy.Request(url='http://47.95.216.113:8888/getIpAddr', callback=self.parse2,  method='GET',
                             headers=headers, )
    def parse2(self, response):
            print(f"parse2 response.text:{response.text}")


