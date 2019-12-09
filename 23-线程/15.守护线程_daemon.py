# import time
# import threading

# #情况一：线程为非守护线程
# def fun():
#     print("start fun")
#     time.sleep(2)
#     print("end fun")

# def main():
#     print("main thread")
#     t1 = threading.Thread(target=fun,args=())
#     t1.setDaemon(False)
#     t1.start()
#     time.sleep(1)
#     print("main thread end")

# if __name__ == '__main__':
#     main()

# #说明：程序在等待子线程结束,才退出了。 

import time
import threading 

def fun(name,sept):
    print("%s——start fun"%name)
    time.sleep(sept)
    print("%s——end fun"%name)

def main():
    print("main thread")
    t1 = threading.Thread(target=fun,args=('t1',3,))
    t2 = threading.Thread(target=fun,args=('t2',1,))

    t1.setDaemon(True)
    print('t1.daemon:%s,t2.daemon:%s'%(t1.daemon,t2.daemon))
    print('t1.daemon:%s,t2.daemon:%s'%(t1.isDaemon(),t2.isDaemon()))

    t1.start()

    t2.start()

    # join()的阻塞是不分对象的，与线程是否守护线程，是否主线程无关，一旦调用，主线程将一直等待，直到被加入的线程运行完成。
    # 只是需要注意，想要真正的多线程运行就要启动所有的子线程后统一调用join，不然就会顺序执行，跟单线程运行没什么区别了

    #t1.join()
    t2.join()

    time.sleep(1)
    print("main thread end")

if __name__ == '__main__':
    main()

#说明：程序在主线程结束后,直接退出了。 导致子线程没有运行完。

#应用场景:
# 如果你设置一个线程为守护线程,就表示你在说这个线程是不重要的,在进程退出的时候,不用等待这个线程退出。
# 如果你的主线程在退出的时候,不用等待那些子线程完成,那就设置这些线程的daemon属性。即在线程开始(thread.start())之前,
# 调用setDeamon()函数,设定线程的daemon标志。(thread.setDaemon(True))就表示这个线程“不重要”。
# 如果你想等待子线程完成再退出,那就什么都不用做。,或者显示地调用thread.setDaemon(False),设置daemon的值为false。
# 新的子线程会继承父线程的daemon标志。整个Python会在所有的非守护线程退出后才会结束,即进程中没有非守护线程存在的时候才结束。
 