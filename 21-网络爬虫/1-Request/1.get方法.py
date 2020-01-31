import requests 

url = 'http://jczl.giscloud.cx/CIGService/rest/services/0/intersectFeaturesByXY'
params = {
    "x":'119.880306363',
    "y":"31.063869536"
}

req = requests.get(url,params=params)
print(req.status_code,req.encoding,req.headers,req.url)
print('')
print(req.text)
print('')
dict = req.json()
for key in dict.keys():
    print("'{}':'{}'".format(key,dict[key]))