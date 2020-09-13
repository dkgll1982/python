#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-09-12 12:03:42 
# @Remark: Life is short, I use python！
# 参考链接：https://www.cnblogs.com/zsvslx/p/10536893.html 
# 参考链接：https://blog.csdn.net/dnxbjyj/article/details/70946508
# 总结：真他嘛的晦涩难懂，多敲把，下次忘了害得重新敲~~~~~~~~~~~~~~~~~~~~~~~~

import re 

str1 = "fishc@abcch"
re1 = re.compile(r'(?=abc)abc')
print(re.findall(re1,str1))
re1 = re.compile(r'(?<=abc)ch')
print(re.findall(re1,str1))
re1 = re.compile(r'@(?=abc)abcch')
print(re.findall(re1,str1))