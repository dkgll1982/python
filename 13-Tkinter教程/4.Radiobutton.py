#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-22 14:18:02 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-22 14:18:02 
# @Software: vscode 

import tkinter as tk  # 使用Tkinter前需要先导入
 
# 第1步，实例化object，建立窗口window
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('My Window')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x
 
# 第4步，在图形界面上创建一个标签label用以显示并放置
var = tk.StringVar()    # 定义一个var用来将radiobutton的值和Label的值联系在一起.
var2 = tk.IntVar()     # 定义一个var用来将radiobutton的值和Label的值联系在一起.
l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack() 

# 第6步，定义选项触发函数功能
def print_selection1():
    if var.get() is not None:
        l.config(text='you have selected ' + var.get()) 
def print_selection2():
    if var2.get() is not None:
        l.config(text='you have selected ' + str(var2.get())) 

def print_selection(bool):
    print('var=%s,va2=%d'%(var.get(),var2.get()))
    print_selection1() if bool else print_selection2()
    
# 第5步，创建三个radiobutton选项，其中variable=var, value='A'的意思就是，当我们鼠标选中了其中一个选项，把value的值A放到变量var中，然后赋值给variable
# command传参的两种形式：一种用StringVar，IntVar接收，一种用匿名函数
# r1 = tk.Radiobutton(window, text='Option A', variable=var, value='A', command=print_selection1)
# r2 = tk.Radiobutton(window, text='Option B', variable=var, value='B', command=print_selection1)
# r3 = tk.Radiobutton(window, text='Option C', variable=var, value='C', command=print_selection1) 
# r4 = tk.Radiobutton(window, text='Option A', variable=var2, value=1, command=print_selection2)
# r5 = tk.Radiobutton(window, text='Option B', variable=var2, value=2, command=print_selection2)
# r6 = tk.Radiobutton(window, text='Option C', variable=var2, value=3, command=print_selection2)

r1 = tk.Radiobutton(window, text='Option A', variable=var, value='A', command = lambda:print_selection(True))
r2 = tk.Radiobutton(window, text='Option B', variable=var, value='B', command = lambda:print_selection(True))
r3 = tk.Radiobutton(window, text='Option C', variable=var, value='C', command = lambda:print_selection(True))
r4 = tk.Radiobutton(window, text='Option A', variable=var2, value=1, command = lambda:print_selection(False))
r5 = tk.Radiobutton(window, text='Option B', variable=var2, value=2, command = lambda:print_selection(False))
r6 = tk.Radiobutton(window, text='Option C', variable=var2, value=3, command = lambda:print_selection(False))

r3.pack()
r2.pack()
r1.pack()
r5.pack()
r4.pack()
r6.pack()
 
# 第7步，主窗口循环显示
window.mainloop()