#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-07-29 17:33:18 
# @Last Modified by: guojun 
# @Last Modified time: 2019-07-29 17:33:18 
# @Software: vscode 

class Animal:
    def __init__(self,name):
        self.name = name
 
    def talk(self):
        pass

    @staticmethod  #静态方法使不需要实例化就可以调用。实现了一种接口，多种实现，可以后续对象可以重复调用这个接口
    def animal_talk(self):
        self.talk()
 
class Cat(Animal):
    def talk(self):
        print('Meow')
 
class Dog(Animal):
    def talk(self):
        print('Woof Woof') 
 
d = Dog('asd')
d.talk()
 
c = Cat('zxc')
c.talk()
 
#能不能通过一种接口，使它们都可以叫
Animal.animal_talk(c)
Animal.animal_talk(d) 

print('-'*40)

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):  
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型

print(isinstance(c, Animal))
print(isinstance(c, Dog))

def run_twice(animal):
    animal.run() 

run_twice(c)
run_twice(b)
run_twice(Cat())

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

run_twice(Tortoise())        
