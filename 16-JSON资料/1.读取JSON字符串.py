import json
s = '''{
        "error_code": "0,#要使用双引号，如果是单引号则运行时会报错，可以上网做在线json格式校验",
        "stu_info": [
                {
                        "id": 309,
                        "name": "小白",
                        "sex": "男",
                        "age": 28,
                        "addr": "河南省济源市北海大道32号",
                        "grade": "天蝎座",
                        "phone": "18512572946",
                        "gold": 100
                },
                {
                        "id": 310,
                        "name": "小白",
                        "sex": "男",
                        "age": 28,
                        "addr": "河南省济源市北海大道32号",
                        "grade": "天蝎座",
                        "phone": "18516572946",
                        "gold": 100
                }
        ]
}''' 
res=json.loads(s)                       #json转换成字典

print(res)                              #打印字典 

print(type(res))                        #打印res类型
for dict in res.get('stu_info'):        #字典类型可以用get方法取值
    print('-'*40)
    for key,value in dict.items():
        print(key,':',value) 
    