def a(args):
    #初始值
    ret = args
    while True:
        ret = yield ('' if args is None else args) + ':' + ('' if ret is None else ret)
        if ret is None:
            break  
        
def b(args):
    send = args
    while True:
        send = yield from a(send)
        # 只有子生成器要结束（return）了，yield from左边的变量才会被赋值，后面的代码才会执行。
        if send is not None:
            print(send)

t = b('张林')
next(t)
print(t.send('男'))
print(t.send('28岁'))
print(t.send('华中科技大学'))
print(t.send('计算机专业'))
t.send(None)
