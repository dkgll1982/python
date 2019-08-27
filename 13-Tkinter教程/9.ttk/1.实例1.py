#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-27 13:40:45 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-27 13:40:45 
# @Software: vscode 

from tkinter import *
# 导入ttk
from tkinter import ttk

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
               #listbox组件部分
        # cb = Listbox(self.master, font=24)
        # # 为Listbox设置列表项
        # for s in ('Python', 'Swift', 'Kotlin'):
        #     cb.insert(END, s)
        # cb.pack(side=LEFT, fill=X, expand=YES)
        # f = Frame(self.master)
        # f.pack(side=RIGHT, fill=BOTH, expand=YES)
        # lab = Label(self.master, text='我的标签', font=24)
        # lab.pack(side=TOP, fill=BOTH, expand=YES)       
        # bn = Button(self.master, text='我的按钮')
        # bn.pack() 
        # ttk使用Combobox取代了Listbox
        cb = ttk.Combobox(self.master, font=24)
        # 为Combobox设置列表项
        cb['values'] = ('Python', 'Swift', 'Kotlin')
        cb.pack(side=LEFT, fill=X, expand=YES)
        f = ttk.Frame(self.master)
        f.pack(side=RIGHT, fill=BOTH, expand=YES)
        lab = ttk.Label(self.master, text='我的标签', font=24)
        lab.pack(side=TOP, fill=BOTH, expand=YES)
        bn = ttk.Button(self.master, text='我的按钮')
        bn.pack() 

root = Tk()
root.title("简单事件处理")
App(root)
root.mainloop()
