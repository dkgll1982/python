#!/usr/bin/python3

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
print(time.ctime(os.path.getatime('E:\\100-航天智慧\\2-源码库\\python\\14-文件操作\\IO.py')))
# 获取最后一次修改时间
print(time.ctime(os.path.getmtime('E:\\100-航天智慧\\2-源码库\\python\\14-文件操作\\IO.py')))
# 获取创建时间
print(time.ctime(os.path.getctime('E:\\100-航天智慧\\2-源码库\\python\\14-文件操作\\IO.py'))) 
# 获取文件大小
print(os.path.getsize('E:\\100-航天智慧\\2-源码库\\python\\14-文件操作\\IO.py'))
# 判断是否为文件
print(os.path.isfile('E:\\100-航天智慧\\2-源码库\\python\\14-文件操作\\IO.py')) # True
# 判断是否为目录
print(os.path.isdir('E:\\100-航天智慧\\2-源码库\\python\\14-文件操作\\IO.py')) # False
# 判断是否为同一个文件
# print(os.path.samefile('E:\\100-航天智慧\\2-源码库\\python\\14-文件操作\\IO.py', './E:\\100-航天智慧\\2-源码库\\python\\14-文件操作\\IO.py')) # True