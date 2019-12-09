# 使用计时器线程-

from threading import Timer, Thread, Event
import time

def mywork(t):
    print("每过%d年一个轮回。。。"%(int(t)*1000))

class perpetualTimer():

    def __init__(self, t, hFunction):
        self.t = t
        self.hFunction = hFunction
        self.thread = Timer(self.t, self.handle_function)

    def handle_function(self):
        self.hFunction(self.t)
        self.thread = Timer(self.t, self.handle_function)
        self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()
    
    def printer(self):
        print('ipsem lorem')
     
if __name__ == "__main__":
    t = perpetualTimer(1,mywork)
    t.start()
    time.sleep(10)
    t.cancel()
    
# 这是可以阻止的t.cancel()
