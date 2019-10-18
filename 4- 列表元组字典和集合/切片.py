#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-08 14:29
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 切片
# @Software: PyCharm

#切片操作基本表达式：object[start_index:end_index:step]
#step：正负数均可，其绝对值大小决定了切取数据时的‘‘步长”，而正负号决定了“切取方向”，正表示“从左往右”取值，负表示“从右往左”取值。
#当step省略时，默认为1，即从左往右以增量1取值。“切取方向非常重要！”“切取方向非常重要！”“切取方向非常重要！”，重要的事情说三遍！

#start_index：表示起始索引（包含该索引本身）；该参数省略时，表示从对象“端点”开始取值，至于是从“起点”还是从“终点”开始，
#则由step参数的正负决定，step为正从“起点”开始，为负从“终点”开始。

#end_index：表示终止索引（不包含该索引本身）；该参数省略时，表示一直取到数据“端点”，至于是到“起点”还是到“终点”，
#同样由step参数的正负决定，step为正时直到“终点”，为负时直到“起点”。

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack', 'chen', 'chen2', 'chen3', 'chen4', 'chen5', 'chen6']

#取前三个元素
print(L[:3])

#取第3到第5个数
print(L[2:5])

#后5个数
print(L[-5:])

#从后取倒数第5个数至倒数第3个数
print(L[-5:-2])

#所有数,每两个取1个
print(L[::2])

#取第2到第10个元素,每两个取1个
print(L[1:10:2])

#取倒数第6至倒数第2个元素,每两个取1个
print(L[-6:-1:2])

for x in range(len(L)): 
    print('L[-1:%d:-1]=L[-1:%d:-1] is %s'%(x,x-len(L),L[-1:x:-1]==L[-1:x-len(L):-1]))