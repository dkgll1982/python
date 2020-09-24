#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-09-14 21:55:45 
# @Remark: Life is short, I use python！

import re

#第一题
# 1.提取所有 11 位数字电话号码
# 2.提取所有 18 或 13 开头的电话号码
# 3.提取所有“王”姓同学的名字
# 4.提取所有“张”姓同学的电话号码
# 5.重新排版，排版成统一的格式，去掉国家区号。

str = """
    张伟 86-14870293148  \n
   王伟   +86-13285654569    \n
    王芳        15856529115    \n
 李伟         13022816340  \n
  王秀英   (86)14785720656     \n
   李秀英    17201444672    \n
    李娜         15682812452     \n
    张秀英         14326967740     \n
    刘伟  15146435743    \n
   张敏        (86)-17712576838   \n
    李静       86 14295083635  \n
    张丽     (+86) 13722348123   \n
   王静         17587918887   \n
  王丽    15493106739    \n
 李强      13786842977   \n
 张静         86-15542304386     \n
    李敏        15642387356 \n
   王敏          18627216756  \n
 王磊       17206185726   \n
    李军      17857426238     \n
   刘洋        17345352790     \n
"""

a = re.findall(r'[\d]{11}',str)
b = re.findall(r'1[8|3][\d]{9}',str)
c = re.findall(r'王\S*',str)

d = re.findall(r'(张\S*)\s+\(?(\+?86?)?\)?[ .-]?([\d]{11})',str)
e = re.sub(r'\s+(\w\S+)\s+\(?(\+?86?)?\)?[ .-]?([\d]{11})',r'\1  \3\n',str)

print(a)
print(b)
print(c)
for line in d:
    print(line[0] + "的电话号码是：" + line[2])

print(e)

print('-----------------------------------------------------------\n')

#第二题
# 提取所有日期
# 提取所有 1996 年以前出生的学生
# 重新排版
# 把所有 1996 年以前出生的学生出生年份改为 1996
# 提取生日 格式：张伟的生日是11月15号 
a = re.findall(r'\d{4}[年.-]?\d{1,2}[月.-]?\d{1,2}\S?',str)  # 提取所有日期
b = re.findall(r'\S+\s+1\d{2}[0-5][年.-]?\d{1,2}[月.-]?\d{1,2}\S?',str)  # 提取所有 1996 年以前出生的学生
c = re.sub(r'\s*(\S+)\s+(\d{4})[年.-]?(\d{1,2})[月.-]?(\d{1,2})\S?',r'\1  \2 年 \3 月 \4 日 \n',str)   #重新排版
d = re.findall(r'(\S+)\s+(1\d{2}[0-6])\S?(\d{1,2})\S?(\d{1,2})\S?',str)
e = re.findall(r'(\S+)\s+\d{4}[年.-]?(\d{1,2})\S?(\d{1,2})\S?',str)

print(a)  
print("\n")
print(b)
print("\n")
print(c)
for line in d:
    print(line[0] + "  " + "1996" + "年" + line[2] + "月" + line[3] + "日" )

print(e)