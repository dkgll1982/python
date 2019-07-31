#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-24 22:17
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 变量作用域
# @Software: PyCharm

def text():
    demo = 'C语言中文网'
    print(demo)
text()
#此处获取局部变量值会引发错误
#print('局部变量 demo 的值为：',demo)

print('-'*40)

demo = 'python编程'
def text():
    global demo
    demo = 'C语言中文网'
    print(demo)
text()

#此处获取局部变量值会引发错误
print('全局变量 demo 的值为：',demo)

print('-'*40)
def test(arg):
    a=1
    b=2
    data_dict = {}
    print(locals())
    print(globals())

if __name__ == '__main__':
    test(3)


print('-'*40)
def foo(arg, a):
    x = 1
    y = 'xxxxxx'
    # for i in range(10):
    #     j = 1
    #     k = i
    print(    locals())

    locals()['x']=100

    print(locals());
    print(locals()['x'])
    print(x);
    print(globals()['x'])

x=122222
# 调用函数的打印结果
foo(1, 2)

print('-'*40)
print(locals()['x'])
print(globals())

print('-'*40)
global name;
name="查叫天"
def foo ():
    # 局部变量name
    name = 'Charlie'
    def bar ():
        nonlocal name
        # 访问bar函数所在的foo函数的name局部变量
        print(name) # Charlie
        name = '孙悟空'
        print(name) # 孙悟空
    bar()
foo()
print(name)