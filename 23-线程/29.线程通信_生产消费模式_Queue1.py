#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-18 10:39
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 12.生产者与消费者.py
# @Software: PyCharm
#参考链接：https://www.cnblogs.com/wongbingming/p/9035579.html

# Event 和 Condition 是threading模块原生提供的模块，原理简单，功能单一，
# 它能发送 True 和 False 的指令，所以只能适用于某些简单的场景中。

# 而Queue则是比较高级的模块，它可能发送任何类型的消息，包括字符串、字典等。
# 其内部实现其实也引用了Condition模块（譬如put和get函数的阻塞），
# 正是其对Condition进行了功能扩展，所以功能更加丰富，更能满足实际应用。

import threading,time,queue,random
from collections import deque

#生产者
def product(id,q):
    ind = 5
    while ind>0:
        num = random.randint(0,10000)
        q.put(num);
        print("生产者%d生产了%d数据放入了队列"%(id,num))
        time.sleep(3)
        ind-=1
    #put队列完成的时候千万不能用task_done()，否则会报错,因为该方法仅仅表示get成功后，执行的一个标记。
    #q.task_done()

#消费者
def customer(id,q):
    while True:
        # 阻塞程序，等待队列消息。
        item = q.get()
        if item is None:
            break
        print("消费者%d消费了%d数据"%(id,item))
        time.sleep(2)
        #告知等待的队列(queue.join()这里在等待)任务的处理已完成。
        q.task_done()
    print('消费完毕！')

if __name__ =="__main__": 
    # maxsize默认为0，不受限
    # 一旦>0，而消息数又达到限制，q.put()也将阻塞 
    q = queue.Queue(maxsize=0)

    #启动生产者
    for i in range(4):
        threading.Thread(target = product,args=(i,q)).start()
    #启动消费者
    for i in range(3):
        threading.Thread(target = customer,args=(i,q)).start()

    q.join()
    print('主线程结束！')
  
# 常用方法
# q.size()：返回队列的正确大小。因为其他线程可能正在更新此队列，所以此方法的返回数字不可靠。

# q.empty()：如果队列为空，返回True，否则返回False。

# q.full()：如果队列已满，返回True，否则返回False。

# q.put(item,block,timeout)：将item放入队列。
# 如果block设为True（默认值），调用者将被阻塞直到队列中出现可用的空闲位置为止。
# 如果block设为False，队列满时此方法将引发Full异常。

# q.put_nowait(item):等价于q.put(item,False)

# q.get(block,timeout):从队列中删除一项，然后返回这个项。
# 如果block设为True（默认值），调用者将阻塞，直到队列中出现可用的空闲为止。
# 如果block设为False，队列为空时将引发Empty异常。
# timeout提供可选的超时值，单位为秒，如果超时，将引发Empty异常。

# q.get_nowait()：等价于get(0)

# q.task_done():在队列种数据的消费者用来指示对于项的处理已经结束。如果使用此方法，那么从队列中删除的每一项都应该调用一次。

# q.join()：阻塞直到队列中的所有项均被删除和处理为止。一旦为队列中的每一项都调用了一次q.task_done()方法，此方法将会直接返回。  