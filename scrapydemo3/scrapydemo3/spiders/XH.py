import scrapy

from scrapydemo3.items import PicItem
from scrapy.http import Request

class XhSpider(scrapy.Spider):
    # 爬虫名称，唯一
    name = "xh"
    # 允许访问的域
    allowed_domains = ["xiaohuar.com"]
    # 初始URL
    start_urls = ['http://www.xiaohuar.com/hua/']
    # 设置一个空集合
    url_set = set()

    def parse(self, response):
        # 如果图片地址以http://www.xiaohuar.com/list-开头，我才取其名字及地址信息
        if response.url.startswith("http://www.xiaohuar.com/list-"):
            allPics = response.xpath('//div[@class="img"]/a')
            for pic in allPics:
                # 分别处理每个图片，取出名称及地址
                item = PicItem()
                name = pic.xpath('./img/@alt').extract()[0]
                addr = pic.xpath('./img/@src').extract()[0]
                addr = 'http://www.xiaohuar.com' + addr
                item['name'] = name
                item['addr'] = addr
                # 返回爬取到的信息
                yield item
        # 获取所有的地址链接
        urls = response.xpath("//a/@href").extract()
        for url in urls:
            # 如果地址以http://www.xiaohuar.com/list-开头且不在集合中，则获取其信息
            if url.startswith("http://www.xiaohuar.com/list-"):
                if url in XhSpider.url_set:
                    pass
                else:
                    XhSpider.url_set.add(url)
                    # 回调函数默认为parse,也可以通过from scrapy.http import Request来指定回调函数
                    # from scrapy.http import Request
                    # Request(url,callback=self.parse)
                    print(f"将要跑的{url}")
                    yield Request(url, dont_filter=True)
            else:
                pass

