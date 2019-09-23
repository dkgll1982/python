#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-09-24 22:49:06 
# @Last Modified by: guojun 
# @Last Modified time: 2019-09-24 22:49:06 
# @Software: vscode 

from tkinter import *
import Pmw

root = Tk()
root.geometry('300x300')

lab = Label(root,text="别惹我")
lab.pack()

ballon = Pmw.Balloon(root)
ballon.bind(lab,'点你妹啊')

root.mainloop()