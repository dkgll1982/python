#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-04 15:33:51 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-04 15:33:51 
# @Software: vscode 
import time

def main():
    for i in range(10):
        print("当前时间: %s" % time.ctime())
        # 调用sleep()函数让当前线程暂停1s
        time.sleep(1)

        def hello():
            print("hello, world")
    from threading import Timer
    # 指定10秒后执行hello函数
    t = Timer(7.0, hello)
    t.start() 

if __name__ == '__main__':
    main()
