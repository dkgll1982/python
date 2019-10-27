#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-21 17:01:10 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-21 17:01:10 
# @Software: vscode 

import requests
import json

host = "http://httpbin.org/"
endpoint = "post"

url = ''.join([host,endpoint])
data = {
    "sites": [
                { "name":"test" , "url":"www.test.com" },
                { "name":"google" , "url":"www.google.com" },
                { "name":"weibo" , "url":"www.weibo.com" }
    ]
}

r = requests.post(url,json=data)
# r = requests.post(url,data=json.dumps(data))
response = r.json()