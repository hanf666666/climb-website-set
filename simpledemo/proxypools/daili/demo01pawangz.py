#!/usr/bin/python3
# encoding: utf-8

"""
@project = simpledemo
@file_name = pawangz.py
@author =  Hj
@datetime = 2022/5/4
"""
import time
import csv
from lxml import etree
from urllib import request, parse

Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'Referer': 'http://www.66ip.cn/',
}
BASE_URL = 'http://www.66ip.cn/'


# 文件路径,数据格式:[[1,2,3],[3,4,5],[5,4,6]]
def write_csv(filepath, datas):
    try:
        with open(filepath, 'a', encoding='utf-8', newline='') as wf:
            writer = csv.writer(wf)
            for data in datas:
                writer.writerow(data)
            return True
    except Exception as ex:
        return False


def crawl(url):
    req = request.Request(url=url, headers=Headers)
    respon = request.urlopen(req)
    html = respon.read().decode('gbk')
    return html


def parsel(html):
    # print(html)
    elem_obj = etree.HTML(html)
    elems = elem_obj.xpath('/html/body/div[2]/div[1]/table/')  # [position() <= 3]
    print(elems)
    result = []
    for elem in elems:
        ip = elem.xpath('//td[1]/text()')[0]
        print(ip)
    return result


if __name__ == '__main__':

        html = crawl(BASE_URL)
        print(html)
        datas = parsel(html)
        flag = write_csv('ip_port.csv', datas)

