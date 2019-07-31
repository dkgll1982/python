#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-07-29 23:10:58 
# @Last Modified by: guojun 
# @Last Modified time: 2019-07-29 23:10:58 
# @Software: vscode 

# 在动态检查对象是否包含某些属性（包括方法〉相关的函数有如下几个：
# hasattr(obj, name)：检查 obj 对象是否包含名为 name 的属性或方法。
# getattr(object, name[, default])：获取 object 对象中名为 name 的属性的属性值。
# setattr(obj, name, value，/)：将obj 对象的 name 属性设为 value。

class Comment:
    def __init__ (self, detail, view_times):
        self.detail = detail
        self.view_times = view_times
    def info ():
        print("一条简单的评论，内容是%s" % self.detail)
       
c = Comment('疯狂Python讲义很不错', 20)
# 判断是否包含指定的属性或方法
print(hasattr(c, 'detail')) # True
print(hasattr(c, 'view_times')) # True
print(hasattr(c, 'info')) # True
# 获取指定属性的属性值
print(getattr(c, 'detail')) # '疯狂Python讲义很不错'
print(getattr(c, 'view_times')) # 20
# 由于info是方法，故下面代码会提示：name 'info' is not defined
#print(getattr(c, info, '默认值'))
# 为指定属性设置属性值
setattr(c, 'detail', '天气不错')
setattr(c, 'view_times', 32)
# 输出重新设置后的属性值
print(c.detail)
print(c.view_times)
#设置不存在的属性，即为对象添加属性
setattr(c, 'test', '新增的测试属性')
print(c.test) # 新增的测试属性

#重新设置对象的方法时， 新设置的方法是未绑定方法
def bar ():
    print('一个简单的bar方法')
# 将c的info方法设为bar函数   
setattr(c, 'info', bar)
c.info() 

#函数将 info() 方法设置成普通值，这样将会把 info 变成一个属性，而不是方法,如下设置为字符串'fkit' 
setattr(c, 'info', 'fkit')
c.info()                    #TypeError: 'str' object is not callable