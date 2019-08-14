#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-04 22:59:15 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-04 22:59:15 
# @Software: vscode 

import os,time,random 
from 下载文件方法 import get_person,save_excel

def run(arg1,arg2): 
    start = time.time()
    li = get_person(arg1);
    save_excel(li,arg2);
    end = time.time() 
    print("")
    print("导入"+arg2+"数据完成！！！""总耗时：%0.6f"%(end -start)); 

if __name__ == "__main__":  
    run("201","刑满释放");
    run("202","社区矫正");
    run("203","精神病");
    run("204","吸毒");
    run("206","信访");
    run("207","重点青少年");
    run("208","邪教");
    run("209","传销");
