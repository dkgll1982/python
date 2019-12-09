# #进程池
# from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
# import  os,time,random
# #IO密集型：线程池，CPU计算密集型：进程池

# def task(name):
#     print('name:%s pid:%s run'%(name,os.getpid()))
#     time.sleep(random.randint(1,2))

# if __name__ == '__main__':
#     pool = ProcessPoolExecutor(3)
#     for i in range(10):
#         pool.submit(task,"egons%s"%i)
    
#     pool.shutdown(wait=True)   #默认是True，意思是进程都执行完毕，再执行主进程的内容

#     print('主')

#线程池
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
from threading import currentThread
import  os,time,random
#IO密集型：线程池，CPU计算密集型：进程池

def task():
    print('name:%s pid:%s run'%(currentThread().getName(),os.getpid()))
    time.sleep(random.randint(1,2))

if __name__ == '__main__':
    pool = ThreadPoolExecutor(5)
    for i in range(10):
        pool.submit(task)
    
    pool.shutdown(wait=True)   #默认是True，意思是进程都执行完毕，再执行主进程的内容

    print('主')
