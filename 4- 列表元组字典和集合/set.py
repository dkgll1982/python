#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-08 10:48
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : set
# @Software: PyCharm


# 因为258是int对象，是不可变对象的。所以下面3个id的值都是一样的，最后一句的结果也是为True
# 有点奇怪的是为什么在IDLE，和在脚本执行的结果不太一样。所以下面的代码请在脚本中执行。

astr = '..'
bstr = '..'
cstr = astr + ''
print(cstr is bstr) # True
print(id(astr), id(bstr), id('..'))  # 三个id相同


m=[5,9]
print(id(m));
m+=[6]
print(id(m));

print(id(258))
a = 258
print(id(a))
b = 258
print(id(b))
print(a is b)
b+=1;
print(id(b));
print(id(a))

x = set('runoob')
y = set('google')

print(list(x)[2])
print(x, y)
(set(['b', 'r', 'u', 'o', 'n']), set(['e', 'o', 'g', 'l']))   # 重复的被删除
print(x & y)         # 交集
set(['o'])
print(x | y)         # 并集
set(['b', 'e', 'g', 'l', 'o', 'n', 'r', 'u'])
print(x - y)         # 差集
set(['r', 'b', 'u', 'n'])
print(y - x)         # 差集

li = [3,4,5,1,2,56,12,652,235]
li.sort(reverse=True)
print(li)

s = set([3,4,5,1,2,56,12,652,235]);
s.add(2)
print(s)

def myfun(func,):
    if func == "abs":
        print("绝对值");
    elif func == "add":
        print("加法")
    #看似可以返回多个值，其实是假象，返回的是个元组tuple，不行可以试试type(myfun("")),结果就是<class 'tuple'>
    return 1,2,3,4,"sdf"

x,y,z,h,d = myfun("abs")
print(type(d))

a1,b2,c3,d4,e5,f6=(1,2,3,4,5,6)

print(c3)

age=1202;
if age<10:
    pass;
elif age<200:
    pass
else:
    print(age)

a = {1,'c',1,(1,2,3),'c'}
b = {1, 'c', (1, 2, 3)};
print(a)
print(type(a))

print('-------------------------------')
#由于集合中的元素是无序的，因此无法向列表那样使用下标访问元素。Python 中，访问集合元素最常用的方法是使用循环结构，将集合中的数据逐一读取出来。
for ele in a:
    print(ele,end=' ')
print('')
print('-------------------------------')

set1 = set("c.biancheng.net")
set2 = set([1,2,3,4,5])
set3 = set((1,2,3,4,5))
print("set1:",set1)
print("set2:",set2)
print("set3:",set3)

a.add((1,2));
a.add(123);

print('-------------------------------')
print(a)
print('-------------------------------')

a.remove((1,2,3))
a.discard((1,2,3,3))
print(a)
print('-------------------------------')
