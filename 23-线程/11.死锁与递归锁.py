from threading import Thread, Lock, RLock
import time

# 递归锁:可以连续acquire多次，每acquire一次计数器+1，只有计数为0时，才能被抢到acquire
#mutexA =  Lock()
#mutexB = Lock()

mutexA = mutexB = RLock()

class MyThread(Thread):
    def run(self):
        self.f1()  # 先拿A锁
        self.f2()  # 先拿B锁

    def f1(self):
        mutexA.acquire()

        print('%s 拿到了A锁' % self.name)
        
        mutexB.acquire()
        print('%s 拿到了B锁' % self.name)
        mutexB.release()

        mutexA.release()

    def f2(self):
        mutexB.acquire()
        print('%s 拿到了B2锁' % self.name)
        time.sleep(0.1) 

        mutexA.acquire()
        print('%s 拿到了A2锁' % self.name)
        mutexA.release()

        mutexB.release()


if __name__ == "__main__":
    for i in range(10):
        t = MyThread()
        t.start()
