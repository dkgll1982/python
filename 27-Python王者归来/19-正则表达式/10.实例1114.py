#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-14 13:58:57 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-14 13:58:57 
# @Software: vscode 

import re
string1 = 'XXX高考的时间是2018年6月7日'
string2 = 'XXX高考的时间是2018/6/7'
string3 = 'XXX高考的时间是2018-6-7'
string4 = 'XXX高考的时间是2018-06'
string5 = 'XXX高考的时间是2018年6月'
string6 = 'XXX高考的时间是2018-11-07' 

regex_str = '.*高考的时间是(\d{4}[年/-](0?[1-9]|1[0-2])([月/-]\d{1,2}(日|$)|[月/-]|$))'
print(re.findall(regex_str,string1))
print(re.findall(regex_str,string2))
print(re.findall(regex_str,string3))
print(re.findall(regex_str,string4))
print(re.findall(regex_str,string5))
print(re.findall(regex_str,string6))

print('\n--简单的验证','*'*40,sep='',end='\n'*2) 
pattern = r"qq:[1-9]\d{4,10}" 
print(re.findall(pattern,'qq:11111111',re.I))
pattern = r"^1[3-9]\d{9}$"
print(re.findall(pattern,'13211111111',re.I))
#找出字母g后面的字母不是u
print(re.findall('.*g[^u].*','cgoogle',re.I))
print(re.findall('.*g[^u].*','glup',re.I))
print(re.findall('.*g[^u].*','dfgulp',re.I))