import os,time,random,sys
from multiprocessing import Process,current_process

def daemon():
    p = current_process()
    print("starting ID:%d prccess:%s\n" % (p.pid,p.name))
    #print("starting ID:%d\n" % (os.getpid()))
    sys.stdout.flush()
    time.sleep(3)
    print("Exiting:%s\n" % p.name)
    sys.stdout.flush() 

if __name__=="__main__":
    p = Process(name="Daemon",target=daemon)
    p.daemon=True
    p.start()
    p.join()
    time.sleep(1)
    #time.sleep(4)
    #由于主进程会在1秒后退出，守护进程的 print "Exiting:%s\n" % p.name这句是看不到的。
    #若想看到守护进程的 print "Exiting:%s\n" % p.name语句输出，可以利用join，
    #主进程等待守护进程的退出后再退出，即在，p.start()后添加p.join()然后把time。sleep（1）删除