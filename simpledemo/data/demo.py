#!/usr/bin/python3
# encoding: utf-8

"""
@project = simpledemo
@file_name = demo.py
@author =  Hj
@datetime = 2022/6/12
"""


import numpy as np
import random
students=[]
STUDENT_NUM=0
class Student:
    def __init__(self,name):
        self.name=name
        self.walletMoney=0
        self.receivedRedPackets=[]
    def printInfo(self):
        print("姓名：{0}\n钱包余额：{1}\n收到的红包：{2}".format(self.name,self.walletMoney,self.receivedRedPackets))
    def receiveRed(self,money):
        self.walletMoney=self.walletMoney+money
        self.receivedRedPackets.append(money)
class LuckPacket:

    def __init__(self,totalMoney) -> None:
        super().__init__()
        self.totalMoney=totalMoney


    def distributeMoney(self):
        # 每个红包分一分钱，剩余的随机分到第一个红包
        redPackets = np.ones(self.redNum)
        remainM = self.totalMoney - self.redNum
        # 为每一个红包随机生成权重
        weights = np.random.randint(10, 100 + self.redNum, self.redNum)
        distrib = weights / weights.sum()
        distrib = distrib * remainM  # 为每一个红包生成额度
        distrib = np.floor(distrib)  # 去掉小数
        redPackets = redPackets + distrib  # 加进红包
        remainM = self.totalMoney - int(redPackets.sum())  # 剩余额度， reaminM值应不超过红包数redNum
        # 接下来是如何

if __name__ == '__main__':
    count=100
    fenfa = LuckPacket(count)

