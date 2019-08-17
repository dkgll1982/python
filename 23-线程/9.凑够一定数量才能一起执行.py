#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-17 22:35
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 9.凑够一定数量才能一起执行.py
# @Software: PyCharm

import threading,time

bar = threading.Barrier(4)

def run():
    print("%s--start"%(threading.currentThread().name))
    time.sleep(1);
    bar.wait()
    print("%s--end"%(threading.currentThread().name))


if __name__ == "__main__":
    for i in range(5):
        threading.Thread(target=run).start()
