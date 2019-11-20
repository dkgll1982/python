#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-17 22:35
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 9.凑够一定数量才能一起执行.py
# @Software: PyCharm

import threading,time

#Barrier类是设置了一个线程数量障碍，当等待的线程到达了这个数量就会唤醒所有的等待线程。
# bar = threading.Barrier(4)

# def run():
#     print("%s--start"%(threading.currentThread().name))
#     time.sleep(1);
#     bar.wait()          # 当前线程进入阻塞状态
#     print("%s--end"%(threading.currentThread().name))


# if __name__ == "__main__":
#     for i in range(5):
#         threading.Thread(target=run).start()
  
# Barrier(parties, action=None, timeout=None)，是设置了一个线程数量障碍，当等待的线程到达了这个数量就会唤醒所有的等待线程。
# 每个线程通过调用wait()尝试通过障碍，并阻塞，直到阻塞的数量达到parties时，阻塞的线程被同时全部释放。
# action是一个可调用对象，当线程被释放时，其中一个线程会首先调用action，之后再跑自己的代码。
# timeout时默认的超时时间。

# wait(self, timeout=None) 当前线程进入阻塞状态
# abort(self) 强行突破阻碍，所有正在等待的线程和要调用wait()方法的线程收到一个BrokenBarrierError异常
# reset(self) 重置当前对象，所有正在等待的线程收到一个BrokenBarrierError异常 
# 参考链接：https://www.cnblogs.com/thunderLL/p/9872771.html

def display():
    print("放了你们")
 
barrier = threading.Barrier(3,display)
 
class Chick(threading.Thread):
    def run(self):
        while True:
            print(self.getName(),": 你抓不到我")
            time.sleep(1)
            print(self.getName(),": 好吧，你抓到我了")
            try:
                barrier.wait()
            except threading.BrokenBarrierError:
                print("BrokenBarrierError")
 
if __name__ == "__main__":
    c1 = Chick(name="A")
    c2 = Chick(name="B")
    c3 = Chick(name="C")
    c1.start()
    c2.start()
    c3.start()
    time.sleep(2)
    #barrier.reset()
    print("main")
