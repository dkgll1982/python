#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-22 14:18:13 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-22 14:18:13 
# @Software: vscode 
 
# import tkinter as tk  # 使用Tkinter前需要先导入
 
# # 第1步，实例化object，建立窗口window
# window = tk.Tk()
 
# # 第2步，给窗口的可视化起名字
# window.title('My Window')
 
# # 第3步，设定窗口的大小(长 * 宽)
# window.geometry('500x300')  # 这里的乘是小x
 
# # 第4步，在图形界面上设定标签
# var = tk.StringVar()    # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
# l = tk.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
# # 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
# l.pack()
 
# # 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
# on_hit = False
# def hit_me():
#     global on_hit
#     if on_hit == False:
#         on_hit = True
#         var.set('you hit me')
#     else:
#         on_hit = False
#         var.set('')
 
# # 第5步，在窗口界面设置放置Button按键
# b = tk.Button(window, text='hit me', font=('Arial', 12), width=10, height=1, command=hit_me)
# b.pack()
 
# # 第6步，主窗口循环显示
# window.mainloop()


from tkinter import *
# 导入ttk
from tkinter import ttk
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        topF = Frame(self.master)
        topF.pack(fill=Y, expand=YES)
        # 定义StringVar变量
        self.v = StringVar()
        # 创建Listbox组件，与v变量绑定
        self.lb = Listbox(topF, listvariable = self.v)
        self.lb.pack(side=LEFT, fill=Y, expand=YES)
        for item in range(20): 
            self.lb.insert(END, str(item))
        # 创建Scrollbar组件，设置该组件与self.lb的纵向滚动关联
        scroll = Scrollbar(topF, command=self.lb.yview)
        scroll.pack(side=RIGHT, fill=Y)
        # 设置self.lb的纵向滚动影响scroll滚动条
        self.lb.configure(yscrollcommand=scroll.set)
        f = Frame(self.master)
        f.pack()
        Button(f, text="选中10项", command=self.select).pack(side=LEFT)
        Button(f, text="清除选中3项", command=self.clear_select).pack(side=LEFT)
        Button(f, text="删除3项", command=self.delete).pack(side=LEFT)
        Button(f, text="绑定变量", command=self.var_select).pack(side=LEFT)
        self.lb.insert(ACTIVE, '第一列2') 
        self.lb.insert(ACTIVE, '第一列3')
        self.lb.insert(ACTIVE, '第一列4')
        self.lb.insert(ACTIVE, '第一列1')
        self.lb.delete(0,1)
        #选中
        self.lb.select_set(1,4)
        self.lb.select_clear(2)
        #print(self.lb.get(2,4))
        #返回当前选中的项的索引
        print(self.lb.curselection())
    def select(self):
        # 选中指定项
        self.lb.selection_set(0, 9) 
    def clear_select(self):
        # 取消选中指定项
        self.lb.selection_clear(1,3)
    def delete(self):
        # 删除指定项
        self.lb.delete(5, 8)
    def var_select(self):
        # 修改与Listbox绑定的变量
        self.v.set(('12', '15'))     
root = Tk()
root.title("Listbox测试")
# 改变窗口图标
root.iconbitmap('images\spoon.ico')
App(root)
root.mainloop()