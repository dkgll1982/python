#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-03 11:20
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 元类2
# @Software: PyCharm

echo=print

# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    """
    :param a:
    :param b:
    :return:
    """
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

c = MyList();
c.add("我是张三");

# 定义Item元类，继承type
class ItemMetaClass(type):
    # cls代表动态修改的类
    # name代表动态修改的类名
    # bases代表被动态修改的类的所有父类
    # attr代表被动态修改的类的所有属性、方法组成的字典
    def __new__(cls, name, bases, attrs):
        # 动态为该类添加一个cal_price方法
        attrs['cal_price'] = lambda self: self.price * self.discount
        return type.__new__(cls, name, bases, attrs)

# 定义Book类
class Book(metaclass=ItemMetaClass):
    __slots__ = ('name', 'price', '_discount')
    def __init__(self, name, price):
        self.name = name
        self.price = price
    @property
    def discount(self):
        return self._discount
    @discount.setter
    def discount(self, discount):
        self._discount = discount

# 定义cellPhone类
class CellPhone(metaclass=ItemMetaClass):
    """
    :metaclass ItemMetaClass: 
    :return:
    """ 
    __slots__ = ('price', '_discount' )
    def __init__(self, price):
        self.price = price
    @property
    def discount(self):
        return self._discount
    @discount.setter
    def discount(self, discount):
        self._discount = discount        

b = Book("Python基础教程", 89)
b.discount = 0.76
# 创建Book对象的cal_price()方法
print(b.cal_price())
cp = CellPhone(2399)
cp.discount = 0.85
# 创建CellPhone对象的cal_price()方法
print(cp.cal_price())

print(CellPhone.__dict__)

print(CellPhone)
print(hasattr(CellPhone,"_discount")) 
print(cp._discount) 

print('-'*40)

class_example = type('class_example', (), {'attr': 1,"name":"张三"})
print(class_example.__dict__)
child_example = type('child_example', (class_example,), {"name":"李四","age":38})
print(child_example.__dict__)
#动态创建包括方法的类
def childfunc(self):
    print("子类方法属性",self.attr)
    pass;

#type(类名,父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)    
#为你的类增加方法。只需要定义一个有着恰当签名的函数（func）并将其作为属性赋值（childfunc）就可以了。
child_example = type('child_example', (class_example,), {"name":"李四","age":38,"func":childfunc})
print(child_example.__dict__)
child_example().func();
#我们也可以先动态创建一个class，然后再赋给其新的方法：
child_example.newfunc = childfunc;

child_example().newfunc()

print('-'*40)

print(cp.discount.__class__)
print(ListMetaclass.__class__)
print(Book.__class__)
print(class_example.__class__)
print(child_example.__class__)
print(child_example.name.__class__)
print(b.__class__)
print(childfunc.__class__)

print('-'*40)

#所有的class都来自于type。type，作为metaclass，创建了以上所有的class object。
print(cp.discount.__class__.__class__)
print(ListMetaclass.__class__.__class__)
print(Book.__class__.__class__)
print(class_example.__class__.__class__)
print(child_example.__class__.__class__)
print(child_example.name.__class__.__class__)
print(b.__class__.__class__)
print(b.__class__.__class__.__class__)
print(childfunc.__class__.__class__)
echo(childfunc.__class__)         

print('-------------------------------------------')

# 元类会自动将你通常传给‘type’的参数作为自己的参数传入
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    '''返回一个类对象，将属性都转为大写形式'''
    #选择所有不以'__'开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))

    # 将它们转为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)
 
    # 通过'type'来做类对象的创建
    return type(future_class_name, future_class_parents, uppercase_attr) 
 
class Foo(metaclass = upper_attr): 
    # 我们也可以只在这里定义__metaclass__，这样就只会作用于这个类中
    bar = 'bip'


print(hasattr(Foo, 'bar'))
# 输出: False
print(hasattr(Foo, 'BAR'))
# 输出:True
 
f = Foo()
print(f.BAR)
# 输出:'bip' 

print('---------------------------------------------------')


#以下代码来自：https://www.jianshu.com/p/e017bc810702 （深刻理解Python中的元类(metaclass)
# 请记住，'type'实际上是一个类，就像'str'和'int'一样
# 所以，你可以从type继承
class UpperAttrMetaClass(type):
    # __new__ 是在__init__之前被调用的特殊方法
    # __new__是用来创建对象并返回之的方法
    # 而__init__只是用来将传入的参数初始化给对象
    # 你很少用到__new__，除非你希望能够控制对象的创建
    # 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
    # 如果你希望的话，你也可以在__init__中做些事情
    # 还有一些高级的用法会涉及到改写__call__特殊方法，但是我们这里不用
    def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return type(future_class_name, future_class_parents, uppercase_attr)

class UpperAttrMetaclass(type):
    def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)

        # 复用type.__new__方法
        # 这就是基本的OOP编程，没什么魔法
        return type.__new__(upperattr_metaclass, future_class_name, future_class_parents, uppercase_attr)       

class UpperAttrMetaclass(type):
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        #return type.__new__(cls, name, bases, uppercase_attr)
        return super(UpperAttrMetaclass, cls).__new__(cls, name, bases, uppercase_attr)

# 使用到元类的代码比较复杂，这背后的原因倒并不是因为元类本身，而是因为你通常会使用元类去做一些晦涩的事情，依赖于自省，控制继承等等。
# 确实，用元类来搞些“黑暗魔法”是特别有用的，因而会搞出些复杂的东西来。但就元类本身而言，它们其实是很简单的：