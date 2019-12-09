#!/usr/bin/python
import json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

json2 = json.dumps(data)
print(json2,type(data),type(json2))

print(json.dumps({'av': 'Runoob', 'ab': 7}, sort_keys=True, indent=4, separators=(',', ': ')))

content = '{"name":"航天神舟智慧系统技术有限公司","sex":"man"}'
 
print(type(json.loads(content)))
 
jsonstr = json.loads(content) 

print(jsonstr)
print(json.dumps(jsonstr))

#python使用json.dump()的中文编码问题
#当json中有中文字符串时:

#open时加上encoding=‘utf-8'，
#dump时加上ensure_ascii=False，
#（这是因为json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False）
print(json.dumps(jsonstr,ensure_ascii=False))

#python中json.load()、json.loads()、json.dump()、json.dumps()的区别
#json.load()从文件中读取json字符串

#json.loads()将json字符串转换为字典类型

#json.dumps()将python中的字典类型转换为字符串类型

#json.dump()将json格式字符串写到文件中