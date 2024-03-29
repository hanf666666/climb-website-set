import json
from datetime import datetime
from time import sleep

import scrapy
from scrapy import Request

from scrapydemo3.items import RoomDetailsItem

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
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        'Content-Type': 'application/json; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
    }
    data = {"siteid": "",
            "useType": "1",
            "areaType": "",
            "projectname": "",
            "entName": "",
            "location": "",
            "minrow": "1",
            "maxrow": "11"}
    parse_list = []
    pagecount = 0
    def start_requests(self):
        if not self.start_urls and hasattr(self, 'start_url'):
            raise AttributeError(
                "Crawling could not start: 'start_urls' not found "
                "or empty (but found 'start_url' attribute instead, "
                "did you miss an 's'?)")
        # 重写父类的方法start_urls
        for url in self.start_urls:
            # print("数据变动===>",self.data)
            # 直接发送get请求
            yield scrapy.Request(url=url, callback=self.parse1, body=json.dumps(self.data), method='POST',
                                 headers=self.headers, )

    def parse1(self, response):
        for i in range(1, 1200*10, 10):
        # for i in range(1, 1500*10, 10):
        # for i in range(1, 11, 10):
            self.data["minrow"] = i
            self.data["maxrow"] = i + 10
            print(f"正在爬取{int(i / 10)}页")
            metaInfo = {
                'crawlpage': int(i / 10)
            }
            yield scrapy.Request(url=self.start_urls[0], callback=self.parse2, body=json.dumps(self.data),
                                 method='POST', headers=self.headers,meta=metaInfo )


    def parse2(self, response):
        try:
            # print(type(response.text))
            # print(f"response.text==={response.text}")
            # print(json.loads(response.text))
            print(json.loads(response.text))
            print(f"response.meta.crawlpage====>正在爬取{response.meta['crawlpage']}页")
            self.pagecount = self.pagecount + 1
            print(f"总共 ====>总共爬取{self.pagecount}页")
            pageDataList = json.loads(response.text)["d"]

            for row in json.loads(pageDataList):
                # print(f"row===>{row}")
                projectname = row["projectname"]
                enterprisename = row["enterprisename"]
                blockname = row["blockname"]
                location = row["location"]
                getRoomJsonhttp = "http://www.cq315house.com/WebService/WebFormService.aspx/GetRoomJson"
                buildingids = row["buildingid"]
                for buildingid in buildingids.split(','):
                    getRoomJsonBody = {
                        "buildingid": buildingid
                    }
                    metaInfo={
                        'projectname': projectname,
                        'buildingid': buildingid,
                        'enterprisename': enterprisename,
                        'location': location,
                    }
                    yield scrapy.Request(url=getRoomJsonhttp, callback=self.parse_rooms, body=json.dumps(getRoomJsonBody),
                                         method='POST', headers=self.headers, meta=metaInfo)
        except:
            print(f"response.text======>{response.text}")

    def parse_rooms(self, response):
        """
        scrapy crawl house
        :param response:
        :return:
        """
        import json
        try:
            # print(f"response.text:{response.text}")
            roomsstr = json.loads(response.text)["d"]
            rooms_json = json.loads(roomsstr)
            print(f"response.meta.buildingid====>{response.meta['buildingid']}")
            print(f"response.meta.projectname====>{response.meta['projectname']}")
            print(f"parse_rooms====>{len(rooms_json)}个")
            projectname = response.meta['projectname']
            buildingid = response.meta['buildingid']
            enterprisename = response.meta['enterprisename']
            location = response.meta['location']
            # print(f"parse_rooms=====>{parse_rooms}")

            for json in rooms_json:
                # print(f"jsonjsonjsonjsonjson==>{type(json)}")
                # print(f"jsonjsonjsonjsonjson==>{json}")
                # print(f"jsonjsonjsonjsonjson==>{type(json['rooms'])}")
                for room in json['rooms']:
                    # print(f'{room["location"]}===>{room["flr"]} =>{room["rn"]}====>{room["tag"]}===>{room["nsjg"]}')
                    # print(f'{room["id"]}')
                    # print(f'{room["fjh"]}')
                    # print(f'{room["roomstatus"]}')
                    # print(f'room的相关信息{type(room)}')
                    # print(f'room的相关信息{room["id"]}')
                    roomDetailsItem = RoomDetailsItem()

                    # use":"成套住宅\
                    if room['use'] in ['成套住宅', '住宅']:
                        roomDetailsItem['projectname'] = projectname
                        roomDetailsItem['buildingid'] = buildingid
                        roomDetailsItem['enterprisename'] = enterprisename
                        roomDetailsItem['locationfu'] = location

                        # {'认购', '网签', '现房'}
                        # 唯一号
                        roomDetailsItem["fjh"] = room["fjh"]
                        roomDetailsItem["downloadDate"] = datetime.now()
                        roomDetailsItem["roomstatus"] = room["roomstatus"]
                        roomDetailsItem["use"] = room["use"]
                        roomDetailsItem["locationzi"] = room["location"]
                        roomDetailsItem["nsjg"] = room["nsjg"]

                        # print(f"=roomDetailsItem==>===================================={roomDetailsItem}")
                        # sleep(10)
                        yield roomDetailsItem
        except:
            print(f"response.text的数据:{response.text}")