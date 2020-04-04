#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-02-21 19:20:37 
# @Last Modified by: guojun 
# @Last Modified time: 2020-02-21 19:20:37 
# @Software: vscode 
from urllib import request
import http.cookiejar as cookielib
import urllib
import json
import pandas as pd
from lxml import etree
 
# 通过CookieJar()类构建一个cookieJar()对象，用来保存cookie的值
cookie = cookielib.CookieJar()

# 通过HTTPCookieProcessor()处理器类构建一个处理器对象，用来处理cookie
# 参数就是构建的CookieJar()对象
cookie_handler = request.HTTPCookieProcessor(cookie)

opener = request.build_opener(cookie_handler)

# 自定义opener的addheadders的参数，可以赋值HTTP报头参数
opener.addheaders = [("Content-type","application/json;charset=UTF-8"),("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36")]

# 需要登录的账户和密码
data = {"userid":"admin", "password":"DFYOPS1RrpdVlu2U"} 

# 通过urlencode()转码
postdata = urllib.parse.urlencode(data).encode('utf8')

# 构建Request请求对象，包含需要发送的用户名和密码
req = request.Request("http://jczl.giscloud.cx/iam/saml/login", data = postdata)

# 通过opener发送这个请求，并获取登录后的Cookie值，
response = opener.open(req) 
print(response.read().decode('utf-8'))

# 可以按标准格式将保存的Cookie打印出来
cookieStr = ""
for item in cookie:
    cookieStr = cookieStr + item.name + "=" + item.value + ";"

# 舍去最后一位的分号(此处取到cookie值)
cookieStr = cookieStr[:-1] 
print("Cookie:",cookieStr)
 
# 调用接口获取数据
req_list=[
    {
        "url":"realPerson/person/familyPersons1?keyword=&personType=&dwdm=&name=&cardNum=&gender=&maritalStatus=&politicalStatus=&education=&startBirthdayDate=&endBirthdayDate=&focusService=&focusControl=&isActualAddr=&isCar=&%C2%A0carNature=&isHouse=&isLegalPerson=&personTag=&offset=10&limit=10&orderby=&ordertype=",
        "name":"户籍人口",
        "descript":"户籍人口列表消息"
    } 
]
for li in req_list: 
    req = request.Request("http://jczl.giscloud.cx/zhzl-frames/main2.html") 
    response = opener.open(req)

    res = response.read().decode('utf-8') 
    html = etree.HTML(res)
    title = html.xpath('//title')
    print(title[0].text)