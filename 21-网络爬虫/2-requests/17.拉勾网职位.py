#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-04-19 15:33:34 
# @Remark: 人生苦短，我用python！
# 备注：通过postman自动生成代码

import requests
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"

payload = {'first': 'true',
'pn': '1',
'kd': 'python'}
files = [

]
headers = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'zh-CN,zh;q=0.9,und;q=0.8,en;q=0.7',
  'Connection': 'keep-alive',
  'Content-Length': '25',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Cookie': 'user_trace_token=20200209220610-d640ad4b-dc96-4a44-a56e-a89fe7792baa; _ga=GA1.2.708725097.1581257172; LGUID=20200209220610-2a3d95ce-4a21-453e-8d66-60924b3218a0; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAAECABFAACEA24898D94B62400FB92D1F907C3E93113; WEBTJ-ID=20200419134551-17190f8b7c1226-0db9b727bd6ec7-6373664-1327104-17190f8b7c23f7; _gid=GA1.2.335286122.1587275152; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1587011868,1587275152; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221702a45e96b1cf-03f580ac9222ee-b383f66-1327104-1702a45e96c3dc%22%2C%22%24device_id%22%3A%221702a45e96b1cf-03f580ac9222ee-b383f66-1327104-1702a45e96c3dc%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2280.0.3987.132%22%7D%7D; TG-TRACK-CODE=search_code; LGSID=20200419150202-c0fd4745-e1f9-4d0a-8904-bda97f24301a; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist%5Fpython%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; X_MIDDLE_TOKEN=674b3a201dc0565b77b30a638dd6ec48; _gat=1; SEARCH_ID=bb3a92745dde44c8af7b66b92d931dbc; X_HTTP_TOKEN=cb9a9928d186223076318278518f96417862597a28; LGRID=20200419152927-9d9e8c3d-39b1-4100-8af8-fadbd4187db6; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1587281369',
  'Host': 'www.lagou.com',
  'Origin': 'https://www.lagou.com',
  'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
  'X-Anit-Forge-Code': '0',
  'X-Anit-Forge-Token': 'None',
  'X-Requested-With': 'XMLHttpRequest',
  'Cookie': 'JSESSIONID=ABAAABAABAGABFA00235821CC5D31DF924DCBDB5AD30069; SEARCH_ID=c504b1add4bd4579bf3bd55b30b10889; user_trace_token=20200419134621-8474493a-59e8-4a33-a558-7548b746870b; X_HTTP_TOKEN=42daf4b72327b2811815727851bf5e71415983ed09; LGSID=20200419134550-42640a6f-cfc1-4cfc-9682-25a1a40846fb; LGRID=20200419150128-0017be70-f079-4e0d-84f1-49e0c5fc2cc9'
}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text)
