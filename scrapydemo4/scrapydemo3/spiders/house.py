import json

import scrapy


"""

scrapy genspider xh xiaohuar.com

scrapy crawl house
scrapy crawl house --nolog
"""
class HouseSpider(scrapy.Spider):

    name = 'house'
    allowed_domains = ['www.cq315house.com']

    start_urls = ['http://www.cq315house.com/WebService/WebFormService.aspx/getParamDatas2']
    headers = {
        'method': 'POST',
        'accept': '*/*',
        'content-type': 'application/json',
        'origin': 'http://www.cq315house.com',
        'referer': 'http://www.cq315house.com/HtmlPage/PresaleDetail.html',
        # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    }

    def parse(self, response):
        print(f"response======={response.text}")
        print("")
        print("")
        print("")
        data = {
            "siteid":"",
            "useType":"",
            "areaType":"",
            "projectname":"",
            "entName":"",
            "location":"",
            "minrow":"1",
            "maxrow":"11"

          }
        yield scrapy.Request(url=self.start_urls[0], body=json.dumps(data), method='POST',headers=self.headers )




