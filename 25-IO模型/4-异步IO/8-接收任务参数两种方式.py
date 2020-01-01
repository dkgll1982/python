#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-01-07 14:28:08 
# @Last Modified by: guojun 
# @Last Modified time: 2020-01-07 14:28:08 
# @Software: vscode 

import asyncio
import random

async def sub_fun(name):
    print('子函数：%s' % (name))
    await asyncio.sleep(random.random())
    return name

async def main():
    li = ["张三", '李四', '王五', '马六', '钱七']
    tasks = [asyncio.ensure_future(sub_fun(item)) for item in li]

    # asyncio.wait方式(返回一个tuple对象,包含一个已经完成的任务set和未完成任务的set)
    dones, pending = await asyncio.wait(tasks)
    for task in dones:
        print('wait Task ret: ', task.result())

    # asyncio.gather方式
    results = await asyncio.gather(*tasks)
    for result in results:
        print('gather Task ret: ', result)

    # 使用wait和gather有哪些区别呢？
    # 首先,gather是需要所有任务都执行结束,如果某一个协程函数崩溃了,则会抛异常,都不会有结果。
    # wait有控制功能【控制运行任务数】：运行第一个任务就返回
    # FIRST_COMPLETED ：第一个任务完全返回
    # FIRST_EXCEPTION：产生第一个异常返回
    # ALL_COMPLETED：所有任务完成返回 （默认选项）

# 创建协程对象
loop = asyncio.get_event_loop()
# 执行任务列表
loop.run_until_complete(main())
