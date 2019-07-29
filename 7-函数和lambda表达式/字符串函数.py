#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-23 14:52
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 字符串函数
# @Software: PyCharm

s1 = "这是数字: "
p = 99.8
#字符串直接拼接数值，程序报错
##print(s1 + p)
#使用str()将数值转换成字符串
print(s1 + str(p))
#使用repr()将数值转换成字符串
print(s1 + repr(p))

s = 'crazyit.org is very good'
# 获取s中从索引3处到索引5处（不包含）的子串
print(s[3: 5]) # 输出 zy
# 获取s中从索引3处到倒数第5个字符的子串
print(s[3: -5]) # 输出 zyit.org is very
# 获取s中从倒数第6个字符到倒数第3个字符的子串
print(s[::-1]) # 输出 doog yrev si gro.tiyza
print("".join(reversed(s)))
#每隔 1 个，取一个字符
print(s[::2]) # 输出 caytogi eygo

str = "C语言中文网  c.biancheng.net mycro soft Amercia"
#sep：用于指定分隔符，可以包含多个字符。此参数默认为 None，表示所有空字符，包括空格、换行符“\n”、制表符“\t”等。
list =s.split();

print(list)
list4 = str.split(' ')
list5 = str.split(' ',4)
print(list4)
print(list5)

dir = '','usr','bin','env'
s5 = ''.join(str);
s3 = '/'.join(dir);
print(s5)
print(s3)

#str.find(sub[,start[,end]])
str = "c.biancheng.net"
fi = str.find('.',1)
rfi = str.rfind('.',1)
#同 find() 方法类似，index() 方法也可以用于检索是否包含指定的字符串，不同之处在于，当指定的字符串不存在时，index() 方法会抛出异常
#str.index(sub[,start[,end]])
i = str.index('.',1)
ri = str.rindex('.',1)
print("\".\"在字符串\"%s\"第一次出现的位置:%d"%(str,fi))
print("\".\"在字符串\"%s\"第一次出现的位置:%d"%(str,rfi))
print('---------------------------------')
print("\".\"在字符串\"%s\"第一次出现的位置:%d"%(str,i))
print("\".\"在字符串\"%s\"第一次出现的位置:%d"%(str,ri))

print(s.title())

str = "  c.biancheng.net \t\n\r"
print(str.strip())
print(str)
print('--------------------------------------')

str='中华人民共和国';
str2=str.encode();
str3= str.encode("GBK")
print(str3)
print(str3.decode("GBK"))
print(help(print))

