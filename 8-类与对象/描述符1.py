#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-10-20 21:14:53 
# @Last Modified by: guojun 
# @Last Modified time: 2019-10-20 21:14:53 
# @Software: vscode 
#!/usr/bin/env python
 
#某个类，只要是内部定义了方法 __get__, __set__, __delete__ 中的一个或多个，就可以称为描述符 
#描述符类
#对象属性的访问顺序： 
#①.实例属性 
#②.类属性 
#③.父类属性 
#④.__getattr__()方法 

class Desc(object):
    
    def __get__(self, instance, owner):
        print("__get__...")
        print("self : \t\t", self)
        print("instance : \t", instance)
        print("owner : \t", owner)
        print('='*40, "\n")
        
    def __set__(self, instance, value):
        print('__set__...')
        print("self : \t\t", self)
        print("instance : \t", instance)
        print("value : \t", value)
        print('='*40, "\n") 

class TestDesc(object):
    #类的属性
    #def __getattribute__(self,object):
    #    print('TestDecs的方法')
    #类的属性
    x = Desc()

#以下为测试代码
t = TestDesc()
t.x 

#以下为输出信息：

#__get__...
#self :          <__main__.Desc object at 0x0000000002B0B828>
#instance :      <__main__.TestDesc object at 0x0000000002B0BA20>
#owner :         <class '__main__.TestDesc'> 
#========================================