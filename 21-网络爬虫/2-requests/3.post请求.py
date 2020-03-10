import requests 
import json

url = 'http://httpbin.org/post'
params = {
    "username":'dpp0130',
    "pwd":"Mp123456",
    "cpwd":"Mp123456"
}

#发送post请求,注册接口
req = requests.post(url,data=params) 
print('1:',req.text) 
print('') 
print('2:',req.content) 
print('3:',req.history) 
print(req.url) 
print('4:',req.cookies) 
print(req.status_code==requests.codes.ok)