#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-10-21 14:28:00 
# @Last Modified by: guojun 
# @Last Modified time: 2019-10-21 14:28:00 
# @Software: vscode 

#对象属性的访问顺序： 
#①.实例属性 
#②.类属性 
#③.父类属性 
#④.__getattr__()方法 

class parent():
    name='王五'
    def __get__(self, instance, owner):
        self.name=parent.name
        return self.name
class Person(object):
    father='钱琦'
    def __init__(self,name,sex,age):
        #②.类属性 ，所有类的实例都可以访问到
        self.name=name
        self.sef=sex
        self.age=age
        self.father='马六'
    #③.父类属性   
    father = parent()

    #④.__getattr__()方法 
    def __getattr__(self,object):  
        return "我是一只小小鸟"

per = Person("张三",'男性',20) 

#__getattr__：当使用点号获取实例属性时，如果属性不存在就自动调用__getattr__方法。
print(per.name,per.age,per.father,per.你猜有值否)

print('-'*40)
print(Person.father)
print('*'*40)

#①.实例属性 
per.name='李四'
print(per.name,per.age)

print('-'*40)

class Dict(dict):
    
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

d = Dict(a=2)
print (d['a'])
print (d.a)             #调用类中原本没有定义的属性时候，调用__getattr__
d.a = 100               #对实例的属性进行赋值的时候调用__setattr__
print (d['a'])  

# -*- coding:utf-8 -*-
class Student:
    #如果不加该方法，如果调用的类属性不存在，会报AttributeError: 'XX' object has no attribute 'XX'的错误
    def __getattr__(self, item):
        return item + ' is not exits'
 
    def __setattr__(self, key, value):
        self.__dict__[key] = value
 
    def __getitem__(self, item):
        return self.__dict__[item]
 
    def __setitem__(self, key, value):
        self.__dict__[key] = value 
 
print('*'*40)

s = Student()
print(s.name)       # 调用__getattr__方法 输出'name is not exits'
s.age = 1           # 调用__setattr__ 方法
print(s.age)        # 输出 1
print(s['age'])     # 调用 __getitem__方法 输出1
s['name'] = 'tom'   # 调用 __setitem__ 方法
print(s['name'])    # 调用 __getitem__ 方法 输出 'tom'
 
print('='*40)

class A:
    att = 'abc'
    def __getattribute__(self, item):
        print("触发了 __getattribut__()")
        return object.__getattribute__(self, item) + ' from getattribute'

    def __getattr__(self, item):
        print("触发了 __getattr__() 方法")
        return item + " form getatter"

    def __get__(self, instance, owner):
        print("触发了 __get__()方法", instance, owner)
        return self

class B:
    a1 = A()

if __name__ == '__main__':
    a2 = A()
    b = B()
 
    print(a2.att)
    print('='*40)
    print(a2.ppppppppp)
    print('='*40)
    b.a1
    print('='*40)
    print(b.a1.att)