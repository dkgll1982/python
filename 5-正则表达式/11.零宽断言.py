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

#查询url是否以http://www.开头
s1=re.findall(r'(?=http:\/\/www\.)(?P<name>.*)','http://www.baidu.com') #结果是：['http://www.baidu.com']
print(s1)
s1=re.findall(r'(?<=http:\/\/www\.)(?P<name>.*)','http://www.baidu.com') #结果是：['baidu.com']
print(s1)
s1=re.findall(r'(?=http:\/\/www\.)(?P<name>.*)','https://www.baidu.com') #结果是：[]
print(s1)

atr = '<div>hello world</div>'
s2 = re.findall('<div>.*(?=ld)',atr)
print(s2)
s2 = re.findall('.*(?=world)',atr)
print(s2)
s2 = re.findall('(?=he).*(?<=ld)',atr)
print(28,s2)
s2 = re.findall('(?<=he).*(?=ld)',atr)
print(s2)
s2 = re.findall('(?=he)(\w+)',atr)
print(s2)

s = 'doing done do todo'
result = re.findall(r'(?<=\bdo)\w+\b',s)    #它断言此位置的前面能匹配表达式exp；
print('=======>',result)
result = re.findall(r'\w(?=o)',s)           #它断言此位置的后面能匹配表达式exp,但不包含此位置；    
print('=======>',result)

s1 = '''
String s1="学习java";
String s2=  " ";
Float   价格=24000.89;
String desc =  "用于找工作技能提升。。。" ;
Double price = 323.232;
Integer num  =   12567   ;

'''  
p1 = re.findall(r'(?=String|String|Float|String|Double|Integer)(?P<type>\w+)',s1,re.I|re.S); 
print('+++++++++++>',p1)

s = "I'm singing while you're dancing."
p = re.findall('[s].*?',s)
print(p)
# 匹配出字符串s中以ing结尾的单词
p = re.findall(r'\w+(?=ing\b)',s) 
print('以ing结尾的单词:',p)
# 匹配出字符串s中含有i的单词
p = re.findall(r'\b\w+(?<=i)\w+\b',s) 
print('s中含有i的单词:',p)
# 匹配出字符串s中不以ing结尾的单词
p = re.findall(r'\b\w{3,5}(?!ing\b)',s) 
print('不以ing结尾的单词:',p) 