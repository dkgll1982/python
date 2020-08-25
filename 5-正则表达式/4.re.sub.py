#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-12 14:32:13 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-12 14:32:13 
# @Software: vscode  

import re

#re.sub(pattern, repl, string, count=0, flags=0)
#其中三个必选参数：pattern, repl, string
#两个可选参数：count, flags

#第一个参数：pattern
# 反斜杠加数字（\N），则对应着匹配的组（matched group）
# 比如\6，表示匹配前面pattern中的第6个group

def dashrepl(matchobj):
    print(matchobj.group('groupName'))
    if matchobj.group('groupName') == '-': 
        return ' '
    else: return '-'


print(re.sub('(?P<groupName>-{1,2})', dashrepl, 'pro----gram-files'))

inputStr = "hello 123 world 456";
#分组定义是(?P<自定义分组名称>正则字符串)
print('替换结果:',re.sub("(?P<number>\d+)", '222', inputStr))

inputStr = "hello crifan, nihao crifan";
patten = re.compile(r"hello (\w+), nihao \1")
print(patten.match(inputStr))

replacedStr = re.sub(patten, "crifanli", inputStr);
print(replacedStr)
print( re.sub("\d+", "222",  "hello 123 world 456"))

#检索和替换
phone = "2004-959-559 # 这是一个电话号码"
 
# 删除注释
num = re.sub(r'#.*$', "", phone)
# re.search匹配整个字符串， 直到找到一个匹配，如果整个字符串都没匹配到，则返回None
print('查询匹配 :',re.search(r'#.*$',phone))
print("电话号码 :[%s]"%num)
 
# 移除非数字的内容
num2 = re.sub(r'\D', "", num)
print('查询匹配 :',re.findall(r'\D',num))
print("电话号码 :[%s]"%num2)

# 只处理部分匹配字符
# 参考链接：https://www.cnblogs.com/telwanggs/p/10410557.html
def pythonReSubDemo():
    """
        demo Pyton re.sub
    """
    inputStr = "hello 123 world 456 nihao 789";

    def _add111(matched):
        intStr = matched.group("number"); #123
        intValue = int(intStr);
        addedValue = intValue + 111; #234
        addedValueStr = str(addedValue);
        return addedValueStr;

    replacedStr = re.sub("(?P<number>\d+)", _add111, inputStr, 2);
    print("replacedStr=",replacedStr); #hello 234 world 567 nihao 789 

pythonReSubDemo()
