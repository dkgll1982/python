#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-17 22:20:05 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-17 22:20:05 
# @Software: vscode 

import threading,time

sem = threading.Semaphore(3)

def run():
    with sem:
        for i in range(5):
            print("%s--%d"%(threading.currentThread().name,i))
            time.sleep(1);

if __name__ == "__main__":
    for i in range(5):
        threading.Thread(target=run).start()
