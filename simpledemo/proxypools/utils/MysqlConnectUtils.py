#!/usr/bin/python3
# encoding: utf-8

"""
@project = scrapydemo3
@file_name = MysqlConnectUtils.py
@author =  Hj
@datetime = 2022/4/25
"""

import pymysql


class MysqlConnectUtils():
    def __init__(self) -> None:
        super().__init__()
        self.conn=pymysql.connect(host='47.95.216.113', user='root', password='Hanjing123-=', database='houseDb')
        print("wfadsfa")

    def insert(self):
        # 连接数据库
        self.conn = pymysql.connect(host='47.95.216.113', user='root', password='Hanjing123-=', database='houseDb')

        # cursor=pymysql.cursors.DictCursor,是为了将数据作为一个字典返回
        cursor = self.cursor(cursor=pymysql.cursors.DictCursor)
        sql = 'select id,name from userinfo where id = %s'
        # 使用cursor()方法获取操作游标
        row = cursor.execute("SELECT VERSION()")

        # fetchall()（获取所有的数据），fetchmany(size)（size指定获取多少条数据），fetchone()（获取一条数据）
        result = cursor.fetchall()
        cursor.close()
        self.close()
        # 最后打印获取到的数据
        print(result)

    def inserttest(self, sql):
        # 连接数据库
        # cursor=pymysql.cursors.DictCursor,是为了将数据作为一个字典返回
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 使用cursor()方法获取操作游标
        cursor.execute(sql)
        self.conn.commit()
        cursor.close()
    def queryone(self, sql):
        # 连接数据库
        # cursor=pymysql.cursors.DictCursor,是为了将数据作为一个字典返回
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 使用cursor()方法获取操作游标
        cursor.execute(sql)
        result = cursor.fetchone()  # 获取
        cursor.close()
        return result
    def queryAll(self, sql):
        # 连接数据库
        # cursor=pymysql.cursors.DictCursor,是为了将数据作为一个字典返回
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 使用cursor()方法获取操作游标
        cursor.execute(sql)
        result = cursor.fetchall()  # 获取
        cursor.close()
        return result
    def close(self):
        self.conn.close()
