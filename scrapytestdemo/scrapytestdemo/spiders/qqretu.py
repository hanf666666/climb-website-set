import scrapy


class QqretuSpider(scrapy.Spider):
    """
    scrapy crawl qqretu --nolog
    """
    name = 'qqretu'
    allowed_domains = ['https://www.qqretu.com/gaoxiaoretu/']
    start_urls = ['https://www.qqretu.com/gaoxiaoretu/']

    def parse(self, response):
        # print(response.text)
        xpathList = response.xpath("/html/body/article/div/div[1]/section/div/ul/li")
        for row in xpathList:
            print("======="*11)
            print(row)

            print(row.xpath("./span/a/text()").extract()[0])



            # print(row.xpath("//a"))

        pass
