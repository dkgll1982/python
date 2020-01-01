import asyncio
from collections.abc import Generator, Coroutine
#参考链接:https://www.cnblogs.com/wongbingming/p/9095243.html

'''
只要在一个生成器函数头部用上 @asyncio.coroutine 装饰器
就能将这个函数对象，【标记】为协程对象。注意这里是【标记】，划重点。
实际上，它的本质还是一个生成器。
标记后，它实际上已经可以当成协程使用。后面会介绍。
'''

#async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
#把@asyncio.coroutine替换为async；
#把yield from替换为await。 
async def hello():
    # 异步调用asyncio.sleep(1):
     await asyncio.sleep(2)
     print('Hello,')

#不能让下边这个简单的例子运行：
#报错：RuntimeWarning: coroutine 'hello' was never awaited
# if __name__ == '__main__':
#     coroutine = hello()
#     print(isinstance(coroutine, Generator))  # True
#     print(isinstance(coroutine, Coroutine))  # False

#运行协同程序需要事件循环。使用 asyncio() library创建一个： 
loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()
 