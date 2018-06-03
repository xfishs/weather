# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import urllib.request as r
import json
city = input("输入城市（拼音）");
address='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric' 
info=r.urlopen(address.format(city)).read().decode('utf-8','ignore') 
data = json.loads(info)
date = []
weather = {"日期":[],"天气":[],"最高气温":[],"最低气温":[],"气压":[]}
for i in range(len(data["list"])):
    weather["日期"].append(data["list"][i]["dt_txt"])
    weather["天气"].append(data["list"][i]["weather"][0]["description"])
    weather["最高气温"].append(data["list"][i]["main"]["temp_max"])
    weather["最低气温"].append(data["list"][i]["main"]["temp_min"])
    weather["气压"].append(data["list"][i]["main"]["pressure"])

string="**********************************\n当前日期：\t{}\n当前天气：\t{}\n最高温度：\t{}\n最低温度：\t{}\n当前气压：\t{}\n\n**********************************"
pointData = weather["日期"][0][:10]
print("\n\n\n********************{}********************".format(pointData))
for i in range(len(data["list"])):
    if weather["日期"][i][:10] != pointData:
        pointData = weather["日期"][i][:10]
        print("\n\n\n********************{}********************".format(pointData))
    print(string.format(weather["日期"][i],weather["天气"][i],weather["最高气温"][i],weather["最低气温"][i],weather["气压"][i]))