# -*- coding: utf-8 -*-
from urllib import request,parse
from http import cookiejar

# 声明一个CookieJar对象实例来保存cookie
cookie = cookiejar.CookieJar()

# 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
cookie_handle = request.HTTPCookieProcessor(cookie)

# 创建http请求管理器
http_handle = request.HTTPHandler()

# 创建https管理器
https_handle = request.HTTPSHandler()

# 通过handler来构建opener
opener =  request.build_opener(cookie_handle,http_handle,https_handle)

# 此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('https://www.baidu.com')

print('name'+' |'+' '+'value')
for item in cookie:
    print(item.name, ' | ', item.value)
