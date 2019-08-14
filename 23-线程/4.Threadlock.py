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
num = 10 
#创建一个全局的ThreadLocal对象
#每个线程有独立的存储空间
#每个线程对ThreadLocal对象都可以读写，但是互不影响
#在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁。
local = threading.local()

def run(x,n): 
    x = x + n
    x = x - n

def func(n):
    #每个线程都有local.x，就是线程的局部变量
    local.x = num
    for x in range(10000000):
        run(local.x,n)
    print("%s：%d"%(threading.current_thread().name,local.x))

if __name__ =="__main__":
    t1 =threading.Thread(target=func,name="Thread-001",args=(6,))
    t2 =threading.Thread(target=func,name="Thread-002",args=(9,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    print("num=",num)

#作用：为每个线程绑定一个数据库连接、http请求、用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便的访问这些资源
#一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。