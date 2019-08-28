#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-28 10:30:19 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-28 10:30:19 
# @Software: vscode 

from tkinter import *
 
root =Tk()
 
#当触发<Button-1>，Tkinter会带着事件本身去调用callback，会把它传入到callback中，因此要个形参来接收对应的事件描述
def callback(event):
    print("点击位置：", event.x, event.y) #这个x和y表示的是相对于应用程序左上角的x和y。root的x和y相对的是屏幕
 
frame = Frame(root, width=200, height=200)
frame.bind("<Button-1>", callback)  # -左边是事件本身，右边是事件详细描述。Button表示的是鼠标的点击事件，1表示的是左键，2代表滚轮，3表示右键，4、5对于Linux系统才有用，表示滚轮向上滚和向下滚。对于Windows和Mac系统来说则是通过mousewhell来表示用户是向上滚还是向下滚了滚轮。
frame.pack()
 
mainloop() 