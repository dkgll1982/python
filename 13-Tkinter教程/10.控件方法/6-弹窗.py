#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-28 16:23:04 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-28 16:23:04 
# @Software: vscode 

from tkinter import *
from ChildWindow import window
import sys
sys.path.append('/Users/michael/my_py_scripts')

tk = Tk();
tk.title('主窗体')
tk.geometry('300x300+200+200')

def returnfrm():
    window.show()

btn =Button(tk,text='跳转子窗体',command=returnfrm)
btn.pack()

tk.mainloop()

