#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-09-12 12:03:42 
# @Remark: Life is short, I use python！
# 参考链接：https://www.cnblogs.com/zsvslx/p/10536893.html 
# 参考链接：https://blog.csdn.net/dnxbjyj/article/details/70946508
# 总结：真他嘛的晦涩难懂，多敲吧，下次忘了还得重新敲~~~~~~~~~~~~~~~~~~~~~~~~

import re 


strTest = "123456789 , 987654321"  

# 此位置后面匹配表达式exp，这个位置不是字符（因此匹配返回无结果），仅仅是一个位置
# 下边的例子，后边的位置是5，5的前边是34
re1 = re.compile(r"\d{2}(?=5)\d{2}")         #3456,7654
# 此位置前面匹配表达式exp
# 下边的例子，前边的位置是5，5的后边是67
re2 = re.compile(r"\d{2}(?<=5)\d{2}")        #4567,6543   
print(re.findall(re1,strTest))
print(re.findall(re2,strTest))     
    
re1 = re.compile(r"(?=5)\d{2}")             #56,54
print(re.findall(re1,strTest))

re2 = re.compile(r"(?<=5)\d{2}")            #67,43
print(re.findall(re2,strTest))

strTest = "aeaa1141aaa , 3bbb222&, 333ccc"  

re1 = re.compile(r"\d{1}(?=[a-zA-Z])[a-zA-Z]+")     #右边匹配表达式
re2 = re.compile(r"\D{1}(?<=[a-zA-Z])\d+")          #左边匹配表达式
print(re.findall(re1,strTest))
print(re.findall(re2,strTest))         
print(re.findall(r'(?=abc)\D+',"fishc@abcch"))

print('*'*40)

strTest = "111aaa222,333bbb444,555cc666"
re1 = re.compile(r"\d{1}(?=[a-zA-Z]{3})[a-zA-Z]+")     
re2 = re.compile(r"\d{1}(?<=[a-zA-Z]{3})\d+")       
print(re.findall(re1,strTest))
print(re.findall(re2,strTest))         
  
str1 = "123,456,789"
# 匹配以逗号间隔的数字(再次强调，不包括这些逗号)。
# 左边？表示可以是0个或1个逗号，右边？也表示可以是0个或1个逗号
re1 = re.compile(r"(?<=,)?(\d+)(?=,)?")
print(re.findall(re1,str1)) 

print('*'*40)

str1 = "<span> hello world </span> <a>eeeee</a>"
# look-behind requires fixed-width pattern,只能指定固定长度的字符，不能有不确定长度的表达式
# 因此匹配可以为\d{m},不能为\d+的形式
re1 = re.compile(r"(?<=<(?P<name>\w{4})>)(.*)(?=</\1>)")
print(re.findall(re1,str1)) 
