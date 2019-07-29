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