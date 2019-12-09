#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-12-15 18:01:19 
# @Last Modified by: guojun 
# @Last Modified time: 2019-12-15 18:01:19 
# @Software: vscode 
# 参考链接：https://www.cnblogs.com/95lyj/p/8954253.html
# 参考链接：https://www.cnblogs.com/xiao-apple36/p/9461295.html#_label2
# 参考链接：https://www.cnblogs.com/eailoo/p/9178763.html

#创建进程队列的另一个类JoinableQueue
# JoinableQueue([maxsize])：这就像是一个Queue对象，
# 但队列允许项目的使用者通知生成者项目已经被成功处理。通知进程是使用共享的信号和条件变量来实现的。

#参数介绍：
# maxsize是队列中允许最大项数，省略则无大小限制。  

#方法介绍：
# JoinableQueue的实例p除了与Queue对象相同的方法之外还具有：
# q.task_done()：使用者使用此方法发出信号，表示q.get()的返回项目已经被处理。如果调用此方法的次数大于从队列中删除项目的数量，将引发ValueError异常
# q.join():生产者调用此方法进行阻塞，直到队列中所有的项目均被处理。阻塞将持续到队列中的每个项目均调用q.task_done（）方法为止

import time
import random
from multiprocessing import Process,JoinableQueue

def consumer(name,q):
    while True:
        res=q.get()
        if res is None:break
        time.sleep(random.randint(1,3))
        print('\033[46m消费者===》%s 吃了 %s\033[0m' %(name,res))
        q.task_done()       #向q.join()发送一次信号,证明一个数据已经被取走了

def producer(name,q,food):
    for i in range(5):
        time.sleep(random.randint(1,2))
        res='%s%s' %(food,i)
        q.put(res)
        print('\033[45m生产者者===》%s 生产了 %s\033[0m' %(name,res))
    # 生产者使用此方法进行阻塞，直到队列中所有项目均被处理。阻塞将持续到为队列中的每个项目均调用q.task_done()方法为止。
    q.join()                #生产完毕，使用此方法进行阻塞，直到队列中所有项目均被处理。

if __name__ == '__main__':
    #1、共享的盆
    q=JoinableQueue()

    #2、生产者们:即厨师们
    p1=Process(target=producer,args=('egon',q,'包子'))
    p2=Process(target=producer,args=('刘',q,'泔水'))
    p3=Process(target=producer,args=('杨',q,'米饭'))

    #3、消费者们:即吃货们
    c1=Process(target=consumer,args=('alex',q))
    c2=Process(target=consumer,args=('梁',q))
    c1.daemon=True
    c2.daemon=True

    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()

    # 确定生产者确确实实已经生产完毕
    p1.join()
    p2.join()
    p3.join()
    
    # 1、主进程等生产者p1、p2、p3结束
    # 2、而p1、p2、p3是在消费者把所有数据都取干净之后才会结束
    # 3、所以一旦p1、p2、p3结束了，证明消费者也没必要存在了，应该随着主进程一块死掉，因而需要将生产者们设置成守护进程
    print('主进程结束')