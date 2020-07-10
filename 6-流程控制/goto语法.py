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

@with_goto     #必须有
def test(list_):	
    tmp_list = list_
    label.begin		#标识跳转并开始执行的地方
    result = []
    try:
        for i, j in enumerate(list_):
            tmp = 1 / j
            result.append(tmp)
            last_right_i = i
    except ZeroDivisionError:
        del tmp_list[last_right_i + 1]
        goto.begin      #在有跳转标识的地方开始执行
    return result

if __main__ == 'main':
    a = test([1, 3, 4, 0, 6])
    print('%d',a)