def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1 

def f_wrapper(fun_iterable):
    print('start')
    for item in fun_iterable:
        yield item
    print('end')

def f_wrapper2(fun_iterable):
    print('start')
    yield from fun_iterable  #注意此处必须是一个可生成对象
    print('end')

#再强调一遍：yield from后面必须跟iterable对象(可以是生成器，迭代器)
 
iter = fab(5)
wrap = f_wrapper(iter)
for i in wrap:
    print(i, end=' ')

wrap = f_wrapper2(fab(5))
for i in wrap:
    print(i,end=' ')