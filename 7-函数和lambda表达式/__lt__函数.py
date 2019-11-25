#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: guojun
# @Company: 航天神舟智慧系统技术有限公司
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2019-11-22 15:51:20
# @Last Modified by: guojun
# @Last Modified time: 2019-11-22 15:51:20
# @Software: vscode

#Python3中已经不能使用cmp()函数了，被如下五个函数替代: 
#import operator       #首先要导入运算符模块
#operator.gt(1,2)      #意思是greater than（大于）
#operator.ge(1,2)      #意思是greater and equal（大于等于）
#operator.eq(1,2)      #意思是equal（等于）
#operator.le(1,2)      #意思是less and equal（小于等于）
#operator.lt(1,2)      #意思是less than（小于）

#比较函数：
#<	object.__lt__(self, other)
#<=	object.__le__(self, other)
#==	object.__eq__(self, other)
#!=	object.__ne__(self, other)
#>=	object.__ge__(self, other)
#>	object.__gt__(self, other)

#Python的基类object提供一系列可以用于实现同类对象进行“比较”的方法，可以用于同类对象的不同实例进行比较。他们也是实例方法，定义如下：
#object.lt(self, other)
#object.le(self, other)
#object.eq(self, other)
#object.ne(self, other)
#object.gt(self, other)
#object.ge(self, other)
#其中self是指对象自身，other是参与比较的另一对象，返回值最好为bool值，也可以是任意值。
#以上这些方法，object类实现了__eq__和__ne__两个方法，lt、le、gt、__ge__这些方法默认返回值为“NotImplemented”，
#需要自定义类实现这些方法才能正确使用这些方法，当然__eq__和__ne__这两个方法也可以重写。
#原文链接：https://blog.csdn.net/LaoYuanPython/article/details/95042104

class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        return

    def __str__(self):
        return self.name + ":" + str(self.age)

    def __lt__(self, other):
        return self.name < other.name if self.name != other.name else self.age < other.age


if __name__ == "__main__":

    print("\t".join([str(item) for item in sorted(
        [People("abc", 18), People("abe", 19), People("abe", 12), People("abc", 17)])]))

    s = sorted([People('张三',99),People('李四',53),People('王五',43),People('张三',34),People('张三',23)])
    for x in s:
        print(x)
 
    #当用运算符进行对象比较时也会被调用，运算符号与方法名称的对应关系如下：x<y 调用 x.__lt__(y)、
    # x<=y 调用 x.__le__(y)、x==y 调用 x.__eq__(y)、x!=y 调用 x.__ne__(y)、x>y 调用 x.__gt__(y)、
    # x>=y 调用 x.__ge__(y)。
    x,y = 1,2
    print(x.__lt__(2))