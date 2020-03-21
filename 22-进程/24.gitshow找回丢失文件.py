#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-03-27 13:20:53 
# @Remark: 人生苦短，我用python！

import sys,subprocess
import os 

class Trigger(object):
 
    def __init__(self):
        pass
    
    def getPushInfo(self): 
        file = open(r'backup/gitshow.txt')
        row_index = 0
        for line in file:
            row_index += 1 
            try: 
                p = subprocess.Popen(line,shell=True,stdout=subprocess.PIPE)
                pipe = p.stdout.readlines()     
                with open(r'backup/git/{}.py'.format(str(row_index)),'wb') as f:
                    f.writelines(pipe)
            except Exception as e:
                print('写入文件失败,原因：{}'.format(e)) 
                
        file.close() 

if __name__ == "__main__":
    Trig =Trigger()
    Trig.getPushInfo()