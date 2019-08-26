#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-22 16:21:59 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-22 16:21:59 
# @Software: vscode 

import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox  # 要使用messagebox先要导入模块
 
# 第1步，实例化object，建立窗口window
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('My Window')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x
 
#创建一个Message，是用来显示文字的空间，但Message控件用来显示多行不可编辑的文字，且它可以自动编排文字的位置。
whatever_you_do = "Only those who have the patience to do simple things perfectly ever acquire the skill to do difficult things easily.\n(Friedrich Schiller)"
msg = tk.Message(window, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 20, 'italic'))
msg.pack( )
 
# 第5步，定义触发函数功能
def hit_me():
    tkinter.messagebox.showinfo(title='Hi', message='你好！')              # 提示信息对话窗
    tkinter.messagebox.showwarning(title='Hi', message='有警告！')       # 提出警告对话窗
    tkinter.messagebox.showerror(title='Hi', message='出错了！')         # 提出错误对话窗
    print(tkinter.messagebox.askquestion(title='Hi', message='你好！'))  # 询问选择对话窗return 'yes', 'no'
    print(tkinter.messagebox.askyesno(title='Hi', message='你好！'))     # return 'True', 'False'
    print(tkinter.messagebox.askokcancel(title='Hi', message='你好！'))  # return 'True', 'False'
    tkinter.messagebox.askretrycancel(title='Hi', message='你好！')
 
# 第4步，在图形界面上创建一个标签用以显示内容并放置
tk.Button(window, text='hit me', bg='green', font=('Arial', 14), command=hit_me).pack()
 
# 第6步，主窗口循环显示
window.mainloop()