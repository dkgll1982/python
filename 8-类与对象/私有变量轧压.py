#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-07-31 13:56:54 
# @Last Modified by: guojun 
# @Last Modified time: 2019-07-31 13:56:54 
# @Software: vscode 
class Info:
    def __init__(self):
        self.__name = 'jay'
    def __say(self):
        print(self.__name)

#访问方式:
a = Info()
print(a._Info__name)  # 'jay'
print(a._Info__say()) # 'jay'
print(a.__dict__)
print(dir(a))

print('-'*40)

class Secretive:  
    def __inaccessible(self):  #双下划线表示私有方法  
        print("Bet you can't see me...")  
    def accessible(self):  
        print("The secret message is:")
        # __xxx    类中的私有变量/方法名 （Python的函数也是对象，所以成员方法称为成员变量也行得通。）," 双下划线 " 开始的是私有成员，
        # 是只有类对象自己能访问，连子类对象也不能访问到这个数据。
        self.__inaccessible()  

s = Secretive()  
#s.__inaccessible() #私有方法从外界是无法访问的，报错
s.accessible()