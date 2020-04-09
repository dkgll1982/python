#如果 Python 函数直接返回多个值，Python 会自动将多个返回值封装成元组。
def fun():
    return 1,'值1',True,1.2

ret1 = fun()

print(type(ret1))
print(ret1)

#直接使用多个变量来接收fun()函数返回的值，这就是利用了 Python 提供的序列解包功能。
ret11,ret12,ret13,ret14 = fun()
print(type(ret11),type(ret12),type(ret13),type(ret14))
print(ret11,ret12,ret13,ret14)

print('*'*40)

def fun2():
    return (1,'值1',True,1.2)

ret2 = fun2()
print(type(ret2))
print(ret2)

ret21,ret22,ret23,ret24 = fun()
print(type(ret21),type(ret22),type(ret23),type(ret24))
print(ret21,ret22,ret23,ret24)

print(ret1 == ret2)