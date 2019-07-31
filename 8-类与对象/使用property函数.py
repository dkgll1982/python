#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-28 15:44
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 使用property函数
# @Software: PyCharm

class Rectangle:
    # 定义构造方法
    def __init__(self, width, height):
        self.width = width
        self.height = height
    # 定义setsize()函数
    def setsize (self , size):
        size = self.width, self.height
    # 定义getsize()函数
    def getsize (self):
        return self.width, self.height
     # 定义getsize()函数
    def delsize (self):
        self.width, self.height = 0, 0
    # 使用property定义属性
    #语法格式：property(fget=None, fset=None, fdel=None, doc=None)
    #调用 property 也可传入 0 个（既不能读，也不能写的属性）、1 个（只读属性）、2 个（读写属性）、3 个（读写属性，也可删除）和 4 个（读写属性，也可删除，包含文档说明）参数。
    size = property(getsize, setsize, delsize, '用于描述矩形大小的属性')
# 访问size属性的说明文档
print(Rectangle.size.__doc__)
# 通过内置的help()函数查看Rectangle.size的说明文档
help(Rectangle.size)
rect = Rectangle(4, 3)
# 访问rect的size属性
print(rect.size) # (4, 3)
print(type(rect.size))
# 对rect的size属性赋值
rect.size = 9, 7
# 访问rect的width、height实例变量
print(rect.width) # 9
print(rect.height) # 7
# 删除rect的size属性
del rect.size
# 访问rect的width、height实例变量
print(rect.width) # 0
print(rect.height) # 0

print('-'*40)

class Person:
    # 定义构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def setperson(self,l):
        self.name=l["name"]+':set访问器'
        self.age=str(l["age"])+':set访问器'
    def getperson(self):
        return {"name":self.name,"age":self.age};

    listperson = property(getperson,setperson,None,"人口方法属性器");

print(Person.listperson.__doc__);

Person1 = Person("孙悟空",100);

print(Person1.listperson);
Person1.listperson = {'name': '者行孙', 'age': 1000}
print(Person1.name);
print(Person1.age);

print('-'*40)

class User :
    def __init__ (self, first, last):
        self.first = first
        self.last = last
    def getfullname(self):
        return self.first + ',' + self.last
    def setfullname(self, fullname):
        first_last = fullname.rsplit(',');
        self.first = first_last[0]
        self.last = first_last[1]
    # 使用property()函数定义fullname属性，只传入2个参数
    # 该属性是一个读写属性，但不能删除
    fullname = property(getfullname, setfullname)
u = User('悟空', '孙')
# 访问fullname属性
print(u.fullname)
# 对fullname属性赋值
u.fullname = '八戒,朱'
print(u.first)
print(u.last)

print('-'*40)
class Cell:
    # 使用@property修饰方法，相当于为该属性设置getter方法
    @property
    def state(self):
        return self._state
    # 为state属性设置setter方法
    @state.setter
    def state(self, value):
        if 'alive' in value.lower():
            self._state = 'alive'
        else:
            self._state = 'dead'
    # 为is_dead属性设置getter方法
    # 只有getter方法属性是只读属性
    @property
    def is_dead(self):
        return not self._state.lower() == 'alive'
c = Cell()
# 修改state属性
c.state = 'Alive'
# 访问state属性
print(c.state)
# 访问is_dead属性
print(c.is_dead)
print('-'*40)

class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 私有属性
        self.__number = 0

    # 获取私有属性值  number = p1.number 会执行这个函数
    @property
    def number(self):
        # 返回私有属性值
        return self.__number

    # 设置私有属性值  p1.number = 666
    @number.setter
    def number(self, value):
        # 设置__number的值
        self.__number = value

    # 删除私有属性  del p1.number 会执行这个函数
    @number.deleter
    def number(self):
        # 删除属性
        del self.__number

p1 = People('张三', 22)
# 正常的对象属性赋值
# 对象.属性名 = 属性值
p1.name = '李四'
# 获取对象的属性值
name = p1.name
# 删除对象的属性
del p1.name
# 私有属性升级版
# 会去执行@property装饰number函数，函数执行完成后返回一个结果
num = p1.number
print(num)
# 会去执行@number.setter装饰的number函数，在函数中设置__number属性的值
p1.number = 666
# 会去执行@property装饰number函数，函数执行完成后返回一个结果
print(p1.number)
# 会去执行@number.deleter装饰的number函数，在函数中会将__number属性删除
del p1.number
# 会去执行@property装饰number函数，函数执行完成后返回一个结果
print(p1.number)

print('-'*40)
