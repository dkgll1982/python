#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2021-01-24 00:19:04 
# @Remark: Life is short, I use python！ 
# @Software: vscode 
# 参考链接：https://blog.csdn.net/ljp1919/article/details/71022887

from redis import StrictRedis

# Redis的地址、运行端口、使用的数据库和密码信息。在默认不传的情况下，这4个参数分别为localhost、6379、0和None。首先声明了一个StrictRedis对象
r = StrictRedis(host='localhost', port=6379, db=0, password=None)

print(f'当前数据库的键数量：{r.dbsize()}')
for index,x in enumerate(range(10),start=1):
    key = r.randomkey()
    #获取键的过期时间，单位为秒，-1表示永久不过期
    ttl = r.ttl(key)
    print(f'随机键：{index},{key},该键的过期时间：{ttl}')
 
key = '会过期的键'
r.set(key, '观察下是否会过期', ex=1000)
print(f'{key}:该键的过期时间：{r.ttl(key)}')

# 给数据库中键为name的string赋予值value并返回上次的value
print(f'{key}:更改之前的值为"{r.getset(key, "Mike").decode()}"更改之后的值为"{r.get(key).decode()}"')

# 同时返回多个键的值
print(r.mget(['k1', 'k3','name',key]))