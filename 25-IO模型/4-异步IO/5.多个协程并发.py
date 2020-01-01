import asyncio

#第一步，当然是创建多个协程的列表。
# 协程函数
async def do_some_work(x):
    print('Waiting: ', x)
    await asyncio.sleep(0.2*x)
    return 'Done after {}s'.format(x)

# 协程对象
coroutine1 = do_some_work(10)
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(1)

# 将协程转成task，并组成list
tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3)
]
#第二步，将这些协程注册到事件循环中（wait()，gather()）
loop = asyncio.get_event_loop()
#loop.run_until_complete(asyncio.wait(tasks))

def callback(future):
    print('这里是回调函数，获取返回结果是：', future.result())

# 添加回调函数
# ①注意：谁先结束谁先回调出结果，并不是按照任务的先后顺序打印,可对比②看看
tasks[0].add_done_callback(callback)
tasks[1].add_done_callback(callback)
tasks[2].add_done_callback(callback)

#asyncio.wait：接收的tasks，必须是一个list对象，这个list对象里，存放多个的task
loop.run_until_complete(asyncio.wait(tasks))
#loop.run_until_complete(asyncio.gather(*tasks)) 

# ②按照任务的先后顺序打印,可对比①看看
# for task in tasks:
#     print('Task ret: ', task.result())