import urllib.request
import random
import ssl

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
    {"http": "113.121.66.221:9999"},
    {"http": "222.189.190.68:9999"},
    {"http": "39.108.71.144:9999"},
    {"http": "182.35.83.9:9999"},
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

print(response.status)
