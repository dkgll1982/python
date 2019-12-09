#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import getpass 

name = input("请输入用户名：") 
pwd = getpass.getpass("请输入密码：") 
print(name, pwd)
