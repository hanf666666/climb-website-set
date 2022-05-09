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
    'Referer': 'https://www.xicidaili.com/nn/',
}
BASE_URL = 'https://www.xicidaili.com/nn/%d'


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
    html = respon.read().decode('utf-8')
    return html


def parsel(html):
    elem_obj = etree.HTML(html)
    elems = elem_obj.xpath('//table//tr[position()>1]')  # [position() <= 3]
    result = []
    for elem in elems:
        ip = elem.xpath('./td[2]/text()')[0]
        port = elem.xpath('./td[3]/text()')[0]
        result.append([ip, port])
    return result


if __name__ == '__main__':
    for i in range(1, 1001):
        html = crawl(BASE_URL % (i))
        datas = parsel(html)
        flag = write_csv('ip_port.csv', datas)
        if flag:
            print('第{}爬取成功'.format(i))
        else:
            print('爬取失败')
        if i % 10 == 0:
            time.sleep(10)