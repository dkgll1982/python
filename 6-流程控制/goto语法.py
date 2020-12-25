#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-07-09 15:54:32 
# @Remark: 人生苦短，我用python！
#goto语法：https://blog.csdn.net/C_chuxin/article/details/83687064/
# Python 2.6 through 3.6 and PyPy,not support in 3.8

from goto import with_goto 

@with_goto
def range(start, stop):
    i = start
    result = []

    label .begin
    if i == stop:
        goto .end

    result.append(i)
    i += 1
    goto .begin

    label .end
    return result

if __main__ == 'main':
    a = range([1, 13])
    print('%s',a)