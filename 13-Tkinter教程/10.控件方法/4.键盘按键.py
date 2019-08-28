#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-28 10:32:45 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-28 10:32:45 
# @Software: vscode 

from tkinter import *
 
root =Tk()
 
def callback(e):
    print(e.char)  #获取当前键盘按下的字符
 
frame = Frame(root, width=200, height=200)
frame.bind("<Key>", callback)  #组件想要响应键盘事件，组件必须获得焦点，组件才会响应键盘来的消息。因为一个窗口可以有很多组件，键盘一次敲击不知道给哪个组件。
frame.focus_set()  #通过focus_set方法获得焦点。也可以设置Frame的takefocus选项为True，然后使用Tab将焦点转移上来
frame.pack()
 
mainloop() 