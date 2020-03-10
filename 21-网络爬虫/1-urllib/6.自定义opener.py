import urllib
from urllib import request

# 参考链接：https://blog.csdn.net/Ka_Ka314/article/details/80972732  
 
https_handler = urllib.request.HTTPSHandler(debuglevel=1)   #构建一个HTTPHandler 处理器对象，支持处理HTTPS请求
http_handler  = urllib.request.HTTPHandler(debuglevel=1)    #构建一个HTTPHandler 处理器对象，支持处理HTTP请求

# 方式1
opener = urllib.request.build_opener(https_handler)         #创建一个打开器

# 如果这么写，就是将opener应用到全局，之后所有的，不管是opener.open()还是urlopen() 发送请求，都将使用自定义代理。
urllib.request.install_opener(opener)                       #安装一个全局的打开器(这一步可选不安装采用默认)
request = urllib.request.Request("http://www.baidu.com/")

# opener打开请求
response = opener.open(request)                       
print(len(response.read().decode()))

# 方式2
response = urllib.request.urlopen('http://www.baidu.com') #urllib.request.urlopen() 特殊的opener
#print(response.read().decode())