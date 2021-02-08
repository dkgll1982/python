#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2021-02-08 15:29:39 
# @Remark: Life is short, I use python！ 
# @Software: vscode 
# 参考链接：https://blog.csdn.net/d1240673769/article/details/105728277

from pybloom_live import BloomFilter
import os
import hashlib
import time
import datetime
import os 

# 获取文件当前所在的目录，并返回完整文件全路径 
def realpath(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

#去重
class BloomCheckFunction(object):
    def __init__(self):
        self.filename = 'bloomFilter.blm'
        is_exist = os.path.exists(self.filename) #判断文件是否存在
        if is_exist:
            self.bf = BloomFilter.fromfile(open(self.filename, 'rb')) #存在直接打开 储存在内存中
        else:
            self.bf = BloomFilter(100000000, 0.001) #新建一个 储存在内存中

    def process_item(self, data):
        data_encode_md5 = hashlib.md5(data.encode(encoding='utf-8')).hexdigest()
        if data_encode_md5 in self.bf:
            # 内容没有更新 丢弃item return False
            return False

        else:
            self.bf.add(data_encode_md5)
            #内容不存在，新来的 return True
            return True

    def save_bloom_file(self):
        self.bf.tofile(open(self.filename, 'wb'))


#获取文件时间
def get_filename():
    h=datetime.datetime.now()-datetime.timedelta(hours=9)
    filename=h.strftime('%m%d%H')+".log"
    logname="process_"+h.strftime('%m%d')+".log"
    return filename,logname

#删除历史文件
def delFile():
    h=datetime.datetime.now()-datetime.timedelta(hours=33)#可根据硬盘空间大小，确定需要保留多久的数据，这里保留最近24小时的日志文件
    del_srcfile=realpath(r"/data/logs/"+h.strftime('%m%d%H')+".log")
    del_dbfile=realpath(r"/data/dblog/"+h.strftime('%m%d%H')+".log")
    #print(del_srcfile)
    if os.path.exists(del_dbfile):
        os.remove(del_dbfile)
        if os.path.exists(del_srcfile):
            os.remove(del_srcfile)
    
def process_data(srcfile,dstfile):
    bf = BloomCheckFunction()#对象初始化 只需要初始化一遍
    with open(dstfile,'w') as fout:        
        with open(srcfile,'r') as fin:
            for line in fin:
                if bf.process_item(line):
                    fout.write(line)
                else:
                    pass

if __name__=="__main__":
    start_time=time.time()
    filename,logname=get_filename()
    srcfile=realpath(r"data/logs/"+filename)
    dstfile=realpath(r"data/dblog/"+filename)
    if os.path.exists(srcfile):
        try:
            delFile()
            process_data(srcfile,dstfile)
            spend_time=time.time()-start_time
            with open(realpath('data/'+logname),"a+") as fin:
                fin.write("file "+srcfile+" process success , spend times: %.3f s\n" % spend_time)
        except:
            with open(realpath('data/'+logname),"a+") as fin:
                fin.write("file "+srcfile+" process failed")
    else:
        with open(logname,"a+") as fin:
                fin.write("file "+srcfile+" not exist !!!")


