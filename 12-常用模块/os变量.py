#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-04 09:59:55 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-04 09:59:55 
# @Software: vscode 
import sys 
import os
python = os.path.dirname(sys.executable)    #解释器所在的文件夹
curpath = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(curpath, "sys变量.py") 

# 显示导入依赖模块的操作系统的名称
print(os.name)
# 获取PYTHONPATH环境变量的值
print(os.getenv('PYTHONPATH'))
# 返回当前系统的登录用户名
print(os.getlogin())
# 获取当前进程ID
print(os.getpid())
# 获取当前进程的父进程ID
print(os.getppid())
# 返回当前系统的CPU数量
print(os.cpu_count())
# 返回路径分隔符
print(os.sep)
# 返回当前系统的路径分隔符
print(os.pathsep)
# 返回当前系统的换行符
print(os.linesep)
# 返回适合作为加密使用的、最多3个字节组成的bytes
print(os.urandom(3))

# 在 os 模块中与进程管理相关的函数的功能：
import os
# 运行平台上的cmd命令
# os.system('cmd')    
# 使用Excel打开g:\abc.xls文件
os.startfile(r'backup\省科技中小企业_科技局.xls')
#os.spawnl(os.P_NOWAIT, 'D:\\Programing\\pdi-ce-8.1.0.0-365\\data-integration\\Spoon.bat', ' ')
# 使用python命令执行os_test.py程序
# os.execl(python+'\\'+'python.exe', " ", 'os_test.py', 'i')
os.execl(python+'\\'+'python.exe', " ", path, 'i')