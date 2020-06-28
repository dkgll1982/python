import requests 

url = 'http:/699pic.com/image/xuanzhuanqiu.html'
params = {
    "x":'119.880306363',
    "y":"31.063869536"
}
header = {
    "host": "699pic.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
}

req = requests.get(url = url,params=params,headers = header)
print(type(req),req.status_code,req.encoding,req.headers,req.url)
print('')
print('---->',req.text)
print('====>',req.content.decode('utf8')) # content是byte类型，进行解码
print(req.cookies)
print('')
dict = req.json()   #如果返回的是json格式的字符串，调用此方法直接得到一个字典，如果不是，会抛出json.decoder.JSONDecodeError异常
print(dict)
for key in dict.keys():
    print("'{}':'{}'".format(key,dict[key]))