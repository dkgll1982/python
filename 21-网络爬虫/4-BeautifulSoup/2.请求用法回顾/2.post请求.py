import urllib.request
import urllib.response
import urllib.parse
import urllib.error 
from urllib import request

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
data = {
    'name': 'zhaofan',
    'age':'12',
    'male':'男'
}

parse = bytes(urllib.parse.urlencode(data),'utf-8')

req = request.Request(url, headers=headers,method= 'post')
#或者通过add_header()添加请求头部
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0')
#urlopen打开URL网址,url参数可以是一个字符串url或者是一个Request对象,
# 返回的是http.client.HTTPResponse对象.http.client.HTTPResponse对象大概包括read()、readinto()、
# getheader()、getheaders()、fileno()、msg、version、status、reason、debuglevel和closed函数

#注意：req = urllib.request.urlopen(url,data,head)加了header 直接用urlopen会报错
#response = request.urlopen(url, headers=headers,method= 'post', data=parse)
response = request.urlopen(req, data=parse)
print(response.read().decode('utf-8'))