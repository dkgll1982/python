#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-01-06 15:08:31 
# @Last Modified by: guojun 
# @Last Modified time: 2020-01-06 15:08:31 
# @Software: vscode 

#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开文件
fo = open(r"backup\1.txt", "wb")
print("文件名为: %s,文件描述符为:%d"%(fo.name,fo.fileno()))
# 关闭文件
fo.close()

# 打开文件
fo = open(r"backup\zip.zip", "r")
print("文件名为: %s,文件描述符为:%d"%(fo.name,fo.fileno()))
# 关闭文件
fo.close()