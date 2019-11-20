#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-10 19:10:34 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-10 19:10:34 
# @Software: vscode 

#参考链接：https://www.cnblogs.com/CJOKER/p/8295272.html

import logging
import os.path
import time
#第一步：创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO);
#第二步：创建一个Handler，写入日志文件
logpath = "C:\\Users\\dkgll\\Desktop\\python目录\\Logs\\"
logname=logpath+"3.txt"

fh = logging.FileHandler(logname,'w');
fh.setLevel(logging.INFO) #输出到file的log总开关

#日志输出-控制台和文件
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)  # 输出到console的log等级的开关

#第三步： 创建一个格式器formatter并将其添加到处理器handler
formatter = logging.Formatter("%(asctime)s - %(levelno)s - %(name)s - %(levelname)s - %(message)s - %(pathname)s")
fh.setFormatter(formatter)
#第四步：将Logger添加到Handler里面
logger.addHandler(fh);

ch.setFormatter(formatter)
logger.addHandler(ch)

logger.debug('this is a logger debug message')
logger.info('this is a logger info message')
logger.warning('this is a logger warning message')
logger.error('this is a logger error message')
logger.critical('this is a logger critical message')

import os 
try:
# 获取绝对路径
    print(os.path.abspath("abc.txt")) # G:\publish\codes\12\12.2\abc.txt
    # 获取共同前缀
    print(os.path.commonprefix(['/usr/lib', '/usr/local/lib'])) # /usr/l
    # 获取共同路径
    print(os.path.commonpath(['/usr/lib', '/usr/local/lib'])) # \usr
    # 获取目录
    print(os.path.dirname('abc/xyz/README.txt')) #abc/xyz
    # 判断指定目录是否存在
    print(os.path.exists('abc/xyz/README.txt')) # False
    # 获取最近一次访问时间
    fileName = 'E:\\100-航天智慧\\2-源码库\\python\\14-文件操作\\6-日志\\IO2.py'
    print(time.ctime(os.path.getatime(fileName)))
    # 获取最后一次修改时间
    print(time.ctime(os.path.getmtime(fileName)))
    # 获取创建时间
    print(time.ctime(os.path.getctime(fileName))) 
    # 获取文件大小
    print(os.path.getsize(fileName))
    # 判断是否为文件
    print(os.path.isfile(fileName)) # True
    # 判断是否为目录
    print(os.path.isdir(fileName)) # False
    # 判断是否为同一个文件
    print(os.path.samefile(fileName, fileName)) # True
except (SystemExit,KeyboardInterrupt):
    raise
except Exception:
    #如果需要将日志不上报错误，仅记录，可以将exc_info=False， 
    logger.error("Faild to open sklearn.txt from logger.error",exc_info = False)
    
logger.info("Finish")