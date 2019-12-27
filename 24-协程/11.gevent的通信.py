# gevent通信
import time
import random

from gevent import monkey;monkey.patch_all()
import gevent
from gevent.queue import Queue

def write(q):
    while True:
        print("put:{}".format('text'))
        q.put('text')
        gevent.sleep(1)  # 模拟阻塞

def read(q):
    while True:
        print("get:{}".format(q.get()))  # get本身是阻塞
        gevent.sleep(2)  # 模拟阻塞

q = Queue()
w = gevent.spawn(write, q)  # 遇到阻塞自动切换
r = gevent.spawn(read, q)
gevent.joinall([w, r])