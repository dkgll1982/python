import requests
import json

# 添加cookie
url = 'http://api.nnzhp.cn/api/user/gold_add'
data = {'stu_id':231,'gold':123}
cookie = {'niuhanyang':'7e4c46e5790ca7d5165eb32d0a895ab1'}
req = requests.post(url,data,cookies=cookie)
print(req.json())

#上传文件
url = 'http://api.nnzhp.cn/api/file/file_upload'
f = open(r'backup\1.html','rb')
r = requests.post(url,files={'file':f})
users_dic = r.json()
print(users_dic)

# 下载文件
url = 'http://www.besttest.cn/data/upload/201710/f_36b1c59ecf3b8ff5b0acaf2ea42bafe0.jpg'
r = requests.get(url)
print(r.status_code)#获取请求的状态码
#print(r.content)#获取返回结果的二进制格式
with open(r'backup\mpp.jpg','wb') as fw:
    fw.write(r.content) 