# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class Scrapydemo3SpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn't have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

ualist = [
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
            'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
            'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'
        ]
proxy_http_list=[
   '58.220.95.44:10174',
    '58.20.184.187:9091'
]
proxy_https_list=[

]
class Scrapydemo3DownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s



    def process_request(self, request, spider):


        request.headers['User-Agent'] = random.choice(ualist)
        print(f"我是请求request==========={request}")
        print(f"我是请求request.body==========={request.body}")
        print(f"我是请求request.headers==========={request.headers}")
        print(f"我是请求request.url==========={request.url}")
        print(f"我是请求request.method==========={request.method}")
        # if request.method=='POST':
        #     if request.url.split(":")[0] == 'http':
        #         request.meta['proxy'] = 'http://{}'.format(random.choice(proxy_http_list))
        #         print(f"我是请求request proxy_http_list===>{request.meta['proxy']}")
            # else:
            #     request.meta['proxy'] = 'https://{}'.format(random.choice(proxy_https_list))
            #     print(f"我是请求request proxy_https_list===={request.meta['proxy']}")
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        if request.url.split(":")[0]=='http':
            request.meta['proxy'] = 'http://{}'.format(random.choice(proxy_http_list))
            print("proxy_http_list")
        # else:
        #     request.meta['proxy'] = 'https://{}'.format(random.choice(proxy_https_list))
        #     print("proxy_https_list")

        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
