#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import time
from datetime import datetime

li=[1,2,3,4,5,6,7,100];
li1 = ['name', 'quest', 'favorite color', 'quest', 'favorite color', 'quest', 'favorite color', 'quest', 'favorite color', 'quest', 'favorite color']
li2=['lancelot', 'the holy grail', 'blue'];
for x in range(12):
    li.insert(x+7, x+8);
del li[7];
for y in li:
    print(y);

time2=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime());
di={
    "name":"张三",
    "age":12,
    "sex":"男",
    "birthday":time2
}
di3={
    "name":"张三ssss",
    "age":122,
    "sex":"男4",
    "birthday":time2
}

#for i,t in di.items():
for i,t in zip(reversed(li),reversed(li1)):
    print(str(i)+'-->'+t);

def fub(b):
    print ("你输入的参数是："+b);

if __name__ == '__main__':
    fub(input("请输入参数:"));

