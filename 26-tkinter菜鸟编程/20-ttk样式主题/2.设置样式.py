#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-22 18:24
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 2.设置样式.py
# @Software: PyCharm

from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('600x500+300+200')
style = ttk.Style()

#定义一个全局样式作为默认样式（"."表示此样式将应用于顶级窗口以及所有子元素）
style.configure('.',font='宋体 28',foreground='brown',background='yellow')

#未指定样式时，使用全局默认样式
ttk.Button(root,text="默认样式").pack()

#定义一个名为danger的样式（newName.oldName格式）
style.configure('danger.TButton',font='Times 12',foreground='red',padding=2)
ttk.Button(root,text="使用danger样式",style='danger.TButton').pack()

#为小控件的不同状态指定样式（用map指定）
style.map("new_state_style.TButton",foreground=[('pressed','red'),('active','blue')])
ttk.Button(root,text="不同状态不同样式",style='new_state_style.TButton').pack()

#覆盖Entry当前主题（即使没有指定样式，也会受到主题更改的影响）
#1：先获取当前主题
current_theme = style.theme_use()
print('当前主题：%s'%current_theme)
#设置Entry控件的主题
style.theme_settings(current_theme,
                     {'TEntry':{
                         "configure":{"padding":10},                #静态样式（configure）
                         "map":{"foreground":[("focus","red")]}     #状态样式（map）
                     },
                      'TLabel':{
                          "configure":{"foreground":"red"}
                      }
                     })

ttk.Entry(root).pack()
ttk.Label(root,text='全局label样式已被更改').pack()  #全局样式加上TLabel样式 
root.mainloop();