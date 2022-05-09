#!/usr/bin/python3
# encoding: utf-8

"""
@project = untitled
@file_name = aa
@author =  Hj
@datetime = 2022/2/18 11:29
"""

import requests
from selenium import webdriver
from lxml import etree
import re
import time
import csv


class LagouSpider(object):
    """爬虫类"""
    def __init__(self):

        chrome_driver = r"D:\pyenv\untitled\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
        """初始化, 新建lagou_detail_position.csv文件（类excel文件)来保存数据"""
        self.driver = webdriver.Chrome(executable_path=chrome_driver)
        self.url = "file:///E:/%E8%B5%84%E6%96%99/%E7%9B%98%E5%8F%A4%E7%BE%8E%E5%A4%A9%E7%A7%91%E6%8A%80/20220215%E6%95%B0%E6%8D%AE%E8%BF%81%E7%A7%BB%E6%96%B9%E6%A1%88/20211007%E6%95%B0%E6%8D%AE%E8%BF%81%E7%A7%BB%E9%A1%B9%E7%9B%AE2.0%E7%89%88%E6%9C%AC[%E7%89%A9%E5%8C%96%E5%90%8C%E6%AD%A5%E6%96%B9%E6%A1%88%E6%AD%A3%E5%9C%A8%E4%BD%BF%E7%94%A8]/clickhouse%E5%AE%95%E6%9C%BA%E5%88%86%E6%9E%90/%E4%BA%91%E6%95%B0%E6%8D%AE%E5%BA%93ClickHouse.html"
        # # 新建excel文件，保存内容
        # headers = ['name', 'company_name', 'salary', 'city', 'work_years', 'education', 'desc']  # 列表
        # with open('lagou_detail_position.csv', 'w', newline='', encoding='utf-8') as fp:
        #     writer = csv.writer(fp)
        #     writer.writerow(headers)  # 写入头部

    def run(self):
        self.driver.get(self.url)
        time.sleep(5)
        source = self.driver.page_source
        # print(source)
        html = etree.HTML(source)
        # print(html)
        links = html.xpath("//span[@aria-haspopup='true']//text()")
        for row in links:
            print("*"*100)
            print(row)
        # now_number = self.driver.find_element_by_xpath("//div[@class='title']")
        # print(now_number.)



if __name__ == "__main__":
    LagouSpider().run()

