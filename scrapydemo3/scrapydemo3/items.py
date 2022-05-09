# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class Scrapydemo3Item(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass
class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
class PicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    addr = scrapy.Field()
    name = scrapy.Field()

class RoomDetailsItem(scrapy.Item):
    """
    房屋详细信息
    """
    projectname = scrapy.Field()
    buildingid=scrapy.Field()
    enterprisename = scrapy.Field()
    locationfu = scrapy.Field()

    fjh=scrapy.Field()
    downloadDate=scrapy.Field()
    roomstatus=scrapy.Field()
    use=scrapy.Field()
    locationzi=scrapy.Field()
    nsjg=scrapy.Field()
