#!/usr/bin/python3
# encoding: utf-8

"""
@project = scrapydemo3
@file_name = StrToJson.py
@author =  Hj
@datetime = 2022/4/24
"""
import json

# 大体信息
buidingjson={
  "d": "{\"enterpriseName\":\"重庆盛毓锦鑫房地产开发有限公司\",\"enterpriseOrgCode\":\"\",\"enterpriseDelegate\":\"\",\"projectName\":\"华宇锦绣玺岸大渡口组团H分区H06-4-1、H06-4-5、H06-5号地块（一期A区）\",\"location\":\"大渡口区大渡口组团H分区H06-4-1、H06-5地块\",\"presaleCert\":\"渝住建委（2022）预字第（223）号\"}"
}
loads = json.loads(buidingjson["d"])
# loads = json.loads(buidingjson["d"])
# print(loads)


# 房屋状态信息
statusJson={"d":"[{\"val\":8,\"name\":\"已售\",\"ab\":\"已售\",\"bgColor\":\"#ff00ff\",\"ftColor\":\"#000000\",\"priority\":1,\"type\":1,\"alarmType\":1,\"showType\":0,\"parentType\":0,\"treeLevel\":0},{\"val\":64,\"name\":\"不可售\",\"ab\":\"不可售\",\"bgColor\":\"#ffff00\",\"ftColor\":\"#000000\",\"priority\":2,\"type\":0,\"alarmType\":1,\"showType\":0,\"parentType\":0,\"treeLevel\":0},{\"val\":256,\"name\":\"不可售\",\"ab\":\"不可售\",\"bgColor\":\"#ffff00\",\"ftColor\":\"#000000\",\"priority\":3,\"type\":1,\"alarmType\":1,\"showType\":0,\"parentType\":0,\"treeLevel\":0},{\"val\":1024,\"name\":\"不可售\",\"ab\":\"不可售\",\"bgColor\":\"#ffff00\",\"ftColor\":\"#000000\",\"priority\":4,\"type\":1,\"alarmType\":1,\"showType\":0,\"parentType\":0,\"treeLevel\":0},{\"val\":2048,\"name\":\"已售\",\"ab\":\"已售\",\"bgColor\":\"#ff00ff\",\"ftColor\":\"#000000\",\"priority\":5,\"type\":1,\"alarmType\":1,\"showType\":0,\"parentType\":0,\"treeLevel\":0},{\"val\":16777216,\"name\":\"已售\",\"ab\":\"已售\",\"bgColor\":\"#ff00ff\",\"ftColor\":\"#000000\",\"priority\":5,\"type\":1,\"alarmType\":1,\"showType\":0,\"parentType\":0,\"treeLevel\":0},{\"val\":131072,\"name\":\"不可售\",\"ab\":\"不可售\",\"bgColor\":\"#ffff00\",\"ftColor\":\"#000000\",\"priority\":6,\"type\":1,\"alarmType\":1,\"showType\":0,\"parentType\":0,\"treeLevel\":0},{\"val\":262146,\"name\":\"未售\",\"ab\":\"可售\",\"bgColor\":\"#00ff00\",\"ftColor\":\"#000000\",\"priority\":7,\"type\":1,\"alarmType\":1,\"showType\":0,\"parentType\":0,\"treeLevel\":0},{\"val\":262150,\"name\":\"未售\",\"ab\":\"可售\",\"bgColor\":\"#00ff00\",\"ftColor\":\"#000000\",\"priority\":8,\"type\":1,\"alarmType\":1,\"showType\":0,\"parentType\":0,\"treeLevel\":0},{\"val\":524292,\"name\":\"未售\",\"ab\":\"可售\",\"bgColor\":\"#00ff00\",\"ftColor\":\"#000000\",\"priority\":10,\"type\":1,\"alarmType\":1,\"showType\":0,\"parentType\":0,\"treeLevel\":0},{\"val\":655364,\"name\":\"不可售\",\"ab\":\"不可售\",\"bgColor\":\"#ffff00\",\"ftColor\":\"#000000\",\"priority\":11,\"type\":1,\"alarmType\":1,\"showType\":0,\"parentType\":0,\"treeLevel\":0},{\"val\":2097152,\"name\":\"已售\",\"ab\":\"已售\",\"bgColor\":\"#ff00ff\",\"ftColor\":\"#000000\",\"priority\":12,\"type\":1,\"alarmType\":1,\"showType\":0,\"parentType\":0,\"treeLevel\":0},{\"val\":2621444,\"name\":\"已售\",\"ab\":\"已售\",\"bgColor\":\"#ff00ff\",\"ftColor\":\"#000000\",\"priority\":13,\"type\":1,\"alarmType\":1,\"showType\":0,\"parentType\":0,\"treeLevel\":0},{\"val\":20176833,\"name\":\"不可售\",\"ab\":\"不可售\",\"bgColor\":\"#ffff00\",\"ftColor\":\"#000000\",\"priority\":14,\"type\":1,\"alarmType\":1,\"showType\":0,\"parentType\":0,\"treeLevel\":0},{\"val\":17301508,\"name\":\"已售\",\"ab\":\"已售\",\"bgColor\":\"#ff00ff\",\"ftColor\":\"#000000\",\"priority\":15,\"type\":1,\"alarmType\":1,\"showType\":0,\"parentType\":0,\"treeLevel\":0},{\"val\":393219,\"name\":\"不可售\",\"ab\":\"不可售\",\"bgColor\":\"#ffff00\",\"ftColor\":\"#000000\",\"priority\":16,\"type\":1,\"alarmType\":1,\"showType\":0,\"parentType\":0,\"treeLevel\":0}]"}
# print(statusJson["d"])
loads = json.loads(str(statusJson["d"]))
valList=[]

for json in loads:
    # print(json['ab'])
    print(json)
    valList.append(json['val'])
    pass
print(valList)
print(8*64)


