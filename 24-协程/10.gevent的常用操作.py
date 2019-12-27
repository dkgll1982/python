"""
gevent: 通过greenlet实现协程，核心就是遇到IO操作，会自动切换到其他协程

"""
# 将python标准库中的一些阻塞操作变为非阻塞
import gevent
from gevent import monkey
monkey.patch_all()
# 使用猴子补丁要写在第一行


def test1():
    print("test1")
    gevent.sleep(0)  # 模拟耗时操作
    print("test11")


def test2():
    print("test2")
    gevent.sleep(0)  # 模拟耗时操作
    print("test22")


g1 = gevent.spawn(test1)  # 将函数封装成协程，并启动
g2 = gevent.spawn(test2)
gevent.joinall([g1, g2])

"""
# joinall() 阻塞当前流程，执行给定的greenlet(列表中的对象),等待程序执行完
# spawn是启动协程，参数为函数名及其参数

运行结果：
test1
test2
test11
test22

代码执行test1,打印test1，遇到gevent.sleep(0)时切换程序，执行test2
test()执行，打印test2，执行到gevent.sleep(0)时切换程序
执行test1在gevent.sleep(0)后面的代码，直到再次遇到gevent时，切换程序
然后在test2中，继续执行gevent后的代码，直到遇到gevent时，再次切换
直到程序执行完毕

gevent的价值在于它的使用基于epoll的libev来避开阻塞；
使用基于gevent的高效协程，来切换执行
只在遇到阻塞的时候切换，没有轮询和线程开销
"""
