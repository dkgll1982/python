#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
#详见 https://www.runoob.com/python/python-json.html
dicts={"name":"lucy","age":12,"sex":"boy"}
#将 Python 对象编码成 JSON 字符串
json_dicts=json.dumps(dicts,indent=4,sort_keys=True, separators=(',', '——'))
print(json_dicts)

'所有员工的基类'
class employee(object):
    '所有员工的基类'
    empCount = 0
    def __init__(self, name, salary):
        print('自动初始化__init__方法！！！')
        self.__name = name
        self.salary = salary
        employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % employee.empCount)
    def displayEmployee(self):
        print("Name : ", self.__name, ", Salary: ", self.salary)

print('-------------------------------------------------------')
emp =employee("张三",18000);
emp._employee__name='李四'
emp.displayEmployee()
print('-------------------------------------------------------')

print(emp.salary);
print(emp.empCount)
print("Employee.__doc__:", employee.__doc__)
print("Employee.__name__:", employee.__name__)
print("Employee.__module__:", employee.__module__)
print("Employee.__bases__:", employee.__bases__)
print("Employee.__init__:", employee.__init__)
print("Employee.__weakref__:", employee.__weakref__)
print("Employee.__dict__:", employee.__dict__)