#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: suixin
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2020-09-14 16:07:22
# @Remark: Life is short, I use python！

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


# 1、匹配一行文字中的所有开头的字母内容
s = "i love you not because of who you are, but because of who i am when i am with you"
result = re.findall(r"\b\w", s)
print(f"{sys._getframe().f_lineno}行第{Seq().__next__()}题:{result}")

# 2、匹配一行文字中的所有开头的数字内容
s = "i love you not because 12sd 34er 56df e4 54434"
result = re.findall(r"\b\d{1,3}", s)
print(f"{sys._getframe().f_lineno}行第{Seq().__next__()}题:{result}")

# 3、只匹配包含字母和数字的行
s = "i love you not because\n12sd 34er 56\ndf e4 54434"
result = re.findall(r"\w+\b", s, re.M)
print(f"{sys._getframe().f_lineno}行第{Seq().__next__()}题:{result}")

# 4、提取每行中完整的年月日和时间字段
s = """se234 1987-02-09 07:30:00

    1987-02-10 07:25:00"""
result = re.findall(r'\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}', s, re.M)
print(f"{sys._getframe().f_lineno}行第{Seq().__next__()}题:{result}")

# 5、将每行中的电子邮件地址替换为你自己的电子邮件地址
s = """693152032@qq.com, werksdf@163.com, sdf@sina.com

    sfjsdf@139.com, soifsdfj@134.com

    pwoeir423@123.com"""
result = re.sub('\w+@\w+.com','350606539@qq.com',s)
print(f"{sys._getframe().f_lineno}行第{Seq().__next__()}题:{result}")

# 6、匹配关键字
s = "skjdfoijower \home   \homewer"
result = re.findall(r'(?=home)\w+\b',s)
print(f"{sys._getframe().f_lineno}行第{Seq().__next__()}题:{result}")

# 7、使用正则提取出字符串中的单词(边界是)
# \b，\B是单词边界，不匹配任何实际字符，所以是看不到的；\B是\b的非(补)。
# \b：表示字母数字与非字母数字的边界，非字母数字与字母数字的边界。
# \B：表示字母数字与(非非)字母数字的边界，非字母数字与非字母数字的边界
s = """i love you not because of who 234 you are, 234 but 3234ser because of who i am when i am with you"""
result = re.findall(r'\b[a-zA-Z]+\b',s)
print(f"{sys._getframe().f_lineno}行第{Seq().__next__()}题:{result}")

# 8、使用正则表达式匹配合法的邮件地址：
s = """xiasd@163.com, sdlfkj@.com sdflkj@180.com solodfdsf@123.com sdlfjxiaori@139.com saldkfj.com oisdfo@.sodf.com.com"""
result = re.findall(r'\w+@\w+.com',s)
print(f"{sys._getframe().f_lineno}行第{Seq().__next__()}题:{result}")


 
 