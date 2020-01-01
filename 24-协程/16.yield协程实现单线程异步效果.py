import time

def consumer(name):
    print('%s 准备吃包子拉！'%name)

    while True:
        baozi=yield 
        print(' 【%s】包子被【%s】吃了...'%(baozi,name))

def producer(name):
    c = consumer('张三')
    d = consumer('王二')
    c.__next__()
    d.__next__()

    print('\r\n%s开始做包子拉...'%name)
    for i in range(10): 
        print('\r\n%s做了俩笼包子！'%name)
        c.send('雪菜肉丝')
        d.send('馒头%d'%i)

producer('老子')