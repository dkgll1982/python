#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: suixin
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2020-09-14 16:07:22
# @Remark: Life is short, I use python！ 
# 参考链接：https://www.jianshu.com/p/1067f3174ee1

import re
import json
import sys

# 匹配以下电话号码
partten = r'(\+?1?)?[ .-]?\(?([\d]{3})\)?[ .-]?([\d]{3})[ .-]?([\d]{4})' 
a =  re.search(partten,'2138675509')
b =  re.search(partten,'(213)8675509')
c =  re.search(partten,'213.867.5509')
d =  re.search(partten,'(213)-867-5509')
e =  re.search(partten,'1(213)867-5509')
f =  re.search(partten,'+1-213-867-5509')
print(a.groups(),'\t',a.group())
print(b.groups(),'\t',b.group())
print(c.groups(),'\t',c.group())
print(d.groups(),'\t',d.group())
print(e.groups(),'\t',e.group())
print(f.groups(),'\t',f.group())
 
print('*'*40)
 
b = re.sub(partten,r'\2\3\4','213-667-8890')
c = re.sub(partten,r'\2\3\4','(213)8675509')
d = re.sub(partten,r'\2\3\4','213.867.5509')
e = re.sub(partten,r'\2\3\4','+1-213-854-5557')                                                                                                                                                                                                                                                                                                                                                                                                                             
f = re.sub(partten,r'\2\3\4','1213-854-5557') 
print(b)
print(c)
print(d)
print(e)
print(f)

print('*'*40)

# 还可以利用sub的功能使所有的电话号码格式一致
partten = r'(\+?1?)[ .-]?\(?([\d]{3})\)?[ .-]?([\d]{3})[ .-]?([\d]{4})'
b = re.sub(partten,r'(\2)\3-\4','213-667-8890')
c = re.sub(partten,r'(\2)\3-\4','(213)8675509')
d = re.sub(partten,r'(\2)\3-\4','213.867.5509')
e = re.sub(partten,r'(\2)\3-\4','+1-213-854-5557')
f = re.sub(partten,r'(\2)\3-\4','1213-854-5557')
print(b)
print(c)
print(d)
print(e)
print(f)