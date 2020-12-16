#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-12-11 11:09:22 
# @Remark: Life is short, I use python！

import re
import requests
import os,sys,time

#使用步骤： 
#1：先将正则表达式的字符串形式编译为Pattern实例，
#2：然后使用Pattern实例处理文本并获得匹配结果（一个Match实例），
#3：最后使用Match实例获得信息，进行其他的操作。

#将正则表达式编译成pattern对象
pattern = re.compile(r'hello')

#从最开始匹配，如果匹配到，则返回符合MatchObject对象，否则返回None.
# 1.re.match("", string)可以匹配任意字符串
# 2.在多行模式下，只匹配第一行开头的的，而不会匹配每一行的开头
match1 = re.match(pattern,'hello world!')
#获取使用pattern实例匹配文本，获得匹配结果，无法匹配时返回None
match2 = pattern.match('hello world!')

print(match1.group(),match2.group())

m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
print("m.string:", m.string)
print("m.re:", m.re)
print("m.pos:", m.pos)
print("m.endpos:", m.endpos)
print("m.lastindex:", m.lastindex)
print("m.lastgroup:", m.lastgroup)
 
print("m.group(1,2):", m.group(1, 2))
print("m.groups():", m.groups())
print("m.groupdict():", m.groupdict())
print("m.start(2):", m.start(2))        #返回指定的组截获的子串在string中的起始索引（子串第一个字符的索引）。group默认值为0。
print("m.end(2):", m.end(2))            #返回指定的组截获的子串在string中的结束索引（子串最后一个字符的索引+1）。group默认值为0。
print("m.span(2):", m.span(2))          #返回(start(group), end(group))。
print(r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3'))
print('-'*40)

match3 = re.search(pattern,'hello world!hello')
print(match3)
match4 = re.findall(pattern,'hello world!hello')
print(match4)

