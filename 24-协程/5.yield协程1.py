import time

index = 0 
def A():
    global index
    while index<20:
        index+=1
        print('------A-----')
        time.sleep(0.1)
        yield

def B():
    global index
    while index<20: 
        index+=1
        print('-------B-----')
        time.sleep(0.1)
        next(a)

a = A()
B()