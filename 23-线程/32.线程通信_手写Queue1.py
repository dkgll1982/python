# 队列用法：https://blog.csdn.net/weixin_43533825/article/details/89155648
# 常用方法： 
# Queue.qsize() 返回队列的大小
# Queue.empty() 如果队列为空，返回True,反之False
# Queue.full() 如果队列满了，返回True,反之False，Queue.full 与 maxsize 大小对应
# Queue.get([block[, timeout]])获取队列，timeout等待时间
# Queue.get_nowait() 相当于Queue.get(False)，非阻塞方法
# Queue.put(item) 写入队列，timeout等待时间
# Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号。每个get()调用得到一个任务，接下来task_done()调用告诉队列该任务已经处理完毕。
# Queue.join() 实际上意味着等到队列为空，再执行别的操作 

from threading import Thread
from queue import Queue
import time

class Reciver(Thread):
    def __init__(self,name,queue):
        super().__init__()
        self.name=name
        self.queue=queue
    
    def run(self):
        while True:
            if not self.queue.empty():  #返回布尔值，判断队列是否为空
                #阻塞程序，时刻监听发送端传递的消息
                msg = self.queue.get()
                if self.name in('小红','小明','小刚','小宝','小玉'):
                    print('%s接收消息，内容：%s'%(self.name,msg))
                else:
                    print('%s可以不用来'%self.name) 
                #每task_done一次 就从队列里删掉一个元素，这样在最后join的时候根据队列长度是否为零来判断队列是否结束，从而执行主线程。
                self.queue.task_done()
            else:                       
                break

class Sender(Thread):
    def __init__(self,queue):
        super().__init__()
        self.queue=queue
    
    def sendmsg(self,name,msg):
        print('%s发送消息，内容：%s'%(name,msg))
        self.queue.put(msg) 
    
q = Queue()
s = Sender(q)
r1 = Reciver('小明',q)
r2 = Reciver('小红',q)
r3 = Reciver('小刚',q)
r4 = Reciver('小宝',q)
r5 = Reciver('小玉',q)
r6 = Reciver('小梁',q)

s.start()

for x in range(100):
    s.sendmsg('学校教务处','第%d条消息：下午开家长会！！！'%x)

# 这里休眠一秒钟，等到队列有值，否则队列创建时是空的，主线程直接就结束了，实验失败，造成误导
time.sleep(1)
    
r1.start()
r2.start()
r3.start()
r4.start()
r5.start()
r6.start() 

#一直阻塞直到队列中的所有项目都已获取并处理完毕,才往下执行主线程的内容
q.join()

# 给个标示，表示主线程已经结束
print("主线程结束")