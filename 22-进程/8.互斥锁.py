from multiprocessing import Process,Lock
import time

def task(name,mutex):
    mutex.acquire()
    print('%s 1'%name)
    time.sleep(1)
    print('%s 2'%name)
    time.sleep(1)
    print('%s 3'%name)
    time.sleep(1)
    mutex.release()

if __name__ == '__main__':
    #互斥锁：就是将要执行任务的部门代码（只涉及到修改共享数据的代码）变成串行
    #第一步：导入multiprocessing方法下面的Lock类
    #第二步：在if __name__ == '__main__':方法下面调用Lock类mutex=Lock()，拿到一个对象
    #第三步：在子类中需要共享的数据前后加入 加锁：mutex.acquire()——》需要共享修改数据的代码体《解锁：——mutex.release() 
    mutex = Lock()
    for i in range(3):
        p = Process(target =task,args=('进程%s'%i,mutex))
        p.start()
