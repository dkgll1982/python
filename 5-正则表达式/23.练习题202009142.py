#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: suixin
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2020-09-14 16:07:22
# @Remark: Life is short, I use python！
# 参考链接：https://www.cnblogs.com/guo-123/p/10745289.html
# 参考链接：https://www.jianshu.com/p/1067f3174ee1

import re
import json
import sys

index = 0

class Seq():
    def __init__(self):
        global index
        self.__index__ = index
        index += 1

    def __iter__(self):
        return self

    def __next__(self):
        self.__index__ += 1
        return self.__index__


# 1、中文处理之年份转换
m0 = '''在一九四九年新中国成立
       比一九九零年低百分之五点二
       人一九九六年击败俄军,取得实质独立'''
# 中文处理涉及到编码问题
result = re.findall(u"[\u96f6|\u4e00|\u4e8c|\u4e09|\u56db|\u4e94|\u516d|\u4e03|\u516b|\u4e5d]+\u5e74", m0)
print(f"{sys._getframe().f_lineno}行第{Seq().__next__()}题:{result}")

# 2、提取有效的python标识符集合
s = '_hello,python_1,2word,pra_ni,@dfa_,ewq*'
result = re.findall(r'\b[a-zA-Z_][\w]*(?!=\W)', s)
print(f"{sys._getframe().f_lineno}行第{Seq().__next__()}题:{result}")

s = '1.txt,2.vcd,4.rar'
# 3、定位：在\b的前边不是txt
result = re.findall(r'\d.(?!txt)\b', s)
print(f"{sys._getframe().f_lineno}行第{Seq().__next__()}题:{result}")

s = 'makesi masike limei hanmeimei liuyuting zhansan wangwu mlgb '
# 4、定位：匹配单词开头不为'm',负向断言不支持不定长表达式,要写匹配的单词长度，这是一个缺陷
result = re.findall(r'\w+(?<!\bm)\w{5}\s', s)
print(f"{sys._getframe().f_lineno}行第{Seq().__next__()}题:{result}")

# 5、匹配字符串s中的一些单词，这些单词不以’x’开头且不以’y’结尾
s = 'xaay xbbc accd xsdy'
result = re.findall(r'(?<!\bx)\w{3}(?!y\b)\w*', s)
print(f"{sys._getframe().f_lineno}行第{Seq().__next__()}题:{result}")

# 6、用正则表达式过滤掉英文和数字，最终输出"张三 深圳"
s = "not 404 found 张三 99 深圳"
chinese = '[\u4e00-\u9fa5]+'  # 中文字符的范围
result = re.findall(chinese, s)
print(result)

result = re.sub(r'[a-zA-Z0-9\s]', '', s)
print(f"{sys._getframe().f_lineno}行第{Seq().__next__()}题:{result}")

# 取字符串中合法的超链接地址
s = '<a href="http://www.gloryroad.cn">光荣之路官网</a>'
result = re.search(r'\w+://\w+.\w+.\w+',s).group()
print(f"{sys._getframe().f_lineno}行第{Seq().__next__()}题:{result}")

# 提取所有的手机号
s = '<table><tr>hello world 18111234589<tr><tr><span>name:张三,tel:18711001111</span></tr></table>'
result = re.findall(r'1[3-9]\d{9}',s,re.S)
print(f"{sys._getframe().f_lineno}行第{Seq().__next__()}题:{result}")
 