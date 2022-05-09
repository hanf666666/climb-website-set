#!/usr/bin/python3
# encoding: utf-8

"""
@project = scrapydemo3
@file_name = pagedatajsondemo.py
@author =  Hj
@datetime = 2022/4/24
"""
import json

dataPageList={
  "d": "[{\"projectid\":\"862545\",\"projectname\":\"华宇锦绣玺岸大渡口组团H分区H06-4-1、H06-4-5、H06-5号地块（一期A区）\",\"enterprisename\":\"重庆盛毓锦鑫房地产开发有限公司\",\"location\":\"大渡口区大渡口组团H分区H06-4-1、H06-5地块\",\"f_presale_cert\":\"渝住建委（2022）预字第（233）号\",\"blockname\":\"规划30号楼,规划18号楼\",\"buildingid\":\"fkVGzqbxr9cgCXNAq2QGyQ,A6Pk6gy8X0qNekBFsEq/YA\",\"counts\":\"2058\"},{\"projectid\":\"862545\",\"projectname\":\"华宇锦绣玺岸大渡口组团H分区H06-4-1、H06-4-5、H06-5号地块（一期A区）\",\"enterprisename\":\"重庆盛毓锦鑫房地产开发有限公司\",\"location\":\"大渡口区大渡口组团H分区H06-4-1、H06-5地块\",\"f_presale_cert\":\"渝住建委（2022）预字第（223）号\",\"blockname\":\"规划14号楼\",\"buildingid\":\"QMegIjZJiC1bnCKxtmX3HQ\",\"counts\":\"2058\"},{\"projectid\":\"933544\",\"projectname\":\"碧桂园龙兴国际生态城龙兴国际生态城（H31-1/02地块）\",\"enterprisename\":\"重庆市碧嘉逸房地产开发有限公司\",\"location\":\"渝北区龙兴镇焕龙路603号\",\"f_presale_cert\":\"渝住建委（2022）预字第（228）号\",\"blockname\":\"5幢（规划2号楼）,11幢（规划9号楼）\",\"buildingid\":\"_XFBtvBkii0oeuF/698KUA,KAfUvsg4eSpripu9OpKsOQ\",\"counts\":\"2058\"},{\"projectid\":\"804563\",\"projectname\":\"禹洲雍锦府悦山\",\"enterprisename\":\"重庆翔泽房地产开发有限公司\",\"location\":\"北碚区北碚组团I分区I18-01/04号宗地\",\"f_presale_cert\":\"渝住建委（2022）预字第（230）号\",\"blockname\":\"规划2号楼\",\"buildingid\":\"VkwRyFuWK3y_FrNKnN4b0A\",\"counts\":\"2058\"},{\"projectid\":\"934570\",\"projectname\":\"龙湖颐天康养天曜蔡家L标准分区项目L05-1/06地块\",\"enterprisename\":\"重庆龙湖颐天鼎圣房地产开发有限公司\",\"location\":\"北碚区蔡家组团L标准分区L05-1/06地块\",\"f_presale_cert\":\"渝住建委（2022）预字第（217）号\",\"blockname\":\"1幢（规划05-1号楼）,2幢（规划05-2号楼）,5幢（规划05-5号楼）,6幢（规划05-6号楼）\",\"buildingid\":\"Pr4bd2SHQJB47omAoydb3g,FY9h9cgKwNfL1c4V70LTTg,eKEHohSrQ/hiincQf3JGJA,lV4zRQIE45IoLaworhh7ng\",\"counts\":\"2058\"},{\"projectid\":\"70781\",\"projectname\":\"御景天水\",\"enterprisename\":\"重庆天成缘江置业有限公司\",\"location\":\"九龙坡区冬山路7号\",\"f_presale_cert\":\"渝住建委（2022）预字第（226）号\",\"blockname\":\"65幢（规划C-3号楼）\",\"buildingid\":\"mCzUioVNTGUXVI6AN7fEjw\",\"counts\":\"2058\"},{\"projectid\":\"917043\",\"projectname\":\"招商渝天府沙坪坝区西永组团Ah标准分区Ah20-01-02/04地块\",\"enterprisename\":\"重庆招商启盛房地产开发有限公司\",\"location\":\"沙坪坝区西永组团Ah标准分区Ah20-01-02/04地块\",\"f_presale_cert\":\"渝住建委（2022）预字第（231）号\",\"blockname\":\"5幢（规划5号楼）,14幢（规划14号楼）\",\"buildingid\":\"gAhCBeYFRH0RXwrogzx_9w,zb/cH1rberF61xMHPsmnNQ\",\"counts\":\"2058\"},{\"projectid\":\"905599\",\"projectname\":\"东原.月印万川Q18-2号宗地\",\"enterprisename\":\"重庆东展钧合房地产开发有限公司\",\"location\":\"两江新区悦来组团Q分区Q18-2号宗地\",\"f_presale_cert\":\"渝住建委（2022）预字第（227）号\",\"blockname\":\"规划4号楼\",\"buildingid\":\"wG800QeorVMcEspIzL4fkA\",\"counts\":\"2058\"},{\"projectid\":\"891241\",\"projectname\":\"中建·滨江星城K13-12地块\",\"enterprisename\":\"重庆宏展置业有限公司\",\"location\":\"巴南区金溪路68号\",\"f_presale_cert\":\"渝住建委（2022）预字第（225）号\",\"blockname\":\"5幢（规划5号楼）,3幢（规划3号楼）\",\"buildingid\":\"7XfK7qizdy8jUDcjD9F6zg,zzIcVMUhPPoNZBo7TCw6vQ\",\"counts\":\"2058\"},{\"projectid\":\"918202\",\"projectname\":\"君临南山.崇德府2期君临南山2期\",\"enterprisename\":\"重庆金瑜盛实业有限公司\",\"location\":\"重庆市南岸区崇文路17号\",\"f_presale_cert\":\"渝住建委（2022）预字第（221）号\",\"blockname\":\"12幢（规划15号楼）,11幢（规划16号楼）\",\"buildingid\":\"NeyvEzrmziwe3mpcfqMUDA,dfOLg2WZsTfHMq5m2rinsw\",\"counts\":\"2058\"}]"
}

dataPageJsonAray = json.loads(dataPageList["d"])
print(len(dataPageJsonAray))
for json in dataPageJsonAray:
    print(json)
    # print(json["buildingid"])
    # for room in json['rooms']:
    #     print(room)