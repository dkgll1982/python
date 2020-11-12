#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-10-10 18:03:52 
# @Remark: Life is short, I use python！
# 参考链接：https://blog.csdn.net/qq_36883141/article/details/90079894

import re

str1 = '语文 数学 英语 物理 化学 生物 政治 历史 地理 美术 音乐 体育'

def func(str0): 
    return '['+str0.group(1)+']'

str2 = re.sub(r'\s+(\w+)',func,str1)
print(str2)