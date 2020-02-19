import urllib.request
import time
from urllib import parse

word = 'q=中国梦&wd=单独的&dg=发发&dg=DFD'
url = ('http', 'www', 'baidu', 'com', 'dfdf', 'eddffa') # 这里至少需要6个元素
print(parse.urlunparse(url)) 
print(parse.quote(word),parse.parse_qs(word))
print(parse.unquote(parse.quote(word))) 

url='http://user:pwd@domain:80/path;params?query=queryarg&para1=p#fragment'
url_change = urllib.parse.urlparse(url)
print('parsed_result 包含了',len(url_change),'个元素')
print(url_change) 

print('scheme  :', url_change.scheme)
print('username:', url_change.username)
print('password:', url_change.password)
print('hostname:', url_change.hostname)
print('port    :', url_change.port) 
print('netloc  :', url_change.netloc)
print('path    :', url_change.path)
print('params  :', url_change.params)
print('query   :', url_change.query)
print('fragment:', url_change.fragment) #锚点

print('-'*40)

url = 'http://ip/'
path = 'api/user/login'
url = parse.urljoin(url,path)

print(url)

data={"name":"王尼玛","age":"/","addr":"abcdef"}
print(url+'?'+urllib.parse.urlencode(data)) 
