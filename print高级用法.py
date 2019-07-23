#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-22 14:09
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : print高级用法
# @Software: PyCharm

#print() 函数的详细语法格式如下：
#print (value,...,sep='',end='\n',file=sys.stdout,flush=False)

user_name = 'Charlie'
user_age = 8
#同时输出多个变量和字符串
print("读者名：",user_name,"年龄：",user_age)
#同时输出多个变量和字符串，指定分隔符
print("读者名：",user_name,"年龄：",user_age,sep='|')
#如果格式化字符串中包含多个“%s”占位符，第三部分也应该对应地提供多个变量，并且使用圆括号将这些变量括起来：
print("读者名： %s 年龄： %s" %(user_name,user_age))

#设置end 参数，指定输出之后不再换行
print(40,'\t',end="");
print(50,'\t',end="");
print(60,'\t',end="");

f = open("C:\\Users\\dkgll\\Desktop\\python目录\\demo.txt","w")#打开文件以便写入
print('沧海月明珠有泪',file=f)
print('明月何时照我还',file=f)
print('蓝回日暖玉生烟',file=f)
f.close()