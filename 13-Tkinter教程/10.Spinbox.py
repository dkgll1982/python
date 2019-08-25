#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-23 23:37:37 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-23 23:37:37 
# @Software: vscode 

import tkinter as tk

root = tk.Tk()

# width x height + x_offset + y_offset
root.geometry("500x300+300+300") 

root.title("root windows")

root.iconbitmap(bitmap="images\spoon.ico") 
 
v = tk.IntVar()
tk.Entry(root,textvariable=v,width=3).pack()

v.set(10)
 
# 参数列表：
# from_：The minimum value. 
# to：See from.

# value是个元组，并且increment无论是多少不会再影响up或down的值只会依次按照元组中的数前后移动
#sp =tk.Spinbox(master=root,from_=0,to_=100,increment=5,value=(2,6,0,-8,9),)
sp =tk.Spinbox(master=root,from_=0,to_=100,increment=5,textvariable=v)

sp.pack()


root.mainloop()


# from tkinter import *
# root=Tk()
 
# v=tk.IntVar()
 
# La=tk.Label(root,width=5,fg='blue')
# La.config(textvariable=v,width=3)
# tk.Entry(root,textvariable=v,width=3).pack()
# La.pack()
 
# tk.Spinbox(root,from_=-100,to=100,increment=2,textvariable=v).pack() 
# root.mainloop()