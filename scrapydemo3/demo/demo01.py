#!/usr/bin/python3
# encoding: utf-8

"""
@project = scrapydemo3
@file_name = demo01.py
@author =  Hj
@datetime = 2022/4/24
"""
from datetime import datetime

# for i in range(1, 1000,10):
#    print(i)
#    print(i+10)
print(datetime.now())



datajson=  "[{\"id\":611,\"systemType\":\"roadSide\",\"resourceName\":\"首页\",\"resourceType\":\"mod\",\"visitUrl\":\"homePage\",\"sort\":1,\"icon\":\"icon_ccgl\",\"resourceVoList\":[]},{\"id\":442,\"systemType\":\"roadSide\",\"resourceName\":\"实时监控\",\"resourceType\":\"mod\",\"visitUrl\":\"realTimeMonitor\",\"sort\":2,\"icon\":\"icon_shouy\",\"resourceVoList\":[{\"id\":164,\"systemType\":\"roadSide\",\"resourceName\":\"地图监控\",\"resourceType\":\"menu\",\"visitUrl\":\"monitor/mapMonitor/parkList\",\"sort\":1,\"parentId\":442,\"resourceVoList\":[]}]},{\"id\":613,\"systemType\":\"roadSide\",\"resourceName\":\"运营监管\",\"resourceType\":\"mod\",\"visitUrl\":\"operateSupervision\",\"sort\":3,\"icon\":\"icon_ccgl\",\"resourceVoList\":[{\"id\":497,\"systemType\":\"roadSide\",\"resourceName\":\"预警数据审核\",\"resourceType\":\"menu\",\"visitUrl\":\"parkOrder/abnormal/info\",\"sort\":1,\"parentId\":613,\"resourceVoList\":[]}]},{\"id\":489,\"systemType\":\"roadSide\",\"resourceName\":\"停车数据\",\"resourceType\":\"mod\",\"visitUrl\":\"parkCarManage\",\"sort\":4,\"icon\":\"icon_parkmanage\",\"resourceVoList\":[{\"id\":490,\"systemType\":\"roadSide\",\"resourceName\":\"停车记录\",\"resourceType\":\"menu\",\"visitUrl\":\"parkCarManage/parkRecord/page\",\"sort\":1,\"parentId\":489,\"resourceVoList\":[]},{\"id\":494,\"systemType\":\"roadSide\",\"resourceName\":\"欠费车辆\",\"resourceType\":\"menu\",\"visitUrl\":\"parkOrder/arrears/page\",\"sort\":2,\"parentId\":489,\"resourceVoList\":[]},{\"id\":504,\"systemType\":\"roadSide\",\"resourceName\":\"超长停车\",\"resourceType\":\"menu\",\"visitUrl\":\"parkOrder/timeOut/page\",\"sort\":4,\"parentId\":489,\"resourceVoList\":[]},{\"id\":508,\"systemType\":\"roadSide\",\"resourceName\":\"无效记录\",\"resourceType\":\"menu\",\"visitUrl\":\"parkCarManage/cancelledRecord/page\",\"sort\":5,\"parentId\":489,\"resourceVoList\":[]}]},{\"id\":7,\"systemType\":\"roadSide\",\"resourceName\":\"交易流水\",\"resourceType\":\"mod\",\"visitUrl\":\"parkOrder\",\"sort\":5,\"icon\":\"icon_ddgl\",\"resourceVoList\":[{\"id\":8,\"systemType\":\"roadSide\",\"resourceName\":\"临停交易流水\",\"resourceType\":\"menu\",\"visitUrl\":\"parkOrder/trade/payPage\",\"sort\":1,\"parentId\":7,\"resourceVoList\":[]},{\"id\":11,\"systemType\":\"roadSide\",\"resourceName\":\"长租交易流水\",\"resourceType\":\"menu\",\"visitUrl\":\"parkOrder/longRent/page\",\"sort\":2,\"parentId\":7,\"resourceVoList\":[]}]},{\"id\":17,\"systemType\":\"roadSide\",\"resourceName\":\"长租车辆\",\"resourceType\":\"mod\",\"visitUrl\":\"longRentManager\",\"sort\":6,\"icon\":\"icon_czgl\",\"resourceVoList\":[{\"id\":19,\"systemType\":\"roadSide\",\"resourceName\":\"长租用户\",\"resourceType\":\"menu\",\"visitUrl\":\"longRentManager/park/page\",\"sort\":1,\"parentId\":17,\"resourceVoList\":[]},{\"id\":20,\"systemType\":\"roadSide\",\"resourceName\":\"白名单车辆\",\"resourceType\":\"menu\",\"visitUrl\":\"longRentManager/whiteList/list\",\"sort\":2,\"parentId\":17,\"resourceVoList\":[]}]},{\"id\":615,\"systemType\":\"roadSide\",\"resourceName\":\"停车资源\",\"resourceType\":\"mod\",\"visitUrl\":\"parkResource\",\"sort\":7,\"icon\":\"icon_tczy\",\"resourceVoList\":[{\"id\":13,\"systemType\":\"roadSide\",\"resourceName\":\"车场管理\",\"resourceType\":\"menu\",\"visitUrl\":\"parkManager/park/page\",\"sort\":1,\"parentId\":615,\"resourceVoList\":[]},{\"id\":14,\"systemType\":\"roadSide\",\"resourceName\":\"车位详情\",\"resourceType\":\"menu\",\"visitUrl\":\"parkManager/parkItem/page\",\"sort\":2,\"parentId\":615,\"resourceVoList\":[]}]},{\"id\":15,\"systemType\":\"roadSide\",\"resourceName\":\"设备管理\",\"resourceType\":\"mod\",\"visitUrl\":\"equipments\",\"sort\":8,\"icon\":\"icon_sbgl\",\"resourceVoList\":[{\"id\":443,\"systemType\":\"roadSide\",\"resourceName\":\"地磁检测器\",\"resourceType\":\"menu\",\"visitUrl\":\"equipment/geomagnetic/getRegistered\",\"sort\":1,\"parentId\":15,\"resourceVoList\":[]},{\"id\":444,\"systemType\":\"roadSide\",\"resourceName\":\"车位管理相机\",\"resourceType\":\"menu\",\"visitUrl\":\"equipment/highVideo/getRegistered\",\"sort\":2,\"parentId\":15,\"resourceVoList\":[]},{\"id\":445,\"systemType\":\"roadSide\",\"resourceName\":\"低位视频桩\",\"resourceType\":\"menu\",\"visitUrl\":\"equipment/video/getRegistered\",\"sort\":3,\"parentId\":15,\"resourceVoList\":[]},{\"id\":163,\"systemType\":\"roadSide\",\"resourceName\":\"智能车位锁\",\"resourceType\":\"menu\",\"visitUrl\":\"equipment/roadLock/bindPage\",\"sort\":4,\"parentId\":15,\"resourceVoList\":[]},{\"id\":165,\"systemType\":\"roadSide\",\"resourceName\":\"泊位巡查车\",\"resourceType\":\"menu\",\"visitUrl\":\"equipment/manage/patrolCarList\",\"sort\":5,\"parentId\":15,\"resourceVoList\":[]},{\"id\":446,\"systemType\":\"roadSide\",\"resourceName\":\"城市诱导屏\",\"resourceType\":\"menu\",\"visitUrl\":\"equipment/manage/ledPage\",\"sort\":6,\"parentId\":15,\"resourceVoList\":[]}]},{\"id\":12,\"systemType\":\"roadSide\",\"resourceName\":\"运营设置\",\"resourceType\":\"mod\",\"visitUrl\":\"parkManager\",\"sort\":9,\"icon\":\"icon_ccgl\",\"resourceVoList\":[{\"id\":475,\"systemType\":\"roadSide\",\"resourceName\":\"停车收费规则\",\"resourceType\":\"menu\",\"visitUrl\":\"expense/manage\",\"sort\":3,\"parentId\":12,\"resourceVoList\":[]},{\"id\":18,\"systemType\":\"roadSide\",\"resourceName\":\"长租资费规则\",\"resourceType\":\"menu\",\"visitUrl\":\"longRentManager/rule/page\",\"sort\":4,\"parentId\":12,\"resourceVoList\":[]},{\"id\":42,\"systemType\":\"roadSide\",\"resourceName\":\"小票模板设置\",\"resourceType\":\"menu\",\"visitUrl\":\"ticket/manage/find\",\"sort\":5,\"parentId\":12,\"resourceVoList\":[]},{\"id\":479,\"systemType\":\"roadSide\",\"resourceName\":\"巡查任务配置\",\"resourceType\":\"menu\",\"visitUrl\":\"system/posPatrolTime/findAll\",\"sort\":6,\"parentId\":12,\"resourceVoList\":[]}]},{\"id\":30,\"systemType\":\"roadSide\",\"resourceName\":\"统计报表\",\"resourceType\":\"mod\",\"visitUrl\":\"statistics\",\"sort\":10,\"icon\":\"icon_tjfx\",\"resourceVoList\":[{\"id\":31,\"systemType\":\"roadSide\",\"resourceName\":\"车场收入统计\",\"resourceType\":\"menu\",\"visitUrl\":\"statistics/parkFee/incomeList\",\"sort\":1,\"parentId\":30,\"resourceVoList\":[]},{\"id\":460,\"systemType\":\"roadSide\",\"resourceName\":\"车场欠费统计\",\"resourceType\":\"menu\",\"visitUrl\":\"statistics/parkFee/arrearList\",\"sort\":2,\"icon\":\"\",\"parentId\":30,\"resourceVoList\":[]},{\"id\":461,\"systemType\":\"roadSide\",\"resourceName\":\"车场运营统计\",\"resourceType\":\"menu\",\"visitUrl\":\"statistics/parkFee/operateList\",\"sort\":3,\"icon\":\"\",\"parentId\":30,\"resourceVoList\":[]},{\"id\":462,\"systemType\":\"roadSide\",\"resourceName\":\"收费员操作统计\",\"resourceType\":\"menu\",\"visitUrl\":\"statistics/posUserOperate/page\",\"sort\":4,\"icon\":\"\",\"parentId\":30,\"resourceVoList\":[]},{\"id\":33,\"systemType\":\"roadSide\",\"resourceName\":\"收费员收入统计\",\"resourceType\":\"menu\",\"visitUrl\":\"statistics/pos/list\",\"sort\":5,\"parentId\":30,\"resourceVoList\":[]},{\"id\":28,\"systemType\":\"roadSide\",\"resourceName\":\"每日账单\",\"resourceType\":\"menu\",\"visitUrl\":\"clearService/daily/bill\",\"sort\":6,\"parentId\":30,\"resourceVoList\":[]},{\"id\":29,\"systemType\":\"roadSide\",\"resourceName\":\"结算账单\",\"resourceType\":\"menu\",\"visitUrl\":\"clearService/settlement/bill\",\"sort\":7,\"parentId\":30,\"resourceVoList\":[]}]},{\"id\":34,\"systemType\":\"roadSide\",\"resourceName\":\"人员管理\",\"resourceType\":\"mod\",\"visitUrl\":\"system\",\"sort\":11,\"icon\":\"icon_rygl\",\"resourceVoList\":[{\"id\":37,\"systemType\":\"roadSide\",\"resourceName\":\"手持端用户账号\",\"resourceType\":\"menu\",\"visitUrl\":\"system/toll/page\",\"sort\":1,\"parentId\":34,\"resourceVoList\":[]},{\"id\":447,\"systemType\":\"roadSide\",\"resourceName\":\"手持端角色权限\",\"resourceType\":\"menu\",\"visitUrl\":\"system/posRole/page\",\"sort\":2,\"parentId\":34,\"resourceVoList\":[]}]},{\"id\":41,\"systemType\":\"roadSide\",\"resourceName\":\"系统设置\",\"resourceType\":\"mod\",\"visitUrl\":\"systemManage\",\"sort\":12,\"icon\":\"icon_xtgl\",\"resourceVoList\":[{\"id\":36,\"systemType\":\"roadSide\",\"resourceName\":\"系统用户管理\",\"resourceType\":\"menu\",\"visitUrl\":\"system/user/page\",\"sort\":1,\"parentId\":41,\"resourceVoList\":[]},{\"id\":35,\"systemType\":\"roadSide\",\"resourceName\":\"系统角色权限\",\"resourceType\":\"menu\",\"visitUrl\":\"system/role/page\",\"sort\":2,\"parentId\":41,\"resourceVoList\":[]},{\"id\":448,\"systemType\":\"roadSide\",\"resourceName\":\"操作日志\",\"resourceType\":\"menu\",\"visitUrl\":\"log/pos\",\"sort\":3,\"parentId\":41,\"resourceVoList\":[]}]}]"
# datajson="[{\"id\":442,\"systemType\":\"roadSide\",\"resourceName\":\"实时监控\",\"resourceType\":\"mod\",\"visitUrl\":\"realTimeMonitor\",\"sort\":1,\"icon\":\"icon_shouy\",\"resourceVoList\":[{\"id\":1,\"systemType\":\"roadSide\",\"resourceName\":\"数据监控\",\"resourceType\":\"menu\",\"visitUrl\":\"system/home/index\",\"sort\":1,\"parentId\":442,\"resourceVoList\":[]},{\"id\":164,\"systemType\":\"roadSide\",\"resourceName\":\"地图监控\",\"resourceType\":\"menu\",\"visitUrl\":\"monitor/mapMonitor/parkList\",\"sort\":2,\"parentId\":442,\"resourceVoList\":[]}]},{\"id\":489,\"systemType\":\"roadSide\",\"resourceName\":\"停车管理\",\"resourceType\":\"mod\",\"visitUrl\":\"parkCarManage\",\"sort\":1,\"icon\":\"icon_parkmanage\",\"resourceVoList\":[{\"id\":490,\"systemType\":\"roadSide\",\"resourceName\":\"停车记录\",\"resourceType\":\"menu\",\"visitUrl\":\"parkCarManage/parkRecord/page\",\"sort\":1,\"parentId\":489,\"resourceVoList\":[]},{\"id\":494,\"systemType\":\"roadSide\",\"resourceName\":\"欠费车辆\",\"resourceType\":\"menu\",\"visitUrl\":\"parkOrder/arrears/page\",\"sort\":2,\"parentId\":489,\"resourceVoList\":[]},{\"id\":497,\"systemType\":\"roadSide\",\"resourceName\":\"预警纠查\",\"resourceType\":\"menu\",\"visitUrl\":\"parkOrder/abnormal/info\",\"sort\":3,\"parentId\":489,\"resourceVoList\":[]},{\"id\":504,\"systemType\":\"roadSide\",\"resourceName\":\"超长停车\",\"resourceType\":\"menu\",\"visitUrl\":\"parkOrder/timeOut/page\",\"sort\":4,\"parentId\":489,\"resourceVoList\":[]},{\"id\":508,\"systemType\":\"roadSide\",\"resourceName\":\"无效记录\",\"resourceType\":\"menu\",\"visitUrl\":\"parkCarManage/cancelledRecord/page\",\"sort\":5,\"parentId\":489,\"resourceVoList\":[]}]},{\"id\":7,\"systemType\":\"roadSide\",\"resourceName\":\"交易流水\",\"resourceType\":\"mod\",\"visitUrl\":\"parkOrder\",\"sort\":3,\"icon\":\"icon_ddgl\",\"resourceVoList\":[{\"id\":8,\"systemType\":\"roadSide\",\"resourceName\":\"临停交易\",\"resourceType\":\"menu\",\"visitUrl\":\"parkOrder/trade/payPage\",\"sort\":1,\"parentId\":7,\"resourceVoList\":[]},{\"id\":11,\"systemType\":\"roadSide\",\"resourceName\":\"长租交易\",\"resourceType\":\"menu\",\"visitUrl\":\"parkOrder/longRent/page\",\"sort\":2,\"parentId\":7,\"resourceVoList\":[]}]},{\"id\":17,\"systemType\":\"roadSide\",\"resourceName\":\"包月车辆\",\"resourceType\":\"mod\",\"visitUrl\":\"longRentManager\",\"sort\":4,\"icon\":\"icon_czgl\",\"resourceVoList\":[{\"id\":19,\"systemType\":\"roadSide\",\"resourceName\":\"长租车\",\"resourceType\":\"menu\",\"visitUrl\":\"longRentManager/park/page\",\"sort\":1,\"parentId\":17,\"resourceVoList\":[]},{\"id\":20,\"systemType\":\"roadSide\",\"resourceName\":\"白名单\",\"resourceType\":\"menu\",\"visitUrl\":\"longRentManager/whiteList/list\",\"sort\":2,\"parentId\":17,\"resourceVoList\":[]}]},{\"id\":12,\"systemType\":\"roadSide\",\"resourceName\":\"运营设置\",\"resourceType\":\"mod\",\"visitUrl\":\"parkManager\",\"sort\":5,\"icon\":\"icon_ccgl\",\"resourceVoList\":[{\"id\":13,\"systemType\":\"roadSide\",\"resourceName\":\"车场配置\",\"resourceType\":\"menu\",\"visitUrl\":\"parkManager/park/page\",\"sort\":1,\"parentId\":12,\"resourceVoList\":[]},{\"id\":14,\"systemType\":\"roadSide\",\"resourceName\":\"车位详情\",\"resourceType\":\"menu\",\"visitUrl\":\"parkManager/parkItem/page\",\"sort\":2,\"parentId\":12,\"resourceVoList\":[]},{\"id\":475,\"systemType\":\"roadSide\",\"resourceName\":\"停车资费\",\"resourceType\":\"menu\",\"visitUrl\":\"expense/manage\",\"sort\":3,\"parentId\":12,\"resourceVoList\":[]},{\"id\":18,\"systemType\":\"roadSide\",\"resourceName\":\"长租资费\",\"resourceType\":\"menu\",\"visitUrl\":\"longRentManager/rule/page\",\"sort\":4,\"parentId\":12,\"resourceVoList\":[]},{\"id\":42,\"systemType\":\"roadSide\",\"resourceName\":\"POS小票\",\"resourceType\":\"menu\",\"visitUrl\":\"ticket/manage/find\",\"sort\":5,\"parentId\":12,\"resourceVoList\":[]},{\"id\":479,\"systemType\":\"roadSide\",\"resourceName\":\"巡查配置\",\"resourceType\":\"menu\",\"visitUrl\":\"system/posPatrolTime/findAll\",\"sort\":6,\"parentId\":12,\"resourceVoList\":[]}]},{\"id\":15,\"systemType\":\"roadSide\",\"resourceName\":\"设备管控\",\"resourceType\":\"mod\",\"visitUrl\":\"equipments\",\"sort\":6,\"icon\":\"icon_sbgl\",\"resourceVoList\":[{\"id\":443,\"systemType\":\"roadSide\",\"resourceName\":\"NB地磁\",\"resourceType\":\"menu\",\"visitUrl\":\"equipment/geomagnetic/getRegistered\",\"sort\":1,\"parentId\":15,\"resourceVoList\":[]},{\"id\":444,\"systemType\":\"roadSide\",\"resourceName\":\"高位视频\",\"resourceType\":\"menu\",\"visitUrl\":\"equipment/highVideo/getRegistered\",\"sort\":2,\"parentId\":15,\"resourceVoList\":[]},{\"id\":445,\"systemType\":\"roadSide\",\"resourceName\":\"视频桩\",\"resourceType\":\"menu\",\"visitUrl\":\"equipment/video/getRegistered\",\"sort\":3,\"parentId\":15,\"resourceVoList\":[]},{\"id\":163,\"systemType\":\"roadSide\",\"resourceName\":\"车位锁\",\"resourceType\":\"menu\",\"visitUrl\":\"equipment/roadLock/bindPage\",\"sort\":4,\"parentId\":15,\"resourceVoList\":[]},{\"id\":165,\"systemType\":\"roadSide\",\"resourceName\":\"¡æ¥è½¦\",\"resourceType\":\"menu\",\"visitUrl\":\"equipment/manage/patrolCarList\",\"sort\":5,\"parentId\":15,\"resourceVoList\":[]},{\"id\":446,\"systemType\":\"roadSide\",\"resourceName\":\"ä½ä½å±\",\"resourceType\":\"menu\",\"visitUrl\":\"equipment/manage/ledPage\",\"sort\":6,\"parentId\":15,\"resourceVoList\":[]}]},{\"id\":34,\"systemType\":\"roadSide\",\"resourceName\":\"äººåç®¡ç\",\"resourceType\":\"mod\",\"visitUrl\":\"system\",\"sort\":7,\"icon\":\"icon_rygl\",\"resourceVoList\":[{\"id\":595,\"systemType\":\"roadSide\",\"resourceName\":\"å·¡æ£è´´åè®°å½\",\"resourceType\":\"menu\",\"visitUrl\":\"system/sticker/page\",\"sort\":1,\"parentId\":34,\"resourceVoList\":[]},{\"id\":447,\"systemType\":\"roadSide\",\"resourceName\":\"POSè§è²æé\",\"resourceType\":\"menu\",\"visitUrl\":\"system/posRole/page\",\"sort\":1,\"parentId\":34,\"resourceVoList\":[]},{\"id\":37,\"systemType\":\"roadSide\",\"resourceName\":\"POSç¨æ·ç®¡ç\",\"resourceType\":\"menu\",\"visitUrl\":\"system/toll/page\",\"sort\":2,\"parentId\":34,\"resourceVoList\":[]},{\"id\":168,\"systemType\":\"roadSide\",\"resourceName\":\"äººåç­¾å°æåµ\",\"resourceType\":\"menu\",\"visitUrl\":\"system/userAttendance/signInDetailPage\",\"sort\":3,\"parentId\":34,\"resourceVoList\":[]},{\"id\":480,\"systemType\":\"roadSide\",\"resourceName\":\"å·¡æ¥å®ææåµ\",\"resourceType\":\"menu\",\"visitUrl\":\"system/tollPatrol/page\",\"sort\":4,\"parentId\":34,\"resourceVoList\":[]}]},{\"id\":30,\"systemType\":\"roadSide\",\"resourceName\":\"统计报表\",\"resourceType\":\"mod\",\"visitUrl\":\"statistics\",\"sort\":9,\"icon\":\"icon_tjfx\",\"resourceVoList\":[{\"id\":31,\"systemType\":\"roadSide\",\"resourceName\":\"车场收入统计\",\"resourceType\":\"menu\",\"visitUrl\":\"statistics/parkFee/incomeList\",\"sort\":1,\"parentId\":30,\"resourceVoList\":[]},{\"id\":460,\"systemType\":\"roadSide\",\"resourceName\":\"车场欠费统计\",\"resourceType\":\"menu\",\"visitUrl\":\"statistics/parkFee/arrearList\",\"sort\":2,\"icon\":\"\",\"parentId\":30,\"resourceVoList\":[]},{\"id\":461,\"systemType\":\"roadSide\",\"resourceName\":\"车场运营统计\",\"resourceType\":\"menu\",\"visitUrl\":\"statistics/parkFee/operateList\",\"sort\":3,\"icon\":\"\",\"parentId\":30,\"resourceVoList\":[]},{\"id\":462,\"systemType\":\"roadSide\",\"resourceName\":\"收费员操作统计\",\"resourceType\":\"menu\",\"visitUrl\":\"statistics/posUserOperate/page\",\"sort\":4,\"icon\":\"\",\"parentId\":30,\"resourceVoList\":[]},{\"id\":33,\"systemType\":\"roadSide\",\"resourceName\":\"收费员收入统计\",\"resourceType\":\"menu\",\"visitUrl\":\"statistics/pos/list\",\"sort\":5,\"parentId\":30,\"resourceVoList\":[]},{\"id\":28,\"systemType\":\"roadSide\",\"resourceName\":\"每日账单\",\"resourceType\":\"menu\",\"visitUrl\":\"clearService/daily/bill\",\"sort\":6,\"parentId\":30,\"resourceVoList\":[]},{\"id\":29,\"systemType\":\"roadSide\",\"resourceName\":\"结算账单\",\"resourceType\":\"menu\",\"visitUrl\":\"clearService/settlement/bill\",\"sort\":7,\"parentId\":30,\"resourceVoList\":[]}]},{\"id\":41,\"systemType\":\"roadSide\",\"resourceName\":\"系统设置\",\"resourceType\":\"mod\",\"visitUrl\":\"systemManage\",\"sort\":10,\"icon\":\"icon_xtgl\",\"resourceVoList\":[{\"id\":35,\"systemType\":\"roadSide\",\"resourceName\":\"角色权限\",\"resourceType\":\"menu\",\"visitUrl\":\"system/role/page\",\"sort\":1,\"parentId\":41,\"resourceVoList\":[]},{\"id\":36,\"systemType\":\"roadSide\",\"resourceName\":\"用户管理\",\"resourceType\":\"menu\",\"visitUrl\":\"system/user/page\",\"sort\":2,\"parentId\":41,\"resourceVoList\":[]},{\"id\":448,\"systemType\":\"roadSide\",\"resourceName\":\"操作日志\",\"resourceType\":\"menu\",\"visitUrl\":\"log/pos\",\"sort\":3,\"parentId\":41,\"resourceVoList\":[]}]}]"
print(datajson)
