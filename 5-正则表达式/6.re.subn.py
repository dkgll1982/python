#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-14 10:27:45 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-14 10:27:45 
# @Software: vscode 
import  re

p = re.compile( '(blue|white|red)')
# subn() 方法跟 sub() 方法干同样的勾当，但区别是返回值为一个包含有两个元素的元组：一个是替换后的字符串，一个是替换的数目。
s = p.subn('color','blue shine red book white board')
print(s)

s = p.sub('color','blue shine red book white board')
print(s)

# 1.开启re.VERBOSE，空格将被忽略。因为这里一堆符号，用空格隔开看着才不会乱糟糟的......
# 2.这里r'subsection{\1}' 使用 \1 引用匹配模式中的 ([^}]*) 匹配的字符串内容。
p = re.compile('section{(?P<GroupName>[^}]*)}', re.X)
# 使用Python 的扩展语法 (?P<name>...) 指定命名组，引用命名组的语法是 \g<name>
# 另外，\g<数字>是通过组的序号进行引用。\g<2> 其实就相当于\2，但我们更提倡使用 \g<2>，因为这样可以避免歧义
s = p.subn(r'subsection{\g<GroupName>}','section{er}First} section{second}')
print(s)