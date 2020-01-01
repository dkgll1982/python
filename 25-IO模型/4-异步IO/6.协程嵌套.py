import asyncio
#参考链接：https://www.cnblogs.com/wongbingming/p/9114171.html

# 用于内部的协程函数
async def do_some_work(x):
    print('Waiting: ', x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

# 外部的协程函数
async def main():
    # 创建三个协程对象
    coroutine1 = do_some_work(10)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(1)

    # 将协程转为task，并组成list
    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]

    # 【重点】：await 一个task列表（协程）
    # dones：表示已经完成的任务
    # pendings：表示未完成的任务
    dones, pendings = await asyncio.wait(tasks)

    for task in dones:
        print('Task ret: ', task.result())

    ######################################################################
    # 注意如果使用的是asyncio.gather(),与await不一样,这里的「*」不能省略     #
    # results = await asyncio.gather(*tasks)                             #
    # for result in results:                                             #      
    #    print('Task ret: ', result)                                     #
    ######################################################################

loop = asyncio.get_event_loop()
loop.run_until_complete(main())