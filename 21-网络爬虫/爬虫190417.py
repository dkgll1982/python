#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2018-08-17 17:56:00 
# @Last Modified by: guojun 
# @Last Modified time: 2018-08-17 17:56:00 
# @Software: vscode 

 
def fac(n): 
    return n+fac(n-1) if n>1 else 1; 

print(fac(100));



