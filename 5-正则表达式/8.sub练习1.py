#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-09-13 17:12:11 
# @Remark: Life is short, I use python！
# Python正则表达式：https://www.92python.com/view/441.html

import re

str1 = 'i say, hello world!'
rep = re.compile(r'(\w+) (\w+)')
print(rep.sub(r'\2 \1',str1))
print(re.sub(rep,r'\2 \1',str1))

def func(m):
    print('==0:{},1:{},2:{},3:{}>'.format(type(m.group()),m.group(),m.group(1),m.group(2)))
    # title()方法返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())。
    # 当repl是一个方法时，这个方法应当只接受一个参数（Match对象），并返回一个字符串用于替换（返回的字符串中不能再引用分组）。
    # 作用是把字符串对象内的每个单词的首字母变成大写。
    # print('Tsddddd'.istitle())
    return m.group(1).title() + ' ' + m.group(2).title()

print(rep.sub(func, str1))

print('*'*40)

# sub()和subn()。两者几乎一样，都是将某字符串中所有匹配正则表达式的部分进行某种形式的替换。
# 用来替换的部分通常是一个字符串，但它也可能是一个函数，该函数返回一个用来替换的字符串。
# subn()和 sub()一样，但subn()还返回一个表示替换的总数，替换后的字符串和表示替换总数的数字一起作为一个拥有两个元素的元组返回。
print(re.sub('X', 'Mr.Guan', 'attn: X\n\nDear X,\n'))
print(re.subn('X', 'Mr.Guan', 'attn: X\n\nDear X,\n'))
print(re.sub('X', 'Mr.Guan', 'attn: X\n\nDear X,\n'))
print(re.sub('[ae]', 'X', 'abcdef'))
print(re.subn('[ae]', 'X', 'abcdef'))

print('*'*40)

def f(m):
    return str(2*int(m.group()))

print(re.sub('\d+',f,'df12sd34f34fg51s'))

def normalize_orders(matchobj):
    print(matchobj)
    if matchobj.group(1) == '-':
        return "A"
    else: 
        return "B"
    
print(re.sub('([-|A-Z])', normalize_orders, '-1234, A193, B123, C124')) #A1234, B193, B123, B124

# 将匹配的数字乘以 2
def double(matched):
    print('matched: ',matched)
    print("matched.group('value'): ",matched.group('value'))
    value = int(matched.group('value'))
    return str(value * 2)
 
string = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, string))