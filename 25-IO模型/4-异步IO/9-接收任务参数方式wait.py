#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-01-07 14:28:02 
# @Last Modified by: guojun 
# @Last Modified time: 2020-01-07 14:28:02 
# @Software: vscode 

import asyncio
import random

async def coro(tag):
    await asyncio.sleep(random.uniform(0.5, 5))
    return random.uniform(0.5, 5)

loop = asyncio.get_event_loop()

# 此例子中；任务总数为11个
tasks = [coro(i) for i in range(1, 11)]

# 【控制运行任务数】：运行第一个任务就返回
# FIRST_COMPLETED ：第一个任务完全返回
# FIRST_EXCEPTION：产生第一个异常返回
# ALL_COMPLETED：所有任务完成返回 （默认选项）
dones, pendings = loop.run_until_complete(
    asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED))
print("第一次完成的任务数:", len(dones), list(dones)[0].result())

# dones：表示已经完成的任务
# pendings：表示未完成的任务
# 【控制时间】：运行一秒后，就返回
dones2, pendings2 = loop.run_until_complete(
    asyncio.wait(pendings, timeout=2))
print("第二次完成的任务数:", len(dones2))

# 【默认】：所有任务完成后返回
dones3, pendings3 = loop.run_until_complete(asyncio.wait(pendings2))
print("第三次完成的任务数:", len(dones3))

loop.close()