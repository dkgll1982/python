#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-04 22:59:15 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-04 22:59:15 
# @Software: vscode 
import os;
from multiprocessing import Pool;
import os,time,random 

def copyFile(rPath,wPath):
    fr=open(rPath,"rb");
    fw=open(wPath,"wb")

    context = fr.read();
    fw.write(context);
    fr.close()
    fw.close()

path=r"images"
toPath=r"backup\copy"

# #读取path下的所有文件
# fileList = os.listdir(path);

# start =time.time();
# #启动for循环拷贝每一个文件
# for fileName in fileList:
#     copyFile(os.path.join(path,fileName),os.path.join(toPath,fileName))
# end =time.time()
# print("总耗时：%0.6f"%(end -start));

if __name__ == "__main__":
    #读取path下的所有的文件
    fileList = os.listdir(path)
 
    start = time.time()
    pp = Pool(4)
    for fileName in fileList:
        pp.apply_async(copyFile,args=(os.path.join(path,fileName),os.path.join(toPath,fileName)))
   
    #当进程池close的时候并未关闭进程池，只是会把状态改为不可再插入元素的状态，完全关闭进程池使用
    pp.close()          #关闭进程池，不再接受新的进程
    
    #进程池对象调用Join，会等待进程池所有子进程结束之后在去执行父进程
    pp.join()           #主进程阻塞等待子进程的退出
    end = time.time()
    print("总耗时：%0.6f"%(end -start));
