#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-28 17:10:44 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-28 17:10:44 
# @Software: vscode 

from tkinter import * 

class window:
    def __init__():
        root = Tk()
        
    def show2():
        top = Toplevel()
        top.title('山丘')
        top.geometry('200x200')
        top.attributes('-alpha',0.8)
        Label(top,text='越过河流').pack()
        Button(top,text='创建下级窗口',command=window.show2).pack() 

    def show():
        top = Toplevel()
        top.title('山丘')
        top.geometry('200x200')
        top.attributes('-alpha',0.8)
        Label(top,text='越过山丘').pack()
        Button(top,text='创建子级窗口',command=window.show2).pack() 