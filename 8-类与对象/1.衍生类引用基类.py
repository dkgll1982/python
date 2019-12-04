#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-09 16:37:43 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-09 16:37:43 
# @Software: vscode 

class Animas():
    def __init__(self,animal_name,animal_age):
        self.name = animal_name
        self.age = animal_age
    def run(self):
        print(self.name.title()," is running")
    
class Dogs(Animas):
    def __init__(self,dog_name,dog_age):
        super().__init__("My pet "+dog_name.title(),dog_age)
        print('父类属性：',self.name,self.age)

Mycat = Animas("lucy",5)
print(Mycat.name.title(),' is ',Mycat.age, ' years old.')
Mycat.run()

Mydog = Dogs("lily",15)
print(Mydog.name.title(),' is ',Mydog.age, ' years old.')
Mydog.run() 