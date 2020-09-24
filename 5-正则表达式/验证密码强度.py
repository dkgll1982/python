#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: suixin
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2020-09-14 16:07:22
# @Remark: Life is short, I use python！
# 参考链接：https://www.cnblogs.com/guo-123/p/10745289.html

import re
import json
import sys

"""
密码长度大于或等于8位数
强：字母+数字+特殊字符
中：字母+数字，字母+特殊字符，数字+特殊字符
弱：纯数字，纯字母，纯特殊字符
"""

def checklen(pwd):
    if len(pwd)>=8:
        return True
    else:
        return False

def is_strong_pwd(pwd):
    pattern=re.compile(r"^(?![a-zA-z]+$)(?!\d+$)(?![!@#$%^&*]+$)(?![a-zA-z\d]+$)(?![a-zA-z!@#$%^&*]+$)(?![\d!@#$%^&*]+$)[a-zA-Z\d!@#$%^&*]+$")
    result=pattern.findall(pwd)
    if result:
        return True
    else:
        return False

def is_inter_pwd(pwd):
    pattern=re.compile(r"^(?![a-zA-z]+$)(?!\d+$)(?![!@#$%^&*]+$)[a-zA-Z\d!@#$%^&*]+$")
    result=pattern.findall(pwd)
    if result:
        return True
    else:
        return False

def is_weak_pwd(pwd):
    pattern=re.compile(r"^(?:\d+|[a-zA-Z]+|[!@#$%^&*]+)$")
    result=pattern.findall(pwd)
    if result:
        return True
    else:
        return False

def checkpassword(pwd):

    #判断密码长度是否合法
    lenOK=checklen(pwd)

    #判断是否强：字母+数字+特殊字符
    strongOK=is_strong_pwd(pwd)

    #判断是否中：字母+数字，字母+特殊字符，数字+特殊字符
    interOK=is_inter_pwd(pwd)

    #判断是否弱：纯数字，纯字母，纯特殊字符
    weakOK=is_weak_pwd(pwd)

    print(lenOK)
    print(strongOK)
    print(interOK)
    print(weakOK)
    if lenOK:
        if strongOK:
            print("密码的强度为强的！")
        elif interOK:
            print("密码的强度为中的！")
        elif weakOK:
            print("密码的强度为弱的，建议修改！")
    else:
        print("密码长度不合格！")
        

checkpassword("Helloworld#123")
checkpassword("Hel333323")
checkpassword("thdkl&99")