#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-22 23:27:15 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-22 23:27:15 
# @Software: vscode 
from tkinter import *
# 导入ttk
from tkinter import ttk
# 导入colorchooser
from tkinter import colorchooser
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        # 创建1个按钮，并为之绑定事件处理函数
        ttk.Button(self.master, text='选择颜色',
            command=self.choose_color # 绑定choose_color方法
            ).pack(side=LEFT, ipadx=50, ipady=20, padx= 100)
    def choose_color(self):
        # 调用askcolor函数获取选中的颜色
        print(colorchooser.askcolor(parent=self.master, title='选择画笔颜色',
            color = 'blue')) # 初始颜色
root = Tk() 
root.geometry('500x300')  
root.title("颜色对话框测试")
App(root)
root.mainloop()