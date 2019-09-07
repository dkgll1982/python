# -*- coding: utf-8 -*-
import tkinter as tk  #装载tkinter模块,用于Python3
from tkinter import ttk  #装载tkinter.ttk模块,用于Python3
from tkinter import messagebox

root =tk.Tk()  # 创建窗口对象
root.title(string = 'ttk.Notebook演示')  #设置窗口标题
root.geometry('800x500+200+200')

tabControl = ttk.Notebook(root)  #创建Notebook

clist = ["red","blue","gray","yellow","pink","white","black","brown","orange","green"]

def msg():
    messagebox.showinfo('Notebook','欢迎使用notebook')

for item in clist:
    tab = tk.Frame(tabControl,bg=item)  #增加新选项卡
    tabControl.add(tab, text='颜色'+item) 
    btn = ttk.Button(tab,text=item,command=msg)
    btn.pack(padx=10,pady=10)

tabControl.pack(expand=1, fill="both") 

root.mainloop()     # 进入消息循环
