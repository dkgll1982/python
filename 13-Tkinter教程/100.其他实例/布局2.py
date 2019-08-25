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
# 引入字体模块
import tkinter.font as tkFont

tk=Tk()
tk.geometry('500x500+300+200')
#标签控件，显示文本和位图，展示在第一行
# sticky 组件紧靠所在单元格的某一边角。
Label(tk,text="1",width=11,height=2,relief="groove",bg='yellow').grid(row=0,sticky='w')
Label(tk,text="2",width=11,height=2,relief="groove",bg='yellow').grid(row=1,sticky='e')#第二行 
Label(tk,text="3",width=14,height=2,relief="groove",bg='pink').grid(row=0,column=1)
Label(tk,text="4",width=14,height=2,relief="groove",bg='pink').grid(row=1,column=1)#第二行 
Label(tk,text="5",width=14,height=2,relief="groove",bg='red').grid(row=0,column=2)
Label(tk,text="6",width=14,height=2,relief="groove",bg='red').grid(row=1,column=2)#第二行 
Label(tk,text="7",width=11,height=2,relief="groove",bg='green').grid(row=2,column=1,sticky='en',padx=4,pady=4)
Label(tk,text="8",width=14,height=4,relief="groove",bg='green').grid(row=3,column=1)#第二行 
Label(tk,text="9",width=14,height=4,relief="groove",bg='blue').grid(row=2,column=2)
Label(tk,text="10",width=14,height=4,relief="groove",bg='blue').grid(row=3,column=2)#第二行 
Label(tk,text="11",width=14,height=4,relief="groove",bg='gray').grid(row=2)
Label(tk,text="12",width=8,height=2,relief="groove",bg='gray').grid(row=3,sticky='ws',padx=3)#第二行 

#跨行跨列的功能：
photo = PhotoImage(file=r"images\gif\1.gif")  #只能是.gif格式 
# Label(tk, 
#     text='hello Place',
#     width=434,
#     height=435,
#     relief="groove",
#     bg='brown',
#     padx=10,
#     pady=20,
#     image=photo,
#     cursor ="fleur"
#     ).place(x=340, y=208, anchor='nw')
Label(tk, text='跨海大桥',width=20,height=2,relief="groove",bg='black',fg='white').grid(row=2,column=3, rowspan=2,sticky='ws',padx=3,pady=52)#第二行 

#输入控件
Entry(tk,bg="lightgreen",width=18,).grid(row=0,column=3,sticky='w',padx=4,ipady=8,ipadx=11)#输入控件
Entry(tk,bg="lightgreen",width=23).grid(row=1,column=3,sticky='w',padx=4 )
 
ft = tkFont.Font(size=14, weight=tkFont.BOLD, underline=1, overstrike=1,slant="italic")


yscroll = Scrollbar(tk,orient='vertical')
yscroll.grid(row=4,
    column=3,
    rowspan=4,
    #试了好久发现用这个实现滚动条高度
    sticky='wns',  
    padx=3,
    pady=5) 

xscroll = Scrollbar(tk,orient='horizontal')
xscroll.grid(row=8,
    columnspan=3,  
    sticky='nwe',  
    padx=3,
    pady=1)             

lb = Listbox(tk,font=ft,width=28,fg='red', yscrollcommand = yscroll.set, xscrollcommand = xscroll.set )
for x in range(100):
    lb.insert('end','超越自己'+str(x*100)+"，努力奋斗，实现自己的梦想...............")
lb.grid(
    row=4,
    columnspan=3,
    rowspan=4,
    sticky='wn',
    pady=5
    )

yscroll.config( command = lb.yview) 
xscroll.config( command = lb.xview) 

# 与下边语句功能相同
#scrollbar["command"] = lb.yview
# Label(tk,text="跨江大桥",bg="lightgreen",width=23,height=4).grid(
#     row=4, 
#     column=3,
#     rowspan=4,
#     sticky='wn',
#     padx=3 )

# horizontal水平方向滚动,默认垂直方向
#主事件循环
mainloop()