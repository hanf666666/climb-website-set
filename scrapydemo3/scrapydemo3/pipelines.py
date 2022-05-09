# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapydemo3.utils.MysqlConnectUtils import MysqlConnectUtils


class Scrapydemo3Pipeline:
    def open_spider(self, spider):
        print("开启")
        self.utils = MysqlConnectUtils()
    def process_item(self, item, spider):
        """
        scrapy crawl house
        :param item:
        :param spider:
        :return:
        """
        if item.__class__.__name__=="RoomDetailsItem":
            # print(f"item.__class__.__name__===>{item.__class__.__name__}")

            sql = f"INSERT INTO housedb.current_house  \
            (projectname, buildingid, enterprisename, locationfu,fjh, downloadDate, roomstatus, `use`, locationzi, nsjg) \
            VALUES('{item['projectname']}', '{item['buildingid']}', '{item['enterprisename']}', '{item['locationfu']}', '{item['fjh']}', '{item['downloadDate']}', '{item['roomstatus']}', '{item['use']}', '{item['locationzi']}', '{item['nsjg']}'); "
            # print(sql)
            self.utils.inserttest(sql)

        return item


    def close_spider(self,spider):
        print("关闭")
        self.utils.close()
        pass
