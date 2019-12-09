from multiprocessing import Process
from threading import Thread
import os,time

# #如果并发的是计算密集型任务：多进程效率高
# def work():
#     res = 0 
#     for i in range(100000000):
#         res+=i

# if __name__ == '__main__':
#     l = []
#     cn = os.cpu_count()                 #查询CPU核心数
#     start = time.time()
#     print(cn)      

#     for i in range(cn):
#         #p = Process(target = work)     #耗时18s多
#         p = Thread(target = work)       #耗时33s多
#         l.append(p)
#         p.start() 

#     for p in l: 
#         p.join()

#     end = time.time()

#     print('run time is %ss'%(end - start))

#如果并发的是IO密集型任务：多线程效率高
def work(): 
    time.sleep(10)
    print('=====>')

if __name__ == '__main__':
    l = []
    cn = os.cpu_count()                 #查询CPU核心数
    start = time.time()
    print(cn)      

    for i in range(40):
        #p = Process(target = work)     #耗时33s多，大部分耗费在创建在进程上
        p = Thread(target = work)     #耗时1s多
        l.append(p)
        p.start() 

    for p in l: 
        p.join()

    end = time.time()

    print('run time is %ss'%(end - start))
    
    