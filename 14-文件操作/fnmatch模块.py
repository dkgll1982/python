#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-04 13:23:03 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-04 13:23:03 
# @Software: vscode 

import os
from pathlib import *
import fnmatch
rootdir = "."
#遍历文件夹   
def iter_files(rootDir):
    #遍历根目录
    for root,dirs,files in os.walk(rootDir):
        for file in files:
            file_name = os.path.join(root,file) 
            #fnmatch.fnmatch(filename, pattern)：判断指定文件名是否匹配指定 pattern
            if fnmatch.fnmatch(file_name, '*.py'):
                print(file_name)
iter_files(rootdir)