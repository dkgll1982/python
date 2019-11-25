import requests
import json
#请求api地址
url ="http://127.0.0.1:5001/gydsj/flsc/getFirmList"
#请求参数
data={
    'deptId':1191870604509184,
    'pjYear':2018,
    'pjMonth':3,
    'pjLevel':'D',
    'pState':0,
    'pResult':'',
    'offset':0,
    'limit':20
}
#执行请求
response= requests.get(url,params=data)
#查看执行的url
print('\n查看请求执行的url:\n',response.url)
#获得请求的内容
print('\n获得请求的内容:\n' , response.text)
#解析获取的json数据
data_json = json.loads(response.text)
print('\n解析获取json中data的值:\n',data_json['data'])