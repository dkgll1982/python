#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-07-25 14:30:29 
# @Last Modified by: guojun 
# @Last Modified time: 2019-07-25 14:30:29 
# @Software: vscode 

class Person :
    '这是一个学习Python定义的一个Person类'
    # 下面定义了一个类变量
    name = "李四"
    hair = 'black'
    def __init__(guojun, name = 'Charlie', age=8,sex ="男"):
        # 下面为Person对象增加2个实例变量
        guojun.name = "姓名:"+name
        guojun.age = "年龄:"+str(age)
        guojun.sex = "性别:"+sex
        name='王五'
    # 下面定义了一个say方法
    def say(zihan, content):
        print(content,zihan.name,zihan.age)
    print(name)

person1= Person();
d =person1.say(content='1')
print(person1.age)
print(person1.name)
print(person1.hair)
print(person1.sex)

person1.skills = ['programming', 'swimming']
print(person1.skills)

#使用实例对象引用属性稍微复杂一些，因为实例对象可引用类属性以及实例属性。但是实例对象引用属性时遵循以下规则：

#总是先到实例对象中查找属性，再到类属性中查找属性；
#属性绑定语句总是为实例对象创建新属性，属性存在时，更新属性指向的对象。

# 删除p对象的name实例变量
print('-------删除属性name前，查询出的是实例对象的name值')
print(person1.name)  # AttributeError
del person1.name
# 再次访问p的name实例变量
print('-------删除属性name后，查询出的是类对象的name值')
print(person1.name)  # AttributeError

print('-'*40)
# 先定义一个函数
def info(self):
    print("---info函数---", self)
# 使用info对p的foo方法赋值（动态绑定方法）
p = Person()
p.foo = info
# Python不会自动将调用者绑定到第一个参数，
# 因此程序需要手动将调用者绑定为第一个参数
p.foo(p)  # ①
# 使用lambda表达式为p对象的bar方法赋值（动态绑定方法）
p.bar = lambda self: print('--lambda表达式--', self)
p.bar(p) # ②

#如果希望动态增加的方法也能自动绑定到第一个参数，则可借助于 types 模块下的 MethodType 进行包装
print('-'*40)
from types import MethodType

p.foot =MethodType(info,p);
p.foot();

print('-'*40)
class Dog:
    # 定义一个jump()方法
    def jump(self):
        print("正在执行jump方法")
    # 定义一个run()方法，run()方法需要借助jump()方法
    def run(self):
        # 使用self参数引用调用run()方法的对象
        self.jump()
        print("正在执行run方法")
dog =Dog();
dog.jump();
dog.run();

#实际上，当通过 Dog 类调用 jump() 实例方法时，Python 只要求手动为第一个参数绑定参数值，并不要求必须绑定 Dog 对象，因此也可使用如下代码进行调用：
Dog().jump()

dog.jump=lambda x,y:print('x*y:%d'%(x*y));
dog.jump(1,2);

class ReturnSelf :
    def grow(self):
        if hasattr(self, 'age'):
            self.age += 1
        else:
            self.age = 1
        # return self返回调用该方法的对象
        return self
rs = ReturnSelf()
# 可以连续调用同一个方法
rs.grow().grow().grow()
print("rs的age属性值是:", rs.age)