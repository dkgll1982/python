#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-24 21:12:36 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-24 21:12:36 
# @Software: vscode 
# 参考链接：https://blog.csdn.net/imzoer/article/details/8678029

from threading import Thread
import subprocess
from queue import Queue

num_threads = 3
ips = ['127.0.0.1', '116.56.148.187']
q = Queue()


def pingme(i, queue):
    while True:
        ip = queue.get()
        print('Thread %s pinging %s' % (i, ip))
        ret = subprocess.call('ping %s' % ip, shell=True,
                              stdout=open(r'C:\Users\dkgll\Desktop\python目录\ping.txt', 'w'), stderr=subprocess.STDOUT)
        if ret == 0:
            print('%s is alive!' % ip)
        elif ret == 1:
            print('%s is down...' % ip)
        queue.task_done()


# start num_threads threads
for i in range(num_threads):
    t = Thread(target=pingme, args=(i, q))
    t.setDaemon(True)
    t.start()

for ip in ips:
    q.put(ip)
print('main thread waiting...')
q.join()
print('Done')
