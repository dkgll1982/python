import re

# findall函数返回的总是正则表达式在字符串中所有匹配结果的列表，

# 此处主要讨论列表中“结果”的展现方式，即findall中返回列表中每个元素包含的信息。
# 1.当给出的正则表达式中带有多个括号时，列表的元素为多个字符串组成的tuple，
#   tuple中字符串个数与括号对数相同，字符串内容与每个括号内的正则表达式相对应，并且排放顺序是按括号出现的顺序。

# 2.当给出的正则表达式中带有一个括号时，列表的元素为字符串，
#   此字符串的内容与括号中的正则表达式相对应（不是整个正则表达式的匹配内容）。

# 3.当给出的正则表达式中不带括号时，列表的元素为字符串，
#   此字符串为整个正则表达式匹配的内容。

# 示例4：[...]匹配括号中的其中一个字符 

# 示例参考：https://www.cnblogs.com/4wheel/p/8497121.html

s = 'qew rty uio pas dfg hjk lzx cvb nm' 
print(0,re.findall('(\w+\s+\w+)\s+\w+',s))           
print(1,re.findall('\w+\s+\w+',s))                          
print(2,re.findall('(\w+)\s+\w+',s)) 
print(3,re.findall('((\w+)\s+\w+)',s))
print(4,re.findall('(\s+\w+)',s))
print(0,re.findall('\w+\w+\s+\w+\s+\w+',s))
print(1,re.findall('\w+\w+\s+\w+','qew rty uio'))
print(2,re.findall('\w+(\w+)\s+\w+','qew rty'))
print(3,re.findall('\w+\w+\s+\w+(\s+\w+)','qew rty uio'))

print('-'*40)
print(re.findall('((\w+)\w+\s+\w+)(\w+)',s))  
print(re.findall('\w+\w+\s+\w+\w+',s))   
#[('qew rt','qe','y'), ('uio pa','ui','s'),('dfg hj','df','k'),('lzx cv','lz','b')]
print(re.findall('(\w+(\s+)\w+)(\w+)',s)) 
#[('qew rt',' ','y'),('uio pa',' ','s'),('dfg hj',' ','k'),('lzx cv',' ','b')]
print('-'*40)
#可以发现是否将整个正则表达式用括号括起来会影响findall的返回结果。

#如果有括号括，则返回元组的第0项是匹配到的整个字符串’abcde’
#如果没有，则返回元组的第0项就是第一对括号’bc’
#并且当存在多层括号嵌套时，各组的排序遵循从左到右，从外到内的原则。
# 即对于正则表达式(a(bc)((d)(e)))，'abcde’是第0组，'bc’是第1组，'de’是第2组，'d’是第3组，而’e’则是第4组。
#原文链接：https://blog.csdn.net/qq_32925781/article/details/83315468
print(re.findall(r'(a(bc)((d)(e)))','abcde'))
print(re.findall(r'a(bc)((d)(e))','abcde'))

print('-'*40)

print(re.findall(r'(^(\d{3})+)','1234567'))
print(re.findall(r'((\d{3})+$)','1234567'))
print(re.findall(r'(?=(\d{3})+$)','1234567'))

print(re.findall(r'((\w+)(\w+)(\w+))','sdsfdd fdsdsfd')) 
print(re.findall(r'((\w+?)(\w+)(\w+))','sdsfdd fdsdsfd')) 
print(re.findall(r'(\w+)','sdsfdd fdsdsfd')) 
print(re.findall(r'(\w+?)','sdsfdd fdsdsfd')) 