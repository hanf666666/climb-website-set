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
        self.url = "http://127.0.0.1:8020/gd_html1124/index.html"
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
        links = html.xpath("//div[@class='title']//text()")
        print(links)
        # now_number = self.driver.find_element_by_xpath("//div[@class='title']")
        # print(now_number.)



if __name__ == "__main__":
    LagouSpider().run()

