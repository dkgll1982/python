import requests 
import json

url = 'http://api.nnzhp.cn/api/user/user_reg'
params = {
    "username":'dpp0130',
    "pwd":"Mp123456",
    "cpwd":"Mp123456"
}

#发送post请求,注册接口
req = requests.post(url,data=params)
print(req.status_code,req.encoding,req.headers,req.url)
print('')
print(req.text)
print('')
dict = req.json()
for key in dict.keys():
    print("'{}':'{}'".format(key,dict[key]))
    
print('-------------------------------')

#入参是json
# url = 'http://api.nnzhp.cn/api/user/add_stu'
# data = {
#     'name':'353',
#     'grade':'fghfgh',
#     'phone':'22611301234'
#     }

url = 'http://localhost:5000/todo/api/v1.0/tasks'
data = { 
    'title':'flask的post调用方式',
    'description':'描述信息'
    }
req = requests.post(url,json=data)
dict = req.json()['task']
for key in dict.keys():
    print("'{}':'{}'".format(key,dict[key]))
    
print('=============================')

#添加header
# url = 'http://api.nnzhp.cn/api/user/all_stu'
# header = {'Referer':'http://api.nnzhp.cn/'}
#print(res.json()['stu_info'][0])
# json_str = json.dumps(res.json(), indent=4, ensure_ascii=False)
# with open(r'backup/person.json', 'w', encoding='utf-8') as f:
#     f.write(json_str)

url = 'http://localhost:5000/todo/api/v1.0/tasks/2'
header = {'Referer':'jczl.com'}         #防盗链
res = requests.get(url,headers=header)
print(res.json())