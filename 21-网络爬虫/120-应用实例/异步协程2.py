#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-05-22 10:38:32 
# @Remark: 人生苦短，我用python！

import aiohttp
import asyncio
import time
import urllib
import cx_Oracle
import socket
import os
import requests
from urllib import request
import http.cookiejar as cookielib
import json
from concurrent.futures import ThreadPoolExecutor

host = 'http://jczl.giscloud.cx/'
inter_url = host + "healthWeb/front/index/healthQuery"
per_data = {"sfzh":"340406198507213836","mzt":"绿码","mffd":"杭州市"}
form_data = bytes(json.dumps(per_data), 'utf8')

def get_host_ip():
    """
    查询本机ip地址
    :return:
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

def get_cookie():   
        login_url = host + "iam/saml/login"
        userpwd = {"userid":"admin", "password":"DFYOPS1RrpdVlu2U"}  
        
        # 通过CookieJar()类构建一个cookieJar()对象，用来保存cookie的值
        cookie = cookielib.CookieJar()
        # 通过HTTPCookieProcessor()处理器类构建一个处理器对象，用来处理cookie
        # 参数就是构建的CookieJar()对象
        cookie_handler = request.HTTPCookieProcessor(cookie)
        opener = request.build_opener(cookie_handler)
        # 自定义opener的addheadders的参数，可以赋值HTTP报头参数
        opener.addheaders = [("Content-type","application/json;charset=UTF-8"),("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36")]
  
        # 通过urlencode()转码
        postdata = urllib.parse.urlencode(userpwd).encode('utf8')
        # 构建Request请求对象，包含需要发送的用户名和密码
        req = request.Request(login_url, data = postdata)
        # 通过opener发送这个请求，并获取登录后的Cookie值，
        response = opener.open(req)  
        # 可以按标准格式将保存的Cookie打印出来
        cookieStr = ""
        for item in cookie:
            cookieStr = cookieStr + item.name + "=" + item.value + ";"

        # 舍去最后一位的分号(此处取到cookie值)
        cookieStr = cookieStr[:-1]   
        headers = {
            "Host":'jczl.giscloud.cx',
            "Content-type":"application/json;charset=UTF-8",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36",
            "Cookie":cookieStr
        } 
        return headers

header = get_cookie()
print(header)

async def get_page(name,url,data,header):
    async with aiohttp.ClientSession() as session:
        async with await session.post(url=url,data=data,headers=header) as response:
            page_text = await response.text()  
            print('接口:%s,结果:%s'%(name,page_text))

def request(args):            
    for i in range(args):
        tasks = []
        loop = asyncio.get_event_loop()

        c = get_page('杭州健康码',inter_url,form_data,header)
        task = asyncio.ensure_future(c)
        tasks.append(task)
        loop.run_until_complete(asyncio.wait(tasks))
                    
def request3(args): 
    print(args)
    
start = time.time()
 
request(2)

print('总耗时：', time.time()-start)
