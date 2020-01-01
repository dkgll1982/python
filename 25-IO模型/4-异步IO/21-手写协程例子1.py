#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-01-07 14:28:17 
# @Last Modified by: guojun 
# @Last Modified time: 2020-01-07 14:28:17 
# @Software: vscode 

import asyncio,random

# 1：创建协程对象列表
# 2：创建事件循环对象容器
# 3：将协程对象转换为task任务
# 4：将task任务扔进事件循环对象中触发 
async def test_func(name):
    print('%s,我是异步运行的！！！' % name)
    await asyncio.sleep(random.random())
    return name

#定义协程对象
coroutine = test_func('张三')
#创建事件循环对象容器
loop = asyncio.get_event_loop()
#将协程对象转换为task任务
task = loop.create_task(coroutine)
#将task任务扔进事件循环对象中触发
loop.run_until_complete(task)

#获取任务运行结果（同步回调）
print('任务运行结果：%s'%task.result())

print(' ')

#另外一种获取结果的方式（异步回调-add_done_callback）
coroutine = test_func('李四')
loop = asyncio.get_event_loop()
task = loop.create_task(coroutine)
task.add_done_callback(lambda self:print('异步回调：%s'%self.result()))
loop.run_until_complete(task)

print(' ')

#主函数，嵌套调用子函数
async def main_fun():
    tasks = [
        asyncio.ensure_future(test_func('张龙')),
        asyncio.ensure_future(test_func('赵虎')),
        asyncio.ensure_future(test_func('王朝')),
        asyncio.ensure_future(test_func('马汉'))
    ]
    print('type:',type(tasks[0]),type(test_func))

    #获取异步回调结果
    for task in tasks:
        task.add_done_callback(lambda self:print('异步回调：%s'%self.result())) 
    
    # 【重点】：await 一个task列表（协程）
    # dones：表示已经完成的任务
    # pendings：表示未完成的任务
    dones, pendings = await asyncio.wait(tasks)
    for task in dones:
        print('wait Task ret: ', task.result())
         
    results = await asyncio.gather(*tasks)
    for result in results:
        print('gather Task ret: ', result)
        
loop =  asyncio.get_event_loop()
loop.run_until_complete(main_fun())  