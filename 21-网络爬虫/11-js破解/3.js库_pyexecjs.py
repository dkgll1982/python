#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-04-16 12:49:56 
# @Remark: 人生苦短，我用python！ 

import execjs
import sys
import os  

# 获取文件当前所在的目录，并返回完整文件全路径 
def realpath(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

def get_js():
    # 打开JS文件
    f = open(realpath("test.js"), 'r', encoding='utf-8')
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr

def check_card(card):
    jsstr = get_js()
    #  加载JS文件
    ctx = execjs.compile(jsstr)
    # 调用js方法  第一个参数是JS的方法名，后面的为js方法的参数
    return ctx.call('checkIDCard', card)

if __name__ == '__main__': 
    while True:
        card = input('请输入身份证号码：')
        if not card:continue
        print('身份证{}校验结果：{}'.format(card,check_card(card)))
        # 按q键退出循环
        if card =='q':
                break