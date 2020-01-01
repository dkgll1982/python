# def foo():
#     print("starting...")
#     while True:
#         res = yield 4
#         print("res:",res)
# g = foo()
# print(next(g))
# print("*"*20)
# print(next(g)) 
# print(next(g)) 
# print(next(g)) 

def fun(total):
    index = 0 
    while index<total:
        new_index = yield
        index += new_index
        print("#",flush=True,end='')

f = fun(1000)
f.__next__()

for x in range(1000):
    try:
        f.send(10) 
    except StopIteration as e:
        exit('100%')  
 