#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-25 17:41:20 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-25 17:41:20 
# @Software: vscode 

from tkinter import *
root = Tk()
root.geometry('500x500+300+200')
lb = Listbox(root,width=53)
sl = Scrollbar(root)
sl.pack(side = RIGHT,fill = Y)
#side指定Scrollbar为居右；fill指定填充满整个剩余区域。
#下面的这句是关键：指定Listbox的yscrollbar的回调函数为Scrollbar的set
lb['yscrollcommand'] = sl.set
for i in range(100):
    lb.insert(END,str(i))
#side指定Listbox为居左
lb.pack(side = LEFT)
#下面的这句是关键：指定Scrollbar的command的回调函数是Listbar的yview
sl['command'] = lb.yview 

root.mainloop()