
import telnetlib
import random
import requests

#免费代理随时会失效
proxy_list = [
    {"http": "58.87.98.112:1080"} 
]

proxies = random.choice(proxy_list)
#此网站返回访问者IP地址(可以测试返回的是否是代理ip)
response = requests.get("http://httpbin.org/ip",proxies = proxies,timeout = 10)
print(response.text)

print('-'*40)
 
'''head 信息'''
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36', 
       'Connection': 'keep-alive'}
'''http://icanhazip.com会返回当前的IP地址'''
p = requests.get('http://icanhazip.com', headers = head, proxies = proxies,timeout = 20)
print(p.text)
