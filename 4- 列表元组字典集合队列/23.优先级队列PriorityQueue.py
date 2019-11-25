from queue import Queue
from queue import PriorityQueue

class Skill(object):
    def __init__(self,priority,description):
        self.priority = priority
        self.description = description
    #下面两个方法重写一个就可以了
    def __lt__(self,other):#operator < 
        return self.priority < other.priority
    def __cmp__(self,other):
        #call global(builtin) function cmp for int
        return cmp(self.priority,other.priority)
    def __str__(self):
        return '(' + str(self.priority)+',\'' + self.description + '\')'

def PriorityQueue_class():
    que = PriorityQueue()
    skill5 = Skill(5,'proficient')
    skill6 = Skill(6,'proficient6')
    que.put(skill6)
    que.put(Skill(5,'proficient'))
    que.put(Skill(10,'expert'))
    que.put(Skill(10,'novice'))
    while not que.empty():
        print(que.get())

PriorityQueue_class()