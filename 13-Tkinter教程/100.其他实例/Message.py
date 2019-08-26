#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-25 22:22:35 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-25 22:22:35 
# @Software: vscode 

import tkinter as tk
from tkinter import Message
win = tk.Tk()
txt = "这是一个长长的字符串，这是一个长长11111的字符串，这是一个长长1111111111的字符串，这是一个长长的字符串，这是一个长长的字符串。"

Message(win,text=txt).pack()
win.mainloop()