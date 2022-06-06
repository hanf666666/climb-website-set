#!/usr/bin/python3
# encoding: utf-8

"""
@project = simpledemo
@file_name = 89ip.py
@author =  Hj
@datetime = 2022/5/4
"""
# 建立属于自己的开放代理IP池
import datetime

import requests
import random
import time
from lxml import etree
from fake_useragent import UserAgent

from proxypools.utils.MysqlConnectUtils import MysqlConnectUtils


class IpPool:
    def __init__(self):
        # 测试ip是否可用url
        self.test_url = 'http://httpbin.org/get'
        self.headers = {'User-Agent': UserAgent(path="D:/pyspace/hanpyspace/climb-website-set/simpledemo/data/fakeuseragent.json").random}
        print(self.headers)

    def test_http_proxy(self, proxy):
        '''测试代理IP是否可用'''
        proxies = {
            'http': 'http://{}'.format(proxy),
            # 'https': 'https://{}'.format(proxy),
        }
        # 参数类型
        # proxies
        # proxies = {'协议': '协议://IP:端口号'}
        # timeout 超时设置 网页响应时间3秒 超过时间会抛出异常
        try:
            resp = requests.get(url=self.test_url, proxies=proxies, headers=self.headers, timeout=3)
            # 获取 状态码为200
            if resp.status_code == 200:
                print('"http://{}'.format(proxy) + '",')
                # print(proxy, '\033[31m可用\033[0m')
                sql = f"INSERT INTO housedb.ippools(ipport, httptype, anonymous, downloadDate, status, updateDate, checkingCount)\
                                                                                  VALUES('{proxy}', 'http' ,'不知', '{datetime.datetime.now()}', '0', '{datetime.datetime.now()}', 0) \
                                                    	on duplicate key update checkingCount = checkingCount+1,updateDate='{datetime.datetime.now()}',status={'0'};"
                print(sql)
                MysqlConnectUtils().inserttest(sql)

            else:
                sql = f"INSERT INTO housedb.ippools(ipport, httptype, anonymous, downloadDate, status, updateDate, checkingCount)\
                                                                                        VALUES('{proxy}', 'http' ,'不知', '{datetime.datetime.now()}', '0', '{datetime.datetime.now()}', 0) \
                                                          	on duplicate key update checkingCount = checkingCount+1,updateDate='{datetime.datetime.now()}',status='1';"
                print(sql)
                MysqlConnectUtils().inserttest(sql)
                pass

        except Exception as e:
            sql = f"INSERT INTO housedb.ippools(ipport, httptype, anonymous, downloadDate, status, updateDate, checkingCount)\
                                                                                           VALUES('{proxy}', 'http' ,'不知', '{datetime.datetime.now()}', '0', '{datetime.datetime.now()}', 0) \
                                                             	on duplicate key update checkingCount = checkingCount+1,updateDate='{datetime.datetime.now()}',status='1';"
            print(sql)
            MysqlConnectUtils().inserttest(sql)
            print(proxy, '不可用')
            pass

    def test_https_proxy(self, proxy):
        '''测试代理IP是否可用'''
        proxies = {
            'http': 'http://{}'.format(proxy),
            # 'https': 'https://{}'.format(proxy),
        }
        # 参数类型
        # proxies
        # proxies = {'协议': '协议://IP:端口号'}
        # timeout 超时设置 网页响应时间3秒 超过时间会抛出异常
        try:
            resp = requests.get(url=self.test_url, proxies=proxies, headers=self.headers, timeout=3)
            # 获取 状态码为200
            if resp.status_code == 200:
                print('"https://{}'.format(proxy) + '",')
                # print(proxy, '\033[31m可用\033[0m')
                sql = f"INSERT INTO housedb.ippools(ipport, httptype, anonymous, downloadDate, status, updateDate, checkingCount)\
                                                        VALUES('{proxy}', 'https', '不知anonymous', '{datetime.datetime.now()}', '0', '{datetime.datetime.now()}', 0) \
                            on duplicate key update checkingCount = checkingCount+1,updateDate='{datetime.datetime.now()}',status={'0'};"
                MysqlConnectUtils().inserttest(sql)

            else:
                # print(proxy, '不可用')
                sql = f"INSERT INTO housedb.ippools(ipport, httptype, anonymous, downloadDate, status, updateDate, checkingCount)\
                                                                  VALUES('{proxy}', 'https', '不知anonymous', '{datetime.datetime.now()}', '0', '{datetime.datetime.now()}', 0) \
                                      on duplicate key update checkingCount = checkingCount+1,updateDate='{datetime.datetime.now()}',status={'1'};"
                MysqlConnectUtils().inserttest(sql)
                pass

        except Exception as e:
            # print(proxy, '不可用')
            sql = f"INSERT INTO housedb.ippools(ipport, httptype, anonymous, downloadDate, status, updateDate, checkingCount)\
                                                                            VALUES('{proxy}', 'https', '不知anonymous', '{datetime.datetime.now()}', '0', '{datetime.datetime.now()}', 0) \
                                                on duplicate key update checkingCount = checkingCount+1,updateDate='{datetime.datetime.now()}',status={'1'};"
            MysqlConnectUtils().inserttest(sql)
            pass


if __name__ == '__main__':
    ip = IpPool()
    sql2=f"select ipport,httptype from housedb.ippools where httptype='https'"
    queryAllList = MysqlConnectUtils().queryAll(sql2)
    for ipport in queryAllList:
        print(ipport['ipport'])
        ip.test_https_proxy(ipport['ipport'])
