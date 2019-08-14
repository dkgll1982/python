#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-10 19:10:44 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-10 19:10:44 
# @Software: vscode 

import os;
from multiprocessing import Process;
import os,time,random 

class sunProcess(Process):
    def __init__(self,name):
        Process.__init__(self);
        self.name = name

    #重写Process类的run方法    
    def run(self):
        print("子进程启动（%s-%s） "%(self.name,os.getpid()))
        #子进程的功能
        time.sleep(3);
        print("子进程结束（%s-%s） "%(self.name,os.getpid()))
 
class sunProcess2(Process):
    def __init__(self,name):
        Process.__init__(self);
        self.name = name

    #重写Process类的run方法    
    def run(self):
        print("子进程2启动（%s-%s） "%(self.name,os.getpid()))
        #子进程的功能
        time.sleep(3);
        print("子进程2结束（%s-%s） "%(self.name,os.getpid()))
 