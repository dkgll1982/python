#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-23 22:57:13 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-23 22:57:13 
# @Software: vscode 

from tkinter import *
# 导入ttk
from tkinter import ttk
from collections import OrderedDict
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        self.text = Text(self.master, height=12, width=60,
            foreground='darkgray',
            font=('微软雅黑', 12),
            spacing2=8, # 设置行间距
            spacing3=12) # 设置段间距
        self.text.pack()
        st = 'C语言中文网成立于 2012 年初,' +\
            '目前已经运营了将近 5 年,' +\
            '我们致力于分享精品教程，帮助对编程感兴趣的读者\n'
        self.text.insert(END, st)
        # 为text组件的右键单击事件绑定处理方法
        self.text.bind('<Button-3>',self.popup)
        # 创建Menu对象，准备作为右键菜单
        self.popup_menu = Menu(self.master,tearoff = 0)
        self.my_items = (OrderedDict([('超大', 16), ('大',14), ('中',12),
            ('小',10), ('超小',8)]),
            OrderedDict([('红色','red'), ('绿色','green'), ('蓝色', 'blue')]))
        i = 0
        for k in ['字体大小','颜色']:
            m = Menu(self.popup_menu, tearoff = 0)
            # 添加子菜单
            self.popup_menu.add_cascade(label=k ,menu = m)
            # 遍历OrderedDict的key（默认就是遍历key）
            for im in self.my_items[i]:
                m.add_command(label=im, command=self.handlerAdaptor(self.choose, x=im))
            i += 1
    def popup(self, event):
        # 在指定位置显示菜单
        self.popup_menu.post(event.x_root,event.y_root)  #①
    def choose(self, x):
        # 如果用户选择修改字体大小的子菜单项
        if x in self.my_items[0].keys():
            # 改变字体大小
            self.text['font'] = ('微软雅黑', self.my_items[0][x])
        # 如果用户选择修改颜色的子菜单项
        if x in self.my_items[1].keys():
            # 改变颜色
            self.text['foreground'] = self.my_items[1][x]
    def handlerAdaptor(self, fun,**kwds):
        return lambda fun=fun, kwds=kwds: fun(**kwds)
root = Tk()
root.title("右键菜单测试")
App(root)
root.mainloop()