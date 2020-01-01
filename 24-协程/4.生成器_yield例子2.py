def my_generator():
    print("first element:")
    n = yield
    print("second element:%s"%n)
    m = yield 2
    print("third element:%s"%m)
    r = yield 3
    
a = my_generator()
t1 = next(a)
t2 = a.send(1)
t3 = next(a)

print(t1,t2,t3)
#第一次调用时必须先next()或send(None)，否则会报错,next()等同于send(None)。
# a.send(None)
# a.send(10)
# a.send(20)


