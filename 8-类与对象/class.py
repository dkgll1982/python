#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
    '所有员工的基类'
    __age = 20

    def getage(self):
        return  self.__age;
    def setage(self,newage):
        self.__age=newage;
    empCount = 0
    name="张三李四王二麻子"
    def __init__(fg, name, salary):
        fg.name = name+'(私)'
        fg.salary = salary
        Employee.empCount += 1
        print("类的初始化方法")
    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)
    def displayEmployee(self):
        name="私有的名字";
        print("self.Name : ", self.name, "，Employee.Name : ", Employee.name, "，private.Name : ", name,", Salary: ", self.salary,", age:",self.__age)


"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
emp1.name="dfgdf帆帆帆帆等等"

emp1.setage(123)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp2._Employee__age=23423424242;
#emp1.displayEmployee()


Employee.name='2242424242'
#emp2.displayEmployee()
#print(emp2._Employee__age);
#print(emp1.getage());
#print(emp2.getage())
#print("Total Employee %s" % Employee.name)
#emp1.displayCount()

emp1.age = 7
emp1.age = 8
del emp1.age

# hasattr(emp1, 'age')
# getattr(emp1, 'age')
# setattr(emp1, 'age', 8)
# delattr(emp1, 'age')