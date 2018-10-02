# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 11:30:12 2018

@author: benak
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 10:51:38 2018

@author: benak
"""
#菜鸡写的时间分析爬虫，因为是Python所以分析出来的数据误差较大
#目前只有最简单的功能，，，还没有加入微信推送

#from bs4 import BeautifulSoup
#import bs4
#import os
#import csv
import requests
from urllib import request
#import urllib.parse
import json
from http import cookiejar
import ssl
#import csv
import openpyxl
#import gc
import time
lgurl = r'https://svr.jikecloud.net/user/login'
jurl = r'https://svr.jikecloud.net/gpu/type/list'
ssl._create_default_https_context = ssl._create_unverified_context
header = {
	
"Accept": "application/json, text/javascript, */*; q=0.01",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
"Connection": "close",
"Content-Length": "67",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#"Cookie": "Hm_lvt_dbfa468b149fbfa4272efada10bdc22e=1532433770,1533054225,1534132408,1534146039; JSESSIONID=D6989EC1760D28C8B0DBD8972C370410; Hm_lpvt_dbfa468b149fbfa4272efada10bdc22e=1534178042",
"Host": "svr.jikecloud.net",
"Origin": "https://www.jikecloud.net",
"Referer": "https://www.jikecloud.net/login.html",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
"Cookie": "Hm_lvt_dbfa468b149fbfa4272efada10bdc22e=1534321014,1534408594,1534418889,1534518497; JSESSIONID=74DFAFF31F1418AADB83368C51879E46; Hm_lpvt_dbfa468b149fbfa4272efada10bdc22e=1534518570"	
}
#header_code = {
#	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
#	"Referer": "https://www.jikecloud.net/login.html",
#	"Host": "svr.jikecloud.net",

#}
S = requests.session()
URL = r'https://svr.jikecloud.net/user/login'

def main():
    print("1:GTX 1080 Ti 12核24G + 250GB SSD + 2TB硬盘 (独占5元每小时)")
    print("2:GTX 1080 Ti 12核32G 250GB SSD + 3TB硬盘 (独占5元每小时)")
    print("3:Titan XP 12核32G 双卡(限时特价独占6元每小时)")
    print("4:gtx1070")
    select = int(input("请选择你要观察的GPU型号"))
    G1="GTX 1080 Ti 12核24G + 250GB SSD + 2TB硬盘 (独占5元每小时)"
    G2="GTX 1080 Ti 12核32G 250GB SSD + 3TB硬盘 (独占5元每小时)"
    G3="Titan XP 12核32G 双卡(限时特价独占6元每小时)"
    G4="GTX 1070 12核32G 120GB SSD + 2TB硬盘 (独占3元每小时)"
    if select==1:
        chk=G1
    elif select==2:
        chk=G2
    elif select==3:
        chk=G3
    elif select==4:
        chk=G4
    #print (chk)
    #脚本总运行时间
    obT=0
    
    while True:
      
            obT=int(input("输入观测时间，请(秒)"))
            if obT>60:
                break
            else:
                print("输入单位是秒啊kora!!!")
                continue
        
    #观察的实例运行的时间
    occT=0
    login_info = {"id":1,"params":{'username':'','passwd':''}}
    
    occT = login2next(login_info,occT,chk,obT)
    ans=occT/obT
    print (ans)
        
        
        
def login2next(data,occT,chk,obT):
    start=time.clock()
    while True:
            
            
            try:
                req = requests.post(url=lgurl,data=json.dumps(data),headers=header,verify=False)
                #response1 = opener.open(req)
                print(req)
                    
                filename = 'D:\log of GPU\cookie2.txt'
                #声明一个CookieJar对象实例来保存cookie
                cookie = cookiejar.MozillaCookieJar(filename)
                #从文件中读取cookie内容到变量
                cookie.load(filename, ignore_discard=True, ignore_expires=True)
                #利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
                handler=request.HTTPCookieProcessor(cookie)
                #通过CookieHandler创建opener
                opener = request.build_opener(handler)
                #此处的open方法打开网页
                response = opener.open('https://www.jikecloud.net/')
                #打印cookie信息
                for item in cookie:
                    print('Name = %s' % item.name)
                    print('Value = %s' % item.value)
                cookie.save(ignore_discard=True, ignore_expires=True)
                formdata={"id":1,"params":{"all":"true","exclude_geek":"false","only_available":"false","region_id":"null"}}
                #formdata = urllib.parse.urlencode(formdata).encode('utf-8')
                wbdata = requests.post(url=jurl,data=json.dumps(formdata),headers=header,verify=False).text
                #response2 = opener.open(wbdata)
                dataa = json.loads(wbdata)
                #print(dataa)
                rawdata = dataa["result"]
                #print(rawdata)
                for n in rawdata:
                    if n['desc']==chk:
                        gotcha=n
                        break
                print(gotcha)
                if (gotcha['isAvailable']==False):
                   occT=timelog(gotcha['desc'],data,occT)
                   stop=time.clock()
                   times=stop-start
                   if times >=obT:
                       break
                   continue
                else:
                    stop=time.clock()
                    times=stop-start
                    if times >=obT:
                        break
                    time.sleep(600)
                    continue
                
            except requests.exceptions.ConnectionError:
                time.sleep(5)
                continue
    return occT       
    

def loginnchk(data,chk):
    while True:
            try:
                req = requests.post(url=lgurl,data=json.dumps(data),headers=header,verify=False)
                #response1 = opener.open(req)
                print(req)
                    
                filename = 'D:\log of GPU\cookie2.txt'
                #声明一个CookieJar对象实例来保存cookie
                cookie = cookiejar.MozillaCookieJar(filename)
                #从文件中读取cookie内容到变量
                cookie.load(filename, ignore_discard=True, ignore_expires=True)
                #利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
                handler=request.HTTPCookieProcessor(cookie)
                #通过CookieHandler创建opener
                opener = request.build_opener(handler)
                #此处的open方法打开网页
                response = opener.open('https://www.jikecloud.net/')
                #打印cookie信息
                for item in cookie:
                    print('Name = %s' % item.name)
                    print('Value = %s' % item.value)
                cookie.save(ignore_discard=True, ignore_expires=True)
                formdata={"id":1,"params":{"all":"true","exclude_geek":"false","only_available":"false","region_id":"null"}}
                #formdata = urllib.parse.urlencode(formdata).encode('utf-8')
                wbdata = requests.post(url=jurl,data=json.dumps(formdata),headers=header,verify=False).text
                #response2 = opener.open(wbdata)
                dataa = json.loads(wbdata)
                #print(dataa)
                rawdata = dataa["result"]
                #print(rawdata)
                for n in rawdata:
                    if n['desc']==chk:
                        gotcha=n
                        break
                #print(gotcha)
                if (gotcha['isAvailable']==False):
                   time.sleep(600)
                   continue
                else:
                    return
                    
            except requests.exceptions.ConnectionError:
                time.sleep(5)
                continue
            
def timelog(gotcha,data,occT):
    start=time.clock()
    loginnchk(data,gotcha)
    stop=time.clock()
    occT=occT+(stop-start)
    return occT
    
    
if __name__ == "__name__":
	main()
        
        
