#参考链接：https://www.cnblogs.com/pythoner6833/p/9008642.html

# 基于greenlet的生产者消费者协程
from greenlet import greenlet
import random
import time

def Producer():
    while True:
        item = random.randint(1, 10)
        print("生产<{}>中...".format(item))
        time.sleep(1)
        c.switch(item)  # 切换到消费者，并将item传入。


def Consumer():
    while True:
        item = p.switch()  # 切换到生产者。等待生产者传递参数item
        print("消费<{}>中..".format(item))

c = greenlet(Consumer)  # 将普通函数编程协程
p = greenlet(Producer)  # 同理
c.switch()  # 启动协程，Consumer先执行
"""
从consumer开始执行，执行到item=p.switch()时，程序切换到producer，并等待传参
producer得到执行权后，生成一个item,并往下执行代码
当producer执行到c.switch(item)时，程序携带传递的item切换到consumer,
consumer继续往下执行，直到下一次运行到p.switch时，交出执行权，切换到producer，重复以上过程


greenlet的价值在于高性能的原生协程，
且语义更加明确、显示切换
执行到switch时就切换程序
直接将函数包装成协程，可以保留原代码的风格
"""