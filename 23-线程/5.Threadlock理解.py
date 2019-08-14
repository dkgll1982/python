#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-11 18:14:10 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-11 18:14:10 
# @Software: vscode  

import threading 

# def show(num):
#     print(threading.current_thread().getName(), num)

# def thread_cal():
#     # 每个线程都有自己的 local_num，各个线程之间互不干涉。
#     local_num = 0
#     for _ in range(1000):
#         local_num += 1
#     # 需要给 show 函数传递 local_num 局部变量，并没有什么不妥。
#     # 不过考虑在实际生产环境中，我们可能会调用很多函数，每个函数都需要很多局部变量，这时候用传递参数的方法会很不友好。
#     show(local_num)

# threads = []

# for i in range(10):
#     threads.append(threading.Thread(target=thread_cal))
#     threads[i].start()


global_data = threading.local()
def show():
    print (threading.current_thread().getName(), global_data.num)
def thread_cal():
    global_data.num = 0
    for _ in range(1000):
        global_data.num += 1
    show()
threads = []

print ("Main thread: ", global_data.__dict__) # {}   


for i in range(10):
    threads.append(threading.Thread(target=thread_cal))
    threads[i].start()