#!/usr/bin/python3
# encoding: utf-8

"""
@project = scrapydemo3
@file_name = JdbcDemo.py
@author =  Hj
@datetime = 2022/4/25
"""
import datetime

from proxypools.utils.MysqlConnectUtils import MysqlConnectUtils




if __name__ == '__main__':

    sql=f"INSERT INTO housedb.ippools(ipport, httptype, anonymous, downloadDate, status, updateDate, checkingCount)\
                                      VALUES('{'fasdfa2'}', 'http', 'anonymous', '{datetime.datetime.now()}', '0', '{datetime.datetime.now()}', 0) \
        	on duplicate key update checkingCount = checkingCount+1,updateDate='{datetime.datetime.now()}',status={'1'};"
    MysqlConnectUtils().inserttest(sql)
    sql2=f"select * from housedb.ippools where ipport='{'fasdfa2'}'"
    queryone = MysqlConnectUtils().queryone(sql2)
    print(queryone)

