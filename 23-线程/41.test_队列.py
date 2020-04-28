from queue import Queue
from threading import Thread
import time

class product(Thread):
    def __init__(self,name,queue):
        super().__init__() 
        self.name = name
        self.queue = queue
        
    def run(self):
        self.queue.put(self.name)
        print('生成商品：',self.name)
        time.sleep(1)

class custom(Thread):
    def __init__(self,name,queue):
        super().__init__()
        self.name = name
        self.queue = queue
    
    def run(self):
        while True: 
            if not self.queue.empty():
                product = self.queue.get()
                print('顾客{}消费商品:{}'.format(self.name,product)) 
                time.sleep(1)
            else :  
                break

if __name__ == "__main__":
    print('主线程开始...')
    start = time.time()
    
    q = Queue(maxsize=3)
    
    list = "草莓,蓝莓,黑莓,桑葚,覆盆子,葡萄,青提,红提,水晶葡萄,马奶子.蜜橘,砂糖橘,金橘,蜜柑,甜橙".split(',')
    for x in list:
        pro = product(x,q)
        pro.start() 
        
    for y in range(3):
        cus = custom(y,q)    
        cus.start()
        
    cus.join()  
    
    end = time.time()
    print('主线程执行完毕...,耗时：%.2fs'%(end-start))