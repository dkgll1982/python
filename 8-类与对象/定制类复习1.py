#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-16 10:32
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 定制类
# @Software: PyCharm

class A(object):
    def __init__(self):
        self.name = "Bob"
        self.age = 18
        self.gender  = "male"

    def __getattribute__(self, attr):
        # 拦截age属性
        if attr == "age":
            return "问年龄是不礼貌的行为"
        # 非age属性执行默认操作
        else:
            return object.__getattribute__(self, attr)

    # 在实例化的对象进行.操作的时候（形如：a.xxx/a.xxx()），都会自动去调用__getattribute__方法。
    # 但是，如果某个属性在__getattribute__方法中未能找到，此时会调用__getattr__方法。        
    def __getattr__(self, attr):
        return ('\'%s\' is not defind!'%attr)

if __name__ == "__main__":
    a = A()
    # 如果我们想改变访问属性的逻辑，如执行a.age语句并非返回18，而是返回问年龄是不礼貌的行为。
    # 这里就可以用__getattribute__方法拦截属性，实现我们想要实现的逻辑。
    print(a.age)
    print(a.name)
    print(a.gender)
    print(a.gender2)

# 输出：
#问年龄是不礼貌的行为
#Bob
#male 