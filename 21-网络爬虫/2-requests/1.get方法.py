import requests 

url = 'http://jczl.giscloud.cx/CIGService/rest/services/0/intersectFeaturesByXY'
params = {
    "x":'119.880306363',
    "y":"31.063869536"
}

req = requests.get(url,params=params)
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