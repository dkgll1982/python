#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-28 20:34
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : supper超类
# @Software: PyCharm

class Employee :
    salary =10000;
    def __init__ (self, salary):
        self.salary = salary
    def work (self):
        print('普通员工正在写代码，工资是:', self.salary)
class Customer:
    def __init__ (self, favorite, address):
        self.favorite = favorite
        self.address = address
    def info (self):
        print('我是一个顾客，我的爱好是: %s,地址是: %s' % (self.favorite, self.address))

# Manager继承了Employee、Customer
#class Manager (Employee, Customer):
class Manager (Customer, Employee):
    pass

#m = Manager(25000)
m = Manager('IT产品', '广州')
#m.work(11111111)
m.info()
print(m.__dir__())

print('-'*40)

# Manager继承了Employee、Customer
class Manager(Customer,Employee):
    # 重写父类的构造方法
    def __init__(self, salary, favorite, address):
        print('--Manager的构造方法--')
        # 通过super()函数调用父类的构造方法
        #super.__init__(favorite, address + '下级单位')
        Customer.__init__(self,favorite, address+'下级单位')
        # 与上一行代码的效果相同
        #super(Manager, self).__init__(salary)
        # 使用未绑定方法调用父类的构造方法
        Employee.__init__(self, salary+100)
        #super(Manager,self).__init__(salary)
# 创建Manager对象
m = Manager(25000, 'IT产品', '广州');
m.work();
m.info();

print('-------------------------')

class A():
    def go(self):
        print ("go A go!")
    def stop(self):
        print ("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")
class B(A):
    def go(self):
        super(B, self).go()
        print ("go B go!")
class C(A):
    def go(self):
        super(C, self).go()
        print ("go C go!")
    def stop(self):
        super(C, self).stop()
        print ("stop C stop!")
class D(B,C):
    def go(self):
        super(D, self).go()
        print ("go D go!")
    def stop(self):
        super(D, self).stop()
        print ("stop D stop!")
    def pause(self):
        print ("wait D wait!")
class E(B,C):
    pass
a = A()
b = B()
c = C()
d = D()
e = E()
# 说明下列代码的输出结果
a.go()                  #"go A go!"
print('--------')
b.go()                  #"go A go!"  "go B go!"
print('--------')
c.go()                  #"go A go!"  "go C go!"
print('--------')
d.go()                  ##"go A go!"  go C go!" "go B go!"  "go D go!"
print('--------')
e.go()                  #"go A go!"  "go B go!"
print('--------')
a.stop()                #"stop A stop!"
print('--------')
b.stop()                #"stop A stop!"
print('--------')
c.stop()                #"stop A stop!" "stop C stop!"
print('--------')
d.stop()                #"stop A stop!" "stop C stop!" "stop D stop!"
print('--------')
e.stop()                #"stop A stop!"  "stop C stop!"
print(D.mro())
