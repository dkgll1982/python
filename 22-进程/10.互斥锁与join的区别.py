# 模拟抢票软件的原理：
from multiprocessing import Lock, Process
import json
import os,sys
import time,datetime
import random 
base_dir = os.path.dirname(os.path.abspath(__file__)) 
sys.path.append(base_dir)

def check(name):        # 查票功能实现并行访问
    time.sleep(0.2)
    with open(base_dir+'/'+'db.txt', 'rt', encoding='utf-8') as f:
        dic = json.load(f)
        print('%s 查看余票数为%s' % (name, dic['count']))

def get(name):          # 购票因为牵涉到对后台数据的修改，所以加互斥锁目的是逐一进行访问修改，以免数据错乱
    with open(base_dir+'/'+'db.txt', 'rt', encoding='utf-8') as f:
        dic = json.load(f)
    time.sleep(0.4)
    if dic['count'] > 0:
        # 有票
        dic['count'] -= 1
        time.sleep(random.randint(1, 3))  # 在购票时，模拟网络延迟...
        with open(base_dir+'/'+'db.txt', 'wt', encoding='utf-8') as f:
            json.dump(dic, f)
        print('%s %s购票成功,余票为%s' % (name,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),dic['count']))
    else:
        print('%s 没有余票' % name)

def task(name,mutex):
    # 查看（并行访问,都可以同时查询，不需要担心安全问题）
    check(name)
    # 抢票（加入互斥锁，实现串行访问，先到先得原则）
    mutex.acquire()
    get(name)
    mutex.release()         # 第一个购买完成后，解锁，后续进入继续购买

if __name__ == '__main__':
    mutex = Lock()          # 调用Lock类拿到一个对象
    prolist = [Process(target=task, args=('路人%s'%i,mutex,)) for i in range(10)]

    for p in prolist: 
        p.start()
    #for p in prolist:  
        #注意：如果join之后还有子线程为start，则变成串行了，后边的子线程也等到前边的线程执行完才能往下执行
        #子线程只要start之后就开始工作了，所有子线程均是并行执行的，只是join方法是主线程等待所有子线程执行完毕
        p.join()
