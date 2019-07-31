#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-07-31 11:53:59 
# @Last Modified by: guojun 
# @Last Modified time: 2019-07-31 11:53:59 
# @Software: vscode 

# 用 hasattr() 函数判断指定属性（或方法）是否存在，
# 但到底是属性还是方法，则需要进一步判断它是否可调用。程序可通过判断该属性（或方法）是否包含 __call__ 属性来确定它是否可调用。
class User:
    __age='32'
    def __init__(self, name, passwd):
        self.name = name
        self.passwd = passwd
        print("my name is ",self.name);
    def validLogin (self):
        print('验证%s的登录' % self.name)       
u = User('crazyit', 'leegang')
# 判断u.name是否包含__call__方法，即判断是否可调用
print(hasattr(u.name, '__call__')) # False
# 判断u.passwd是否包含__call__方法，即判断是否可调用
print(hasattr(u.passwd, '__call__')) # False
# 判断u.validLogin是否包含__call__方法，即判断是否可调用
print(hasattr(u.validLogin, '__call__')) # True
print(dir(User)) 
u.name=lambda self:print("my name is ",self);
print(hasattr(u.name, '__call__')) # True
u.name("ffff")

print('******************************************************')

def myfun(self): 
    print("call方法调用")
    def __call__():
        print("call方法调用2") 

fun = myfun("传参") 
myfun("传参")
myfun.__call__("传参") 

def foo ():
    print('--foo函数--')  
# 下面示范了2种方式调用foo()函数
foo()
foo.__call__()
print("foo的属性",dir(foo))
foo.__init__()
print(getattr(foo, '__init__')) # '疯狂Python讲义很不错'

print('******************************************************')

class Entity:
    '''调用实体来改变实体的位置。''' 
    def __init__(self, size, x, y):
        self.x, self.y = x, y
        self.size = size 
    def __call__(self, x, y):
        '''改变实体的位置'''
        self.x, self.y = x, y
        print("call方法调用")
        print(self.x);
        print(self.y);

e = Entity(1, 2, 3)     # 创建实例
e(4, 5)                 # 实例可以象函数那样执行，并传入x y值，修改对象的x y 
e.__call__(4,5)