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
var.set('信息')
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

def gettag(index):
    if index in('1','2','3'):
        return "单击" 
    elif index=='4':
        return "向上滚动滑轮"
    elif index=='5':
        return "向下滚动滑轮"

listbox.bind('<Button-1>',lambda e:print(str(e)+"左键"+gettag('1')+"事件"))
listbox.bind('<Button-2>',lambda e:print(str(e)+"中键"+gettag('2')+"事件"))
listbox.bind('<Button-3>',lambda e:print(str(e)+"右键"+gettag('3')+"事件")) 

listbox.bind('<Double-Button-1>',lambda e:print(str(e)+"左键双击事件"))
listbox.bind('<Double-Button-2>',lambda e:print(str(e)+"中键双击事件"))
listbox.bind('<Double-Button-3>',lambda e:print(str(e)+"右键双击事件")) 

listbox.bind('<ButtonRelease-1>',lambda e:print(str(e)+"鼠标左键释放")) 
listbox.bind('<ButtonRelease-2>',lambda e:print(str(e)+"鼠标中键释放")) 
listbox.bind('<ButtonRelease-3>',lambda e:print(str(e)+"鼠标右键释放")) 


listbox.bind('<Enter>',lambda e:print(str(e)+"鼠标移入")) 
listbox.bind('<Leave>',lambda e:print(str(e)+"鼠标移出")) 

listbox.bind('<Key>',lambda e:print(str(e)+"键盘按下")) 

#键位绑定事件
listbox.bind('<Return>',lambda e:print(str(e)+"你按下了回车键")) 
listbox.bind('<BackSpace>',lambda e:print(str(e)+"你按下了回退键")) 
listbox.bind('<space>',lambda e:print(str(e)+"你按下了空格键")) 
listbox.bind('<Escape>',lambda e:print(str(e)+"你按下了退出键")) 
listbox.bind('<Left>',lambda e:print(str(e)+"你按下了左键")) 
listbox.bind('<Up>',lambda e:print(str(e)+"你按下了向上键")) 
listbox.bind('<Down>',lambda e:print(str(e)+"你按下了向下键")) 
listbox.bind('<Right>',lambda e:print(str(e)+"你按下了右键")) 

mainloop()