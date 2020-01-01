import time
import redis
import asyncio
from queue import Queue
from threading import Thread
#参考链接：https://www.cnblogs.com/wongbingming/p/9124142.html

def start_loop(loop):
    # 一个在后台永远运行的事件循环
    asyncio.set_event_loop(loop)
    loop.run_forever()

async def do_sleep(x, queue):
    await asyncio.sleep(0.1*x)
    queue.put("ok-%f"%x)

def get_redis():
    connection_pool = redis.ConnectionPool(host='127.0.0.1', db=0)
    return redis.Redis(connection_pool=connection_pool)

def consumer():
    while True:
        task = rcon.rpop("queue") #轮询接收redis名为queue的队列信息
        if not task:
            time.sleep(1)
            continue
        asyncio.run_coroutine_threadsafe(do_sleep(float(task), queue), new_loop)


if __name__ == '__main__':
    print(time.ctime())
    new_loop = asyncio.new_event_loop()

    # 定义一个线程，运行一个事件循环对象，用于实时接收新任务
    loop_thread = Thread(target=start_loop, args=(new_loop,))
    loop_thread.setDaemon(True)
    loop_thread.start()
    # 创建redis连接
    rcon = get_redis()

    queue = Queue()

    # 子线程：用于消费来自Redis的队列消息，并实时往事件对象容器中添加新任务
    consumer_thread = Thread(target=consumer)
    consumer_thread.setDaemon(True)
    consumer_thread.start()

    while True:
        msg = queue.get()
        print("协程运行完..,获取值：%s"%msg)
        print("当前时间：", time.ctime())

    #我们在Redis，分别发起了5s，3s，1s的任务。
    #从结果来看，这三个任务，确实是并发执行的，1s的任务最先结束，三个任务完成总耗时5s  
    #运行后，程序是一直运行在后台的，我们每一次在Redis中输入新值，都会触发新任务的执行。。