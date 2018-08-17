import math
L = []
n=1

t = (1,)

print(t)

def add(x,y,f):
    return f(x)+f(y)

def fun(x):
    return x*100

print(add(20,30,fun));
print(add(20,30,abs));
print(add(20,30,math.sqrt));

lll = map(lambda x: x ** 2 ** 2, [1, 2, 4, 8, 64]);

for li in lll:
    print(li)

for item in dir(__builtins__):
    print(item)

d = {'a': 1, 'b': 2, 'c': 3}

for k,v in d.items():
    print(d[k]==v);
    print("k:%s    v:%s"%(k,v));

for x in '12121':
    print(x);

from collections import Iterable

obj=121223;
if isinstance(obj,Iterable):
    print(isinstance(obj,Iterable));
else:
    print("对象%s:不可迭代"%obj)

li=[x for x in range(1, 11) if x%2 == 1]
print(li);

li = [m + n for m in 'ABC' for n in 'XYZ']
print(li);
import os # 导入os模块，模块的概念后面讲到
li =[d for d in os.listdir('.')] # os.listdir可以列出文件和目录
print(li)

L1 = ['Hello', 'World', 1223, 'Apple', None]
for x in (x.lower() for x in L1 if isinstance(x,str)):
    print(x)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield n
        a, b = b, a + b
        n = n + 1
    return 'done'

for x in fib(10):
    print (x);

def read_file(fpath):
   BLOCK_SIZE = 1024
   with open(fpath, 'rb') as f:
       while True:
           block = f.read(BLOCK_SIZE)
           if block:
               yield block
           else:
               return

def get_primes(number):
    while True:
        yield number
        number += 1
f= get_primes(1);
print(next(f));

l2=iter(L1);
print(next(l2));
print(next(l2));
print(next(l2));
print(next(l2));

##表示一个无限大的整数
def bignum():
    b=0;
    while True:
        yield b;
        b+=1;

bb = bignum();
print(next(bb))

print('');
def fabs():
    b=1;
    while b<2000000:
        yield  b;
        b+=1;

b = fabs();

print(next(b));
print(next(b));
print(next(b));
print(next(b));

l1 = [1,34,52,234,32];

print('');
for x in reversed(sorted(l1)):
    print(x);