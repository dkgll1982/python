#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-09-12 12:03:42 
# @Remark: Life is short, I use python！
# 参考链接：https://www.cnblogs.com/zsvslx/p/10536893.html 
# 参考链接：https://blog.csdn.net/dnxbjyj/article/details/70946508
# 总结：真他妈的晦涩难懂，多敲吧，下次忘了还得重新敲~~~~~~~~~~~~~~~~~~~~~~~~

import re 

str1 = "fishc@abcch"
re1 = re.compile(r'(?=abc)abc')
print(re.findall(re1,str1))
re1 = re.compile(r'(?<=abc)ch')
print(re.findall(re1,str1))
re1 = re.compile(r'@(?=abc)abcch')
print(re.findall(re1,str1))

print('*'*40)

str2 = 'go go go'
rep1 = r'(?P<name>go)\s+(?P=name)\s+(?P=name)'
rep2 = r'(go)\s+\1\s+\1'
rep3 = r'(?P<name>go)\s+\1\s+\1'
print(re.search(rep1, str2).group(),',',re.search(rep1, str2).groups())
print(re.search(rep2, str2).group(),',',re.search(rep2, str2).groups())
print(re.search(rep3, str2).group(),',',re.search(rep3, str2).groups())

print('*'*40)

# 交换数字的位置
s = 'abc.xyz'
print(re.sub(r'(.*)\.(.*)', r'\2.\1', s))

s = '111-222-333-444-555-666'
print(re.sub(r'(\d+)\-(\d+)', r'\2-\1', s))

s = 'aaa.txt'
# 提取不是.txt结尾的文件
# 后边不匹配txt
print(re.findall(r'.*\..*$(?=txt$)',s)) 

print('*'*40)

A = 'doine done Sdo todo'
# 匹配以do结尾的单词
re2 = re.compile(r'\b\w+(?=do\b)')
print(re.findall(re2,A))
# 匹配以do开头的单词
re2 = re.compile(r'(?<=\bdo)\w+\b')
print(re.findall(re2,A))
# 匹配不以do结尾的单词,此处有雷
re2 = re.compile(r'\b\w+\W(?!do)')
print(re.findall(re2,A))