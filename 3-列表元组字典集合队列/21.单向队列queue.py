#参考链接：https://blog.csdn.net/qq_31821675/article/details/91973423

 
from queue import Queue
from queue import PriorityQueue
print("Queue类实现了一个基本的先进先出(FIFO)容器，使用put()将元素添加到序列尾端，get()从队列尾部移除元素。")
 
q = Queue(3)
 
for i in range(3):
    q.put(i)

print(q.full(),q.qsize())
while not q.empty():
    print(q.get())

 
print("\n与标准FIFO实现Queue不同的是，LifoQueue使用后进先出序（会关联一个栈数据结构）。")
 
from queue import LifoQueue
 
q1 = LifoQueue()
 
for i in range(3):
    q1.put(i)
 
while not q1.empty():
    print(q1.get())
 
 
print("\n除了按元素入列顺序外，有时需要根据队列中元素的特性来决定元素的处理顺序。例如，老板的打印任务可能比研发的打印任务优先级更高。PriorityQueue依据队列中内容的排序顺序(sort order)来决定那个元素将被检索。")
 
 
class Job(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print('New job:', description) 
 
    def __lt__(self, other):
        return self.priority < other.priority
 
q2 = PriorityQueue()
 
q2.put(Job(5, 'Mid-level job'))
q2.put(Job(20, 'Low-level job'))
q2.put(Job(13, 'Important job')) #数字越小，优先级越高
 
while not q2.empty():
    next_job = q2.get() #可根据优先级取序列
    print('Processing job', next_job.description)
 
#print(help(Queue))
  