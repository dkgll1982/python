#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: guojun
# @Company: 航天神舟智慧系统技术有限公司
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2019-08-04 22:59:15
# @Last Modified by: guojun
# @Last Modified time: 2019-08-04 22:59:15
# @Software: vscode
import os
from multiprocessing import pool
import os
import time
import random


def copyFile(rPath, wPath):
    fr = open(rPath, "rb")
    fw = open(wPath, "wb")

    context = fr.read()
    fw.write(context)
    fr.close()
    fw.close()


path = r"images"
toPath = r"backup\copy"

# 读取path下的所有文件
fileList = os.listdir(path)

start = time.time()
# 启动for循环拷贝每一个文件
for fileName in fileList:
    copyFile(os.path.join(path, fileName), os.path.join(toPath, fileName))
end = time.time()
print("总耗时：%0.6f" % (end - start))
