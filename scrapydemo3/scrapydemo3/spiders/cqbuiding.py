import scrapy

"""
scrapy crawl cqbuiding
"""
class CqbuidingSpider(scrapy.Spider):
    name = 'cqbuiding'
    allowed_domains = ['ghzrzyj.cq.gov.cn']
    start_urls = ['http://ghzrzyj.cq.gov.cn/']


    def parse(self, response):
        # 方法2,设置页面的编码
        # response.encoding = response.apparent_encoding
        # resp2 = response.text

        with open(file="aaaa.html", mode='w', encoding='utf-8') as f:
            f.write(response.text)
        xpath = response.xpath("/html/body/div/div[2]/div[4]/a[2]/span")
        print(f"xpath==Selector===={xpath}")
        print(f"xpath.extract()==获得一个list===={xpath.extract()}")
        print(f"xpath.extract()[0]==获得一个list的元素===={xpath.extract()[0]}")
        print("===========text()=================="*2)

        textxpath = response.xpath("/html/body/div/div[2]/div[4]/a[2]/span/text()")
        print(f"textxpath==Selector===={textxpath}")
        print(f"textxpath.extract()==获得一个list===={textxpath.extract()}")
        print(f"textxpath.extract()[0]==获得一个list的元素===={textxpath.extract()[0]}")

        print("===========@()==================" * 2)
        hrefxpath = response.xpath("/html/body/div/div[2]/div[4]/a[2]/@href")
        print(f"hrefxpath==Selector===={hrefxpath}")
        print(f"hrefxpath.extract()==获得一个list===={hrefxpath.extract()}")
        print(f"hrefxpath.extract()[0]==获得一个list的元素===={hrefxpath.extract()[0]}")

        print("===========动态数据无法抓取()==================" * 2)
        hrefxpath = response.xpath('//*[@id="gwyinfo"]/li[1]/a')
        print(f"动态数据==Selector===={hrefxpath}")
        print(f"动态数据.extract()==获得一个list===={hrefxpath.extract()}")
        print(f"动态数据.extract()[0]==获得一个list的元素===={hrefxpath.extract()[0]}")



