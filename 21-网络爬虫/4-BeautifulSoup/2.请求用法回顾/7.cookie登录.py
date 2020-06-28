#coding:utf8
import requests

response = requests.get('http://www.baidu.com')
print(response.cookies)
print(response.cookies.items())  # [('BDORZ', '27315')]
for key, value in response.cookies.items():
    print(key + '=' + value)
    
#模拟登陆
s = requests.Session()
s.get('http://httpbin.org/cookies/set/BDORZ/123456')
response = s.get('http://httpbin.org/cookies')
print(response.text)

from urllib.parse import urlunparse

data = ['http','www.baidu.com','index.html','user','a=123','commit']
print(urlunparse(data))

from urllib.parse import urljoin


print(urljoin('http:', '//www.cnblogs.com'))
print(urljoin('http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.baidu.com', 'https://pythonsite.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://pythonsite.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://pythonsite.com/FAQ.html?question=2'))
print(urljoin('http://www.baidu.com?wd=abc', 'https://pythonsite.com/index.php'))
print(urljoin('http://www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com#comment', '?category=2'))