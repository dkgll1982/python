#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-09 14:47
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 进程
# @Software: PyCharm

from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')