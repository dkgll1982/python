#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : guojun
# @Company : 航天神舟智慧系统技术有限公司
# @Site    : https://user.qzone.qq.com/350606539/main
# @Date    : 2020-08-25 16:23
# @File    : test2
# @Software: PyCharm

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('self:', self)

    # 定义一个build方法，返回一个person实例对象，这个方法等价于Person()。
    @classmethod
    def build(cls):
        # cls()等于Person()        
        p = cls(name='张三',age=33) 
        cls.sex='男'
        print('cls:', cls)
        return p

if __name__ == '__main__':
    person = Person.build()
    print(person, person.name, person.age, person.sex)
    
    person = Person('擦擦擦',111)
    print(person, person.name, person.age)
    
    