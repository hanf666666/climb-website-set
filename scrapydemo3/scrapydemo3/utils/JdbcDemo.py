#!/usr/bin/python3
# encoding: utf-8

"""
@project = scrapydemo3
@file_name = JdbcDemo.py
@author =  Hj
@datetime = 2022/4/25
"""
from scrapydemo3.utils.MysqlConnectUtils import MysqlConnectUtils


def inserttest():
    pass


if __name__ == '__main__':
    # sql="insert into current_house value ('tSUObi15P_3bf4dU0LjR6Q','期房','大渡口区大滨中路9号14号楼1-8-4')"
    # MysqlConnectUtils().inserttest(sql)
    httpssql = "select ipport  from ippools i where status='0' and httptype='http' order by checkingCount desc ,updateDate desc;"
    proxy_https_dict = MysqlConnectUtils().queryAll(httpssql)
    proxy_https_list=[row['ipport'] for row in proxy_https_dict]
    print(proxy_https_list)
