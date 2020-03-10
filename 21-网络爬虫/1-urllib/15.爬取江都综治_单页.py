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
req = request.Request("https://jd.spacecig.com/iam/saml/login", data = postdata)

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

# opener包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面 
# 调用接口获取数据
req_list=[
    {
        "url":"realPerson/person/familyPersons1?keyword=&personType=&dwdm=null&name=&cardNum=&gender=&maritalStatus=&politicalStatus=&education=&startBirthdayDate=&endBirthdayDate=&focusService=&focusControl=&isActualAddr=&death=&offset=0&limit=500&orderby=&ordertype=",
        "name":"户籍人口",
        "descript":"户籍人口列表消息"
    }
    ,{
        "url":"places/placeMain/placeCommons?offset=0&limit=800&orderby=&ordertype=&keyword=&departmentId=&placeTypeMax=all&placeType=&createStartDate=&createEndDate=&visitSit=&visitStartDate=&visitEndDate=",
        "name":"场所总况",
        "descript":"场所列表信息"
    },{
        "url":"event/v2/doEvent/sjcx?offset=0&limit=1000&orderby=&ordertype=&querySystem=&cigrole=query&isLeader=1&keyword=&dealDeptId=&dwdm=&eventType=&curnode=&eventSlType=&state=&passCqState=&changeState=&reporter=&reportStartDate=&reportEndDate=&citypartCode=&placeId=&yjaTag=&yjaState=&passCqStartDate=&passCqEndDate=&isXntj=",
        "name":"事件信息",
        "descript":"事件查询信息"
    },{
        "url":"xqglNew/gridRelation/jdQueryList?offset=0&limit=10&orderby=&ordertype=&keyword=&ownerGrid=1125899906842624&objFlag=2&objType=0&createSDate=&createEDate=&areaType=1&politicalStatus=&education=",
        "name":"网格员",
        "descript":"网格员信息"
    }  
]
for li in req_list: 
    req = request.Request("https://jd.spacecig.com/zhzlbackend/%s"%(li["url"]))
    response = opener.open(req)

    res = response.read().decode('utf-8')
    # 打印响应内容
    # 7. 打印响应内容
    with open(r'backup\爬虫\{}.json'.format(li["name"]),'w',encoding='utf8') as f:
        f.write(res)  
        print('成功获取%s！'%li["descript"]) # 打印响应内容 
    
    
    j = json.loads(res)  
    data = j['data']['rows'] 
  
    df = pd.DataFrame() # 最后转换得到的结果
    for line in data:
        df1 = pd.DataFrame([line])
        df = df.append(df1)

    #在excel表格的第1列写入, 不写入index
    df.to_excel(r'backup/excel/{}.xlsx'.format(li["name"]), sheet_name='sheet1', startcol=0, index=False)
