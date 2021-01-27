#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-04-16 12:49:56 
# @Remark: 人生苦短，我用python！
# 参考链接：https://www.lagou.com/lgeduarticle/82320.html

import execjs
import sys
import os  

# 获取文件当前所在的目录，并返回完整文件全路径 
def realpath(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

def get_js():
    # 打开JS文件
    f = open(realpath("a.js"), 'r', encoding='utf-8')
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr

def get_des_psswd(acc, code):
    jsstr = get_js()
    #  加载JS文件
    ctx = execjs.compile(jsstr)
    # 调用js方法  第一个参数是JS的方法名，后面的为js方法的参数
    return ctx.call('doencodeacc', acc, code)

if __name__ == '__main__': 
    print(get_des_psswd("zhangsan123456", "pYr6BTle"))   # pYr6BTle = ralt code (加密的盐值)