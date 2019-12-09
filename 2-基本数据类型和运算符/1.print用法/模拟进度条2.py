#!/usr/bin/env/python
# _*_ coding:utf-8 _*_
# @Time   : 2018/7/13 1:08
# @Author : Jingzeng Mo
# @Project: FTP_PROGRAM
# 参考链接：https://www.cnblogs.com/jingzeng/p/9305595.html

import sys
import math 

def progress_bar(portion, total):
    """
    total 总数据大小，portion 已经传送的数据大小
    :param portion: 已经接收的数据量
    :param total: 总数据量
    :return: 接收数据完成，返回True
    """
    part = total / 50  # 1%数据的大小
    count = math.ceil(portion / part)
    sys.stdout.write('\r')
    sys.stdout.write(('[%-50s]%.2f%%' % (('>' * count), portion / total * 100)))
    sys.stdout.flush()

    if portion >= total:
        sys.stdout.write('\n')
        return True
    
    
# 调用方式
portion = 0
total = 25482000
while True:
    portion += 1024
    sum = progress_bar(portion, total)
    if sum:
        break
print("ok")