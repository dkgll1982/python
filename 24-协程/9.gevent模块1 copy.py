from gevent import monkey
monkey.patch_all()
import gevent,time

def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.1)

g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
time.sleep(3)
# g1.join()
# g2.join()
# g3.join()