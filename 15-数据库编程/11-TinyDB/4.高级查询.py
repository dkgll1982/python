#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-07-13 14:04:51 
# @Remark: 人生苦短，我用python！
# 参考链接：https://www.cnblogs.com/watalo/p/12388046.html

from tinydb import TinyDB,Query,where
import sys
import os 
import re

# 获取文件当前所在的目录，并返回完整文件全路径 
def realpath(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

db = TinyDB(realpath('db3.json'))
student = db.table("student")
User = Query()

#判断是否存在 exist(...) ，返回对于字段列表（filed）
print(student.search(User.name.exists()))
print(student.search(User.name.first_name.exists()))

#正则表达式判断 matches(...) 
i = student.search(~(User.name.matches('[aZ]*')))
print(i)
i = student.search((User.name.matches('[aZ]*')))
print(i)

j = student.search(User.name.matches('Tom', flags=re.I))
print(j)

print('-'*40)

#正则嵌套
student.insert({'中国':'湖北省','武汉':{'继续':'加油'}})
l = student.search(User.中国.matches('湖北', flags=re.IGNORECASE))
l_1 = student.search(User.中国.matches('湖', flags=re.IGNORECASE))
l_2 = student.search(User.中国.matches('北', flags=re.IGNORECASE))
# value也是字典的话，只能嵌套查询
m = student.search(User.武汉.matches('加油', flags=re.IGNORECASE)) 
n = student.search(User.武汉.继续.matches('加', flags=re.IGNORECASE))
print(l)    #[{'中国': '湖北省', '武汉': {'继续': '加油'}}]
print(l_1)  #[{'中国': '湖北省', '武汉': {'继续': '加油'}}]
print(l_2)  # []
print(m)    # []
print(n)    # [{'中国': '湖北省', '武汉': {'继续': '加油'}}]