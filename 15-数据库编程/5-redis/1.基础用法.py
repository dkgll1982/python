#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2021-01-24 00:19:04 
# @Remark: Life is short, I use python！ 
# @Software: vscode 
# 参考链接1：https://blog.csdn.net/ljp1919/article/details/71022887
# 参考链接2：https://www.cnblogs.com/john-xiong/p/12089103.html

from redis import StrictRedis

# Redis的地址、运行端口、使用的数据库和密码信息。在默认不传的情况下，这4个参数分别为localhost、6379、0和None。首先声明了一个StrictRedis对象
r = StrictRedis(host='localhost', port=6379, db=0, password=None)
# 接下来调用set()方法，设置一个键值对，然后将其获取并打印。
r.set('name', 'Bob')
print(r.get('name'))
print(r.get('myKey'))

r.set('k1', 'v1')
r.set('k2', 'v2')
print(r.get('k1'))
print(r.keys())#打印当前所有的keys
print(r.dbsize())#查看当前有多少keys
r.delete('k2')#删除k2
print(r.keys())
print(r.dbsize())
print(dir(r))#查看redis对应的方法

'''
采用pipeline方式
一次性批量提交命令
'''
# #pipeline
p = r.pipeline()
p.set('k3', 'v3')
p.set('k4', 'v4')
p.set('V8', '法拉利的引擎')
p.incr('num')
p.incr('num')
p.execute()
print(r.get('num'))