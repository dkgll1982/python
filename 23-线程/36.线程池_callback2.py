# 提交任务的两种方式
# 1；同步调用:提交任务后，就在原地等待任务执行完毕，拿到结果，再执行下一行代码，导致程序是串行执行

from concurrent.futures import ThreadPoolExecutor
import time
import random

def la(name):
    print('%s is laing ' % name)
    time.sleep(random.randint(3, 5))
    res = random.randint(7, 13)*'#'
    return {'name': name, 'res': res}
    #weight({'name': name, 'res': res})

def weight(shit):
    re = shit.result()
    name = re['name']
    size = len(re['res'])
    print('%s 拉了%skg' % (name, size))


if __name__ == "__main__":
    pool = ThreadPoolExecutor(13)

    # result(timeout=None)：获取该 Future 代表的线程任务最后返回的结果。如果 Future 代表的线程任务还未完成，
    # 该方法将会阻塞当前线程，其中 timeout 参数指定最多阻塞多少秒。
    # shit1 = pool.submit(la,'alex').result()
    # weight(shit1)
    # shit2 = pool.submit(la,'wupeiqi').result()    
    # weight(shit2)
    # shit3 = pool.submit(la,'yuanhao ').result()
    # weight(shit3)
    

#2：异步调用：提交任务后，不再等待任务执行完毕 
    #去掉result，变成并行执行，不用等结果出来再执行下一个
    # shit1 = pool.submit(la,'alex') 
    # shit2 = pool.submit(la,'wupeiqi')     
    # shit3 = pool.submit(la,'yuanhao ') 
    pool.submit(la,'alex').add_done_callback(weight) 
    pool.submit(la,'wupeiqi').add_done_callback(weight)      
    pool.submit(la,'yuanhao ').add_done_callback(weight)  