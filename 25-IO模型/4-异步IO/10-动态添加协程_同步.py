import time
import asyncio
from queue import Queue
from threading import Thread

# 协程多任务通常运行在同一进程的单线程环境中，但如果有要将多个基于asyncio的协程运行在不同线程中的需求，
# 在主线程中使用asyncio.new_event_loop()创建一个new_loop，
# 在子线程中使用asyncio.set_event_loop(new_loop)为子线程设置其事件循环。
def start_loop(loop):
    # 一个在后台永远运行的事件循环
    asyncio.set_event_loop(loop)
    loop.run_forever()

def do_sleep(x, queue, msg=""):
    time.sleep(0.1*x)
    queue.put(msg)

if __name__ == "__main__": 
    queue = Queue() 

    start = time.time()
    print('主线程运行：',time.ctime())

    #主线程
    new_loop = asyncio.new_event_loop()

    # 定义一个子线程，并传入一个事件循环对象
    t = Thread(target=start_loop, args=(new_loop,))
    t.start() 

    # 动态添加两个协程
    # 这种方法，在主线程是同步的
    new_loop.call_soon_threadsafe(do_sleep, 6, queue, "第一个")
    new_loop.call_soon_threadsafe(do_sleep, 3, queue, "第二个")

    while True: 
        msg = queue.get()
        print("{} 协程运行完..".format(msg))
        print(time.ctime()) 
        time.sleep(1)
        if(queue.empty()):
            print('队列已空...') 
            new_loop.call_soon_threadsafe(new_loop.stop)
            break
    end = time.time()
    print('主线程状态：%s，运行耗时：%fs'%(new_loop.is_running(),end-start))