# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 10:03:20 2018

@author: lenovo
"""

import urllib.request as r
city_pinyin=input("请输入城市拼音：")
address='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996'
info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
print(info)

import json
data=json.loads(info)

city=data['city']['name']
print("当前城市："+str(city))

for i in range (38):
    day=data['list'][i]['dt_txt']
    print("日期和时刻："+str(day))
    description=data['list'][i]['weather'][0]['description']
    print("当前天气状况:"+str(description))
    temp=data['list'][i]['main']['temp']
    print("当前天气温度："+str(temp)+"开摄氏度")
    pressure=data['list'][i]['main']['pressure']
    print("当前气压为："+str(pressure))
    print("--------------------------------------------------")
    if str(data['list'][i]['dt_txt'])[9:10]!=str(data['list'][i+1]['dt_txt'])[9:10]:
        print("***********************************************************")
    
 #    D=str(data['list'][i]['dt_txt'])[9:10]   
'opiu'[2:2]
    
day=data['list'][i]['dt_txt']
listday=list(day)
listday
n=len(listday) 
n 
n=len(listday)
n
day
D=str(data['list'][i]['dt_txt'])[9:10]
D
    
    

day=data['list'][3]['dt_txt']
print("日期："+str(day))
description=data['list'][3]['weather'][0]['description']
print("天气状况:"+str(description))
temp=data['list'][3]['main']['temp']
print("天气温度："+str(temp)+"开摄氏度")
pressure=data['list'][3]['main']['pressure']
print("气压为："+str(pressure))