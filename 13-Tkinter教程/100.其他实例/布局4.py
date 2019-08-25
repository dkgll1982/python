#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-24 19:14:15 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-24 19:14:15 
# @Software: vscode 
 
from tkinter import *
window = Tk()
window.title("New England")
yscroll = Scrollbar(window, orient=VERTICAL)
yscroll.grid(row=0,column=2,rowspan=4,sticky=NS)
statesList = ["Connecticut","Maine","Masssachusetts","New Hampshired","Rhode ISsland", "Vermont","New Hampshired","Rhode ISsland", "Vermont"]
conOFlstNE = StringVar()
lstNE = Listbox(window,width=14,height=8,listvariable=conOFlstNE,yscrollcommand=yscroll.set)
lstNE.grid(row=0,column=1,rowspan=4,sticky=E)
conOFlstNE.set(tuple(statesList))
yscroll["command"] = lstNE.yview
window.mainloop()