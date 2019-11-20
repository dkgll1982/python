import json

content = json.load(open(r'.vscode\tasks.json', 'r', encoding='utf-8'))
print(type(content))            #<class 'dict'>

json_dicts = json.dumps(content, indent=4, ensure_ascii=False)
print(json_dicts)
print(type(json_dicts))         #<class 'str'>

# 定义字典类型字符串
user_dic = json.loads(json_dicts)  
print(user_dic) 
