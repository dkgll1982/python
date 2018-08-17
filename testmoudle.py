#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-06-08 10:51
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : testmoudle.py
# @Software: PyCharm

# a=(1,)
#
# b=(1);
#
# a=(23,43,43,54,[23423432,345,436,456,5,67,567,65,76,575])

# print(type(a));
# # print(type(a[1]));
# # print(type(a[4]));
# # print(type(b));
# # print(a);
# # print(b);

index=0;
a=[
    {"name":"炸三","age":13,"sex":"女"},
    {"name":"里斯","age":2313,"sex":"不男不女"},
    {"name":"王屋","age":134,"sex":"变新人"},
    {"name":"码流","age":1354,"sex":"小曦曦能给"}
]

s1 = set([333,234,2,123,12,3,4,5,6,7,8,9]);
s1.add(1);
s1.add(2);

s2=set([2,433,123,13,1,3,43,5,34,5,43,53,53,53])

# print(type(s1));
# print(s1);
#
# print('s1 & s2 = %s' % (s1&s2) );
# print('s1 | s2 = %s' % (s1|s2) );


# for i in range(len(a)):
#     for f in a[i].keys():
#         print("第%d组--%s的值:%s" %(i+1,f,a[i][f]));
#     print("");

# for item in a:
#      index+=1;
#      for f in item.keys():
#          print("第%d组--%s的值:%s" %(index,f,item[f]));
#      print("");


# sum = 0
# for x in range(101):
#     sum += x
# print(sum)


#remove删除首个符合条件的元素，并不删除特定的索引。
n =[1,2,9,2,3,4,5]
while 2 in n:
    n.remove(2)
n.sort(reverse=True);
print(n)

#输出  [1, 2, 2, 4, 5]

#pop按照索引删除字符，返回值可以付给其他的变量，返回的是你弹出的那个数值。
n =[1,2,2,3,4,5]
a=n.pop(4)
print(a)
print(n)
#输出
4
[1, 2, 2, 3, 5]


#del按照索引删除字符，返回值不可以付给其他的变量。
n =[1,2,2,3,4,5]
del(n[3])
print (n)

#输出
[1, 2, 2, 4, 5]

def fab(x):
    while x>1:
        return x+fab(x-1);
    return 1;
print("%8s1到%d的和等于：%d" % ('*',100,fab(100)) );

def test(*params):
     print('参数长度是：',  len(params))
     print('第二个参数是：', params[1])

test(324,23,35,43,543,5,3,534,5348);
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(add_end());
print(add_end());

nums = [1, 2, 3]
n2=calc(*nums);
n3=calc(1,2,3);

print(n2);
print(n3);

def person(name, age, **kwe):
    print('name:', name, 'age:', age, 'other:', kwe)

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Adam', 45, **extra);

def trim(s):
    while s[:1]==' ':
        s=s[1:];
    while s[-1:]==' ':
        s=s[:-1];
    return s;

print(trim('   d 2  '));