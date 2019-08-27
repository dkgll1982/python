#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-27 21:08:22 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-27 21:08:22 
# @Software: vscode 

from tkinter import *

master = Tk()

var = StringVar()
var.set('dfgdgdgd')
listbox = Listbox(master,selectmode=EXTENDED ,listvariable=var)
listbox.pack()

listbox.insert(END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)

b = Button(master, text="Delete",
           command=lambda : listbox.delete(ANCHOR))
b.pack()

def ud():
    var.set((1,2,3,4,5,5,6,7,7))
    
b2 = Button(master, text="修改",command=ud)
b2.pack()

mainloop()