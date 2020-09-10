import urllib.request
import random
import ssl
import requests

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.baidu.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
}

'''
:16816
'''

#免费代理
proxy_list = [
    {"http": "94.25.104.250:8080"},
    {"http": "1.20.156.230:8080"},
    {"http": "175.42.128.134:9999"},
    {"http": "164.163.12.50:8080"},
]

proxies = random.choice(proxy_list)

# authproxy = {
#     "https": "188.131.173.36:16816"
# }

authproxy = {
    "https": "496155678:tx4p1gbw@188.131.173.36:16816"
}

proxyhandler = urllib.request.ProxyHandler(
    proxies = proxies
)
# 创建一个opener
opener = urllib.request.build_opener(proxyhandler)

request = urllib.request.Request(url=url, headers=headers)

response = opener.open(request)

# with open(r'backup\爬虫\baidu.txt','wb') as f:
#     f.write(response.read())     
   
import telnetlib


def test_ip(ip,port):
    try:
        telnetlib.Telnet(ip,port,timeout = 10)
        print(f"代理ip:{ip}有效！")
    except:
        print(f"代理ip:{ip}无效！")
        
test_ip("58.87.98.112","1080")
test_ip("113.121.95.193","9999")
test_ip("171.35.171.85","9999")

proxy_list = [
    {"http": "58.87.98.112:1080"} 
]

proxies = random.choice(proxy_list)

#此网站返回访问者IP地址(可以测试返回的是否是代理ip)
response = requests.get("http://httpbin.org/ip",proxies = proxies,timeout = 10)

print(response.text)


import requests
'''代理IP地址（高匿）'''
proxy = {
  'http': 'http://117.85.105.170:808',
  'https': 'https://117.85.105.170:808'
}
'''head 信息'''
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36', 
       'Connection': 'keep-alive'}
'''http://icanhazip.com会返回当前的IP地址'''
p = requests.get('http://icanhazip.com', headers=head, proxies=proxy)
print(p.text)
