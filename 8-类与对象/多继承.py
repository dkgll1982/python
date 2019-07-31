#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2018-07-29 16:41:31 
# @Last Modified by: guojun 
# @Last Modified time: 2018-07-29 16:41:31 
# @Software: vscode 

class Animal(object):
    __slots__ = ('gettype','age2',"fuwnc","gettde")  # 用tuple定义允许绑定的属性名称
    __name='';
    name='父类的名字'
    def __init2__(self):
        __name='11'
        #print("初始化方法")
        return __name
    def speak(self,tag):
        print("Hello, I'm is Animal."+tag)

class Cat(Animal):
    def speak(self,tag):
        #super().speak(tag)
        print("Hello, I'm is Cat."+tag)

class Dog(Animal):
    __slots__ = ('gettype','ag3e',"fuwnc","gettdpe")  # 用tuple定义允许绑定的属性名称
    def speak(self,tag):
        #super().speak(tag)
        print("Hello, I'm is Dog."+tag)

class Botany(Cat,Dog):
    name='子类的名字';
    #def speak(self,tag):
    #    super().speak(tag)
    #    print("Hello, I'm is Botany, HaHaHa."+tag)

def func(func):
    print('类别：'+str(type(func)));

def start_perform(animal,tag):
    r = animal();
    r.speak(tag)

class Student(object):
    __slots__ = ('name', 'age','score') # 用tuple定义允许绑定的属性名称

s = Student();
s.name="的地方大师傅但是是否是";
s.score="234"

print(s.name) 
Animal.namef='2323242433242432';

a=Dog();
b=Botany();
c=Animal();
c.gettype=func;
a.speak('1');
print('-'*40)
#多重继承顺序：Botany,Dog,Cat,Animal
b.speak('2');
print('-'*40)
print(a.namef)

start_perform(Botany,'***')


b.name="外部的名字"
print(b.name);
del b.name
print(b.name)

print()
print(isinstance(a,(Cat,Dog)))
print(isinstance(b,Animal) and isinstance(b,object) and isinstance(b,Cat) and isinstance(b,Dog))

print(isinstance(a,(type,Animal,Dog,Cat,Botany)));

print(dir(str))
print(hasattr(c,'__named'));

a=Animal().__init2__()+Animal().__init2__();

def hasattribute(cla):
    if(hasattr(cla,"__init2__")):
        return int(cla().__init2__());
    return None;

b=hasattribute(Animal)+hasattribute(Animal);

print(b)