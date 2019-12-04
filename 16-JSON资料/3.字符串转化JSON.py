import json

dicts = {
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
}
# json.dumps 进行序列化时，默认使用ascii编码， print json.dumps(dic)输出unicode编码的结果： {"a": "\u4e2d\u56fd"}
# json.dumps(dic,ensure_ascii=False)，不使用ascii编码，输出结果为：{"a": "中国"}
# 参考链接：https://www.cnblogs.com/shiju/p/9511916.html
json_dicts = json.dumps(dicts, indent=4, ensure_ascii=False)
print(json_dicts)

with open(r'C:\Users\dkgll\Desktop\python目录\stus.txt', 'w') as f:  # 打开文件
    f.write(json_dicts)  # 在文件里写入转成的json串

stus = {'xiaojun': '123456', 'xiaohei': '7890', 'lrx': '111111'}
f = open(r'C:\Users\dkgll\Desktop\python目录\stus.txt', 'w', encoding='utf-8')
#indent：应该是一个非负的整型，如果是0，或者为空，则一行显示数据，
# 否则会换行且按照indent的数量显示前面的空白，这样打印出来的json数据也叫pretty-printed json
json.dump(stus, f, indent=4, ensure_ascii=False)
