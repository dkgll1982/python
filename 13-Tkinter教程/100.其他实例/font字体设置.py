'''Tkinter教程之Font篇'''
# Tkinter中其它常用的一些功能
'''1.字体使用'''
# -*- coding: utf-8 -*-
# 改变组件的显示字体
from tkinter import *
 
root = Tk()
root.geometry('800x500+100+100')
# 创建一个Label
for ft in ('Arial', ('Courier New',), ('Comic Sans MS',), 'Fixdsys', ('MS Sans Serif',), ('MS Serif',), 'Symbol', 'System',
           ('Times New Roman',), 'Verdana'):
    Label(root, text='hello sticky', font=ft).grid()

# 引入字体模块
import tkinter.font as tkFont
  
# 创建一个Label
# 指定字体名称、大小、样式
#font字体的参数有如下6个
#family: 字体类别，如'Fixdsys'
#size: 作为一个整数，以点字体的高度。为了获得字体的n个像素高，使用-n.
#weight: "BOLD" 表示加粗, "NORMAL" 表示正常大小，默认是NORMAL
#slant：斜体（默认正常）， “NORMAL”表示正常，"ITALIC"表示字体倾斜
#underline：下划线，1表示添加下滑线，0表示没有，默认值为0
#overstrike：删除线，1表示添加删除线，0表示没有，默认值为0 

ft = tkFont.Font(family='Fixdsys', size=20, weight=tkFont.BOLD,slant=tkFont.ITALIC,overstrike=1)
lbl = Label(root, text='hello sticky', font=ft,fg="red",bd =4,bg='gray',justify ='left',wraplength=80,width=10)
lbl.config(highlightbackground = "yellow")
lbl.grid()    
 

#highlightbackground：指定当 Listbox 没有获得焦点的时候高亮边框的颜色， 默认值由系统指定，通常是标准背景颜色
#highlightcolor：指定当 Listbox 获得焦点的时候高亮边框的颜色，默认值由系统指定
#highlightthickness： 指定高亮边框的宽度，默认值是 1
text1 = Entry(
    root,  
    highlightbackground = 'blue',
    highlightcolor = 'red',
    highlightthickness=3,
    bd =3,
    bg='lightyellow',
    selectbackground='pink',#选中文字的背景颜色
    selectborderwidth=12,
    font = ft,
    fg="green",
    selectforeground = '#A020F0', #选中文字的颜色 
)
text2 = Entry(root, highlightbackground = 'blue',highlightcolor = 'red',highlightthickness=3,bd =3)
text1.grid(padx=13,pady=20)
text2.grid(padx=13)

root.mainloop()