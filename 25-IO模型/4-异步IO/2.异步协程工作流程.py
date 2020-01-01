import asyncio
#参考链接：https://www.jianshu.com/p/02316b9d99a9

#协程完整的工作流程：
#1：定义/创建协程对象: async / @asyncio.coroutine
#2：定义事件循环对象容器: loop = asyncio.get_event_loop()
#3：将协程对象转化为task任务（两种方式）:
# 3.1 task = loop.create_task(协程对象),这种是单个task对象
# 3.2 task = asyncio.ensure_future(协程对象), tasks = [task, task...],这种是多个task对象
#4：将task任务扔进事件循环对象中触发
# 4.1 loop.run_until_complete(task)
# 4.2 多task对象的触发有两种方式：
# loop.run_until_complete(asyncio.wait(tasks))
# loop.run_until_complete(asyncio.gather(*tasks)) 

async def hello(name):
    await asyncio.sleep(2)
    print('Hello,', name)

# 定义协程对象
coroutine = hello("World")

# 定义事件循环对象容器
loop = asyncio.get_event_loop()
# 官方推荐不要直接创建 Task 实例，应该使用 ensure_future() 函数或 BaseEventLoop.create_task() 方法
# encure_future: 最高层的函数，推荐使用！
# create_task: 在确定参数是 coroutine 的情况下可以使用。
# Task: 可能很多时候也可以工作，但真的没有使用的理由！ 
#task = asyncio.ensure_future(coroutine)
# 或者将协程转为task任务
task = loop.create_task(coroutine)  
# 将task任务扔进事件循环对象中并触发
loop.run_until_complete(task)