参考链接：https://www.jb51.net/article/168021.htm

                                python并发编程 Process对象的其他属性方法join方法详解

一 Process对象的join方法

在主进程运行过程中如果想并发地执行其他的任务，我们可以开启子进程，此时主进程的任务与子进程的任务分两种情况

情况一：

在主进程的任务与子进程的任务彼此独立的情况下，主进程的任务先执行完毕后，主进程还需要等待子进程执行完毕，然后统一回收资源。 这种是没有join方法

情况二：
如果主进程的任务在执行到某一个阶段时，需要等待子进程执行完毕后才能继续执行，

就需要有一种机制能够让主进程检测子进程是否运行完毕，在子进程执行完毕后才继续执行，否则一直在原地阻塞，这就是join方法的作用

让主进程等着，所有子进程执行完毕后，主进程才继续执行


join 会变串行？

既然join是等待进程结束, 那么我像下面这样写, 进程不就又变成串行的了吗?
当然不是了, 必须明确：p.join()是让谁等？
很明显p.join()是让主线程等待p 子进程的结束，卡住的是主进程而绝非 子进程p， 

from multiprocessing import Process
import time
import os
def task(name):
  print('%s is running' %(name))
  time.sleep(2)
  print('%s is end' %(name))
if __name__ == '__main__':
  p1 = Process(target=task, args=('子进程1',))
  p2 = Process(target=task, args=('子进程2',))
  p3 = Process(target=task, args=('子进程3',))
  p4 = Process(target=task, args=('子进程4',))
  p1.start()
  p2.start()
  p3.start()
  p4.start()
  p1.join()
  p2.join()
  p3.join()
  p4.join()
  print('主',os.getpid(),os.getppid())
详细解析如下：

进程只要start就会在开始运行了,所以p1-p4.start()时,系统中已经有四个并发的进程了

而我们p1.join()是在等p1结束,没错p1只要不结束主线程就会一直卡在原地,这也是问题的关键

join是让主线程等,而p1-p4仍然是并发执行的,p1.join的时候,其余p2,p3,p4仍然在运行,等#p1.join结束,可能p2,p3,p4早已经结束了,这样p2.join,p3.join.p4.join直接通过检测，无需等待

所以4个join花费的总时间仍然是耗费时间最长的那个进程运行的时间

所以不会是串行执行，是并发执行

4个join花费的总时间仍然是耗费时间最长的那个进程运行的时间

所以就是5秒，就是子进程1 那个等待的时间

join 保证所有子进程执行完 主进程才能工作，不然一直阻塞