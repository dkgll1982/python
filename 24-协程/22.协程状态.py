from inspect import getgeneratorstate  #一定要导入
from time import sleep

#协程有四种状态，分别是
#GEN_CREATED：等待执行，即还没有进入协程
#GEN_RUNNING：解释器执行（这个只有在使用多线程时才能查看到他的状态，而协程是单线程的）
#GEN_SUSPENDED：在yield表达式处暂停（协程在暂停等待的时候的状态）
#GEN_CLOSED：执行结束（协程执行结束了之后的状态）

def my_generator():
    for i in range(3):
        sleep(0.5)
        x = yield i + 1  
 
g = my_generator()      #创建一个生成器对象
 
def main(generator):
    try:
        print("生成器状态为:{0}".format(getgeneratorstate(g)))  
        next(g)         #激活生成器
        print("生成器状态为:{0}".format(getgeneratorstate(g)))  
        g.send(100)
        print("生成器状态为:{0}".format(getgeneratorstate(g)))  
        next(g)
        print("生成器状态为:{0}".format(getgeneratorstate(g)))  
        next(g)
    except StopIteration:
        print('全部迭代完毕了')
        print("生成器状态为:{0}".format(getgeneratorstate(g))) 
 
main(g)
'''运行结果为：
生成器状态为:GEN_CREATED
生成器状态为:GEN_SUSPENDED
生成器状态为:GEN_SUSPENDED
生成器状态为:GEN_SUSPENDED
全部迭代完毕了
生成器状态为:GEN_CLOSED
'''