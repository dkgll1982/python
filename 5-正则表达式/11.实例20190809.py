#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-04 11:26:59 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-04 11:26:59 
# @Software: vscode 

import re
print(re.__all__)

m1 = re.match('www', 'www.fkit.org')# 开始位置可以匹配
print(m1.span())  # span返回匹配的位置
print(m1.group()) # group返回匹配的组
print(re.match('fkit', 'www.fkit.com')) # 开始位置匹配不到，返回None
m2 = re.search('www', 'www.fkit.org') # 开始位置可以匹配
print(m2.span())
print(m2.group())
m3 = re.search('fkit', 'www.fkit.com') # 中间位置可以匹配，返回Match对象
print(m3.span())
print(m3.group())

print('-'*40)

# 返回所有匹配pattern的子串组成的列表, 忽略大小写
print(re.findall('fkit', 'FkIt is very good , Fkit.org is my favorite' , re.I))
# 返回所有匹配pattern的子串组成的迭代器, 忽略大小写
it = re.finditer('fkit', 'FkIt is very good , Fkit.org is my favorite' , re.I)
for e in it:
    print(str(e.start()) + "-->" + e.group())

print('-'*40)

my_date = '2008-08-18'
# 将my_date字符串里中画线替换成斜线
print(re.sub(r'-', '/' , my_date))
# 将my_date字符串里中画线替换成斜线，只替换一次
print(re.sub(r'-', '/' , my_date, 1))

# 在匹配的字符串前后添加内容
def fun(matched):
    # matched就是匹配对象，通过该对象的group()方法可获取被匹配的字符串
    value = "《基础" + (matched.group('lang')) + "教程》"
    return value
s = 'Python很好，Kotlin也很好'
# 将s里面的英文单词（用re.A旗标控制）进行替换
# 使用fun函数指定替换的内容
print(re.sub(r'(?P<lang>\w+)', fun, s, flags=re.A))