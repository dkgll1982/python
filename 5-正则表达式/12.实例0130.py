#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-01-30 11:49:21 
# @Last Modified by: guojun 
# @Last Modified time: 2020-01-30 11:49:21 
# @Software: vscode 

import re

print(re.match(r".","my.name|is guojun"))
print(re.match(r".*g","my.name|is guojun"))

#数量词(*,+,?,{m},{m,n}默认是贪婪匹配的，即匹配尽可能多的字符
print(re.match(r".*","my.name|is guojun"))
print(re.match(r".+","my.name|is guojun"))
print(re.match(r".?","my.name|is guojun"))
print(re.match(r".{2}","my.name|is guojun"))
print(re.match(r".{2,}","my.name|is guojun"))
print(re.match(r".{,2}","my.name|is guojun"))
print(re.match(".*(\\bgood\\b).*","today is a good daytoday is a good day").groups())
      
print( re.match("[^\s]+","this is good day"))   
print( re.match("^t","this is good day"))    
print( re.match("\d+","10086"))     
print( re.match("[\d]","10086")) 

print(re.match('.*?(?=\d).*?$','11d'))  
print(re.match('^.*(?<=\d).*$','11d1'))  
print(re.match('(db)+','dbdbms'))
print(re.match('(db)?','dbdbms'))
print(re.match('(db)*','dbdbms'))
print(re.match('(a(b)c)d','abcd').groups())

print(re.findall("[^ ]+", "a little boy")) #[^abc] --> 除a b c之外任意字符
#search()函数会在整个字符串内查找模式匹配,只到找到第一个匹配然后返回一个包含匹配信息的对象,
print(re.search(r"(https|http|ftp)://\S+"," https://www.baidu.com"))
#match()函数只检测字符串开头位置是否匹配，匹配成功才会返回结果，否则返回None
print(re.match(r"(https|http|ftp)://\S+"," https://www.baidu.com"))
print(re.search(r"(?P<dog>ab)cdef",'abcdefghti').group('dog'))