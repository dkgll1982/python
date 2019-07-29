#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-28 15:18
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 类变量和实例变量
# @Software: PyCharm

class Address :
    detail = '广州'
    post_code = '510660'
    def info (self):
        # 尝试直接访问类变量
        #print(detail) # 报错
        # 通过类来访问类变量
        print(self.detail) # 输出 广州
        print(self.post_code) # 输出 510660
# 通过类来访问Address类的类变量
print(Address.detail)
addr = Address()
addr.info()

print('-------------------------------------------------');

# 修改Address类的类变量
Address.detail = '佛山'
Address.post_code = '460110'
addr.info()

# 通过实例对 detail、post_code 变量赋值，看上去很像是对类变量赋值，但实际上不是，而是重新定义了两个实例变量（如果第一次调用该方法）。

# 上下边程序在调用 Address 对象的 info() 方法之后，访问 Address 对象的 detail、post_code 变量，由于该对象本身己有这两个实例变量，
# 因此程序将会输出该对象的实例变量的值；接下来程序通过 Address 访问它的 detail、post_code 两个类变量，此时才是真的访问类变量。

addr.detail="武汉"
addr.post_code="222222"

addr.info()
#如果程序对一个对象的实例变量进行了修改，这种修改也不会影响类变量和其他对象的实例变量。例如如下代码：
print(Address.detail);
print(Address.post_code)

# 如果程序通过类修改了两个类变量的值，程序中 Address 的实例变量的值也不会受到任何影响。例如如下代码：
# 修改Address类的类变量
Address.detail = '江苏'
Address.post_code = '410110'

print(addr.detail);
print(addr.post_code)