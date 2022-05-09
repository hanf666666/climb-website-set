#!/usr/bin/python3
# encoding: utf-8

"""
@project = simpledemo
@file_name = kuaidaili.py
@author =  Hj
@datetime = 2022/5/4
"""
# 建立属于自己的开放代理IP池
import requests
import random
import time
from lxml import etree
from fake_useragent import UserAgent


class IpPool:
    def __init__(self):
        # 测试ip是否可用url
        self.test_url = 'http://httpbin.org/get'
        # 获取IP的 目标url
        self.url = 'https://www.kuaidaili.com/free/inha/1/'
        self.headers = {'User-Agent': UserAgent().random}

    def get_html(self, url):
        '''获取页面'''
        html = requests.get(url=url, headers=self.headers).text

        return html

    def get_proxy(self, url):
        '''数据处理  获取ip 和端口'''
        html = self.get_html(url=url)
        # print(html)

        elemt = etree.HTML(html)

        ips_list = elemt.xpath('//table/tbody/tr/td[1]/text()')
        ports_list = elemt.xpath('//table/tbody/tr/td[2]/text()')

        for ip, port in zip(ips_list, ports_list):
            # 拼接ip与port
            proxy = ip.strip() + ":" + port.strip()
            # print(proxy)

            # 175.44.109.195:9999
            self.test_proxy(proxy)

    def test_proxy(self, proxy):
        '''测试代理IP是否可用'''
        proxies = {
            'http': 'http://{}'.format(proxy),
            'https': 'https://{}'.format(proxy),
        }
        # 参数类型
        # proxies
        # proxies = {'协议': '协议://IP:端口号'}
        # timeout 超时设置 网页响应时间3秒 超过时间会抛出异常
        try:
            resp = requests.get(url=self.test_url, proxies=proxies, headers=self.headers, timeout=3)
            # 获取 状态码为200
            if resp.status_code == 200:
                print('"http://{}'.format(proxy)+'",')
                # print(proxy, '\033[31m可用\033[0m')
                # 可以的IP 写入文本以便后续使用
                self.file.write(proxy)

            else:
                # print(proxy, '不可用')
                pass

        except Exception as e:
            # print(proxy, '不可用')
            pass

    def crawl(self):
        '''执行函数'''
        # 快代理每页url 的区别
        # https://www.kuaidaili.com/free/inha/1/
        # https://www.kuaidaili.com/free/inha/2/
        # .......
        # 提供的免费ip太多
        # 这里只获取前100页提供的免费代理IP测试
        for i in range(1, 101):
            # 拼接完整的url
            page_url = self.url.format(i)
            # 注意抓取控制频率
            time.sleep(random.randint(1, 4))
            self.get_proxy(url=page_url)

        # 执行完毕关闭文本
        self.file.close()


if __name__ == '__main__':
    ip = IpPool()
    ip.crawl()
