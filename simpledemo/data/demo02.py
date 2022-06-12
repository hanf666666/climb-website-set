#!/usr/bin/python3
# encoding: utf-8

"""
@project = simpledemo
@file_name = demo02.py
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
    """红包对象"""
    def __init__(self,redNum,totalMoney) -> None:
        super().__init__()
        # 红包数量
        self.redNum=redNum
        # 红包的金额
        self.totalMoney=totalMoney*100
        self.stuDict={}
        self.walletMoney=1

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
        # 接下来是如何随机的把remainM分给每个红包。

        idxSort = weights.argsort()  # 得到weights 排序的索引,argsort函数返回的是数组值从小到大的索引值
        idxSort = idxSort[::-1]  # 步长为-1，切片
        for i in range(remainM):  # 把剩余的钱分到权重较大的remainM个红包
            redPackets[idxSort[i]] += 1
        # 把已分好的红包随机分到同学
        self.distributeToStudents(redPackets)


    def distributeToStudents(self, redPacket):
        selectStu = random.sample(students, self.redNum)
        for i in range(len(selectStu)):
            selectStu[i].receiveRed(redPacket[i])
            self.stuDict[selectStu[i]] = redPacket[i]

    def printRedDistribution(self):
            print("看看大家的运气：")
            for k, v in self.stuDict.items():
                # print("{:<6}{:>12.2f}元".format(k.name, v / 100))
                print("{:<6}{:>12.2f}元".format(k.name, v / 100))
    def printLuckKing(self):
        # (学生对象,得到的最大金额)
        luckKing=(0,0)
        for item in self.stuDict.items():
            # print(item[1])
            if item[1]>luckKing[1]:
                luckKing=item
        print("*"*80)
        # print(luckKing)
        print("运气王是%s,得到的额度是%10.2f元"%(luckKing[0].name,luckKing[1]/ 100))



# class CommonPacket:
#     """普通红包"""
#     def __init__(self,redNum,singleMoney):
#      self.redNum=redNum
#      self.singleMoney=int(singleMoney*100)
#      self.stuDict={}
#     def distributeMoney(self):
#         selectStu=random.sample(students,self.redNum)
#         for i in range(len(selectStu)):
#             selectStu[i].receiveRed(self.singleMoney)
#             self.stuDict[selectStu[i]]=self.singleMoney
#     def printRedDistribution(self):
#         print("看看大家的运气：")
#         for k,v in self.items():
#             print("{:<6}{:>12.2f}元".format(k.name,v/100))


def initData():
        global students
        global STUDENT_NUM
        #dataFile="D:\实训\实验6 Python第三方库numpy调用\python7班.csv"
        # names=np.loadtxt(r"D:\实训\实验6 Python第三方库numpy调用\python7班.csv",encoding="utf-8",delimiter=",",skiprows=1,usecols=(2,),dtype=str)
        # for name in names:
        students.append(Student("han1"))
        students.append(Student("han2"))
        students.append(Student("han3"))
        STUDENT_NUM=len(students)
def printWallets():
    lis=sorted(students,key=lambda x:x.walletMoney,reverse=True)
    for i in lis:
        students.append(Student(i))
        STUDENT_NUM=len(students)


if __name__=="__main__":
    initData()
    count=0
    while count<1:
        count=count+1
        # htype=int(input("请输入功能选择(1.拼手气红包，2.普通红包，0.退出，9.打印每位同学的红包金额)"))
        htype=1
        if htype==0:
            exit()
        elif htype==1:
            # redNum=int(input("请输入红包数量："))
            redNum=3
            # money=float(input("请输入发放总金额（元）："))
            money=20
            if int(money*100)<redNum:
                print("红包金额不够分，至少要保证每个红包有0.01元，请重新输入！")
            luckP=LuckPacket(redNum,money)
            luckP.distributeMoney()
            luckP.printRedDistribution()
            luckP.printLuckKing()
        elif htype==2:
            redNum=int(input("Q请输入红包数量："))
            money=float(input("请输入单个红包的金额（元）："))
            # commonP=CommonPacket(redNum,money)
            # commonP.distributeMoney()
            # commonP.printRedDistribution()
        #elif htype==9: