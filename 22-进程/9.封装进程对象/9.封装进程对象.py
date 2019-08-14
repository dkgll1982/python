#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-10 19:12:54 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-10 19:12:54 
# @Software: vscode 

from  sunProcess import sunProcess,sunProcess2; 

if __name__ == "__main__":
    print("父进程启动")

    #创建子进程
    p = sunProcess("test");
    #自动调用p进程对象run方法
    p.start();
    p.join();

    #创建子进程
    p2 = sunProcess2("test");
    #自动调用p进程对象run方法
    p2.start();
    p2.join();

    print("父进程结束")