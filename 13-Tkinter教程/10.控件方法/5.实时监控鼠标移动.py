#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-28 10:34:29 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-28 10:34:29 
# @Software: vscode 

from tkinter import *

root = Tk()

def callback(e):
    print('鼠标位置：%d,%d'%(e.x,e.y))

frm = Frame(root,width=200,height=200)

frm.bind('<Motion>',callback)
#frm.focus_set()     #通过focus_set方法获得焦点。也可以设置Frame的takefocus选项为True，然后使用Tab将焦点转移上来

frm.pack()
help(frm.focus_set)
mainloop();
