#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-27 14:09:21 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-27 14:09:21 
# @Software: vscode 

#compound 选项支持如下属性值：
#None：图片覆盖文字。
#LEFT 常量（值为‘left’字符串）：图片在左，文本在右。
#RIGHT 常量（值为‘right’字符串）：图片在右，文本在左。
#TOP 常量（值为‘top’字符串）： 图片在上，文本在下。
#BOTTOM 常量（值为‘bottom’字符串）：图片在底，文本在上。
#CENTER 常量（值为‘center’字符串）：文本在图片上方。

from tkinter import *
# 导入ttk
from tkinter import ttk
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        # 创建一个位图
        bm = PhotoImage(file = r'images\001.png')
        # 创建一个Label，同时指定text和image
        self.label = ttk.Label(self.master, text='学编程\n神器',\
            image=bm, font=('StSong', 20, 'bold'), foreground='red' )
        self.label.bm = bm
        # 设置Label默认的compound为None
        self.label['compound'] = None
        self.label.pack()
        # 创建Frame容器，用于装多个Radiobutton
        f = ttk.Frame(self.master)
        f.pack(fill=BOTH, expand=YES)
        compounds = ('None', "LEFT", "RIGHT", "TOP", "BOTTOM", "CENTER")
        # 定义一个StringVar变量，用作绑定Radiobutton的变量
        self.var = StringVar()
        self.var.set('None')
        # 使用循环创建多个Radionbutton组件
        for val in compounds:
            rb = Radiobutton(f,
                text = val,
                padx = 20,
                variable = self.var,
                command = self.change_compound,
                value = val).pack(side=LEFT, anchor=CENTER)
    # 实现change_compound方法，用于动态改变Label的compound选项
    def change_compound(self):
        self.label['compound'] = self.var.get().lower()
root = Tk()
root.title("compound测试")
App(root)
root.mainloop()