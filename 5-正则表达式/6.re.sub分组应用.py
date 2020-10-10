#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-12 23:40:50 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-12 23:40:50 
# @Software: vscode 

str  =  '''
String s1 = "学习java";
String s2 =   " ";
Float   价格 = 24000.89;
String desc  =   "用于找工作技能提升。。。" ;
Integer num   =    12567   ;

'''
#参考链接：https://blog.csdn.net/isscollege/article/details/80138158

import re,sys

#需求1，，分3组:<type>,<name>,<value>,求数据类型，变量名称，变量的值，下面3种求法，结果相同
s1 = re.findall(r'(?=String|Float|Integer)(?P<type>\w+)\s+(?P<name>.*?)\s*?=\s*?(?P<value>.*?)\s*?;',str,re.I|re.S)
print(sys._getframe().f_lineno,s1)           
#结果是：[('String', 's1', '"学习java"'), ('String', 's2', '  " "'), ('Float', '价格', '24000.89'), ('String', 'desc', '  "用于找工作技能提升。。。"'), ('Integer', 'num', '   12567')]
s1 = re.findall(r'(?P<type>String|Float|Integer\s+?\w+)\s+(?P<name>.*?)\s*? = \s*?(?P<value>["\d].*?)\s*?;',str,re.I|re.S)              
print(sys._getframe().f_lineno,s1)            
#结果是：[('String', 's1', '"学习java"'), ('String', 's2', '  " "'), ('Float', '价格', '24000.89'), ('String', 'desc', '  "用于找工作技能提升。。。"'), ('Integer', 'num', '   12567')]
#优化上面，当变量前面有空格时，要清除["\d],表示双引号或数字开头,匹配结果自动加入到<value>组，正则语法为：不消耗前缀
s1 = re.findall(r'(?=String|Float|Integer)(?P<type>\w+)\s+(?P<name>.*?)\s*?=\s*?(?=["\d])(?P<value>.*?)\s*?;',str,re.I|re.S);  #结果是：[('String', 's1', '"学习java"'), ('String', 's2', '" "'), ('Float', '价格', '24000.89'), ('String', 'desc', '"用于找工作技能提升。。。"'), ('Integer', 'num', '12567')]
print(sys._getframe().f_lineno,s1)           
#结果是：[('String', 's1', '"学习java"'), ('String', 's2', '" "'), ('Float', '价格', '24000.89'), ('String', 'desc', '"用于找工作技能提升。。。"'), ('Integer', 'num', '12567')]

#需求2，分2组:<name>,<value>，求变量名称，变量的值，
s1 = re.findall(r'\s+?(?P<name>\S+?)\s*? = \s*?(?P<value>["\d].*?)\s*?;',str,re.I|re.S)      
print(sys._getframe().f_lineno,s1)           
#结果是：[('s1', '"学习java"'), ('s2', '" "'), ('价格', '24000.89'), ('desc', '"用于找工作技能提升。。。"'), ('num', '12567')]

#需求3，分1组<value>,求每个变量的值，要清除首尾空格,给出2种求法
s1 = re.findall(r' = \s*?(?P<value>[\d"].*?)\s*?;',str,re.I|re.S) 
print(sys._getframe().f_lineno,s1)           
#结果是：['"学习java"', '" "', '24000.89', '"用于找工作技能提升。。。"', '12567']
s1 = re.findall(r'=\s*?(?=[\d"])(?P<value>.*?)\s*?;',str,re.I|re.S)
print(sys._getframe().f_lineno,s1)          
#结果是：['"学习java"', '" "', '24000.89', '"用于找工作技能提升。。。"', '12567']


#需求4，分1个<name>只取变量名称
s1 = re.findall(r'.*?\s+(?P<name>\w+?)\s*? = .*?;',str,re.I|re.S)
print(sys._getframe().f_lineno,s1)           
#结果是：['s1', 's2', '价格', 'desc', 'num']

