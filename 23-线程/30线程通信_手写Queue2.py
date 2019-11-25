from threading import Thread
import time
from queue import Queue

# q = Queue()
# q.put(1)
# q.put(3)
# print(q.qsize())
# q.put(2)
# q.put(4)
# print(q.qsize())
# print(q.empty(),q.get())
# print(q.qsize())
# print(q.empty(),q.get())

# print(q.qsize())

def send(queue,msg):
    time.sleep(1)
    queue.put(msg)
    print("发送消息:%s"%(msg))

def recive(queue,i):
    time.sleep(1)
    while not queue.empty():
        msg = queue.get()
        print("接收者%d\t接收消息:%s"%(i,msg))
    print('队列已经清空，将回到主线程')
    queue.task_done()

if __name__ == "__main__":
    q = Queue()

    Thread(target=send, args=(q,'1:这是一个简单的发送接收队列',)).start()
    time.sleep(0.01)
    Thread(target=send, args=(q,'2:测试队列的特性',)).start()
    time.sleep(0.01)
    Thread(target=send, args=(q,'3:先进先出',)).start()
    time.sleep(0.01)
    Thread(target=send, args=(q,'4:先put后get',)).start()
    time.sleep(0.01)
    Thread(target=send, args=(q,'5:队列为空（empty）时结束任务（task_done）回到主线程\r\n',)).start()
    time.sleep(0.01)
    
    Thread(target=recive, args=(q,1)).start()
    Thread(target=recive, args=(q,2)).start()
    Thread(target=recive, args=(q,3)).start()

    q.join()
    time.sleep(3)
    print('主线程结束！')
