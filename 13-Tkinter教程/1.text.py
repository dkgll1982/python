#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-22 10:30:13 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-22 10:30:13 
# @Software: vscode 

import tkinter as tk

# 第1步：实例化obvbject，建立窗口window
Window = tk.Tk()

# 第2步：设置窗口的大小和位置
# width x height + x_offset + y_offset
Window.geometry("500x300+300+300")   

# 第3步：给窗口起名字
Window.title("我的窗口程序")

# 第4步：在图形界面上设定标签
var = tk.StringVar()   # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
var.set('蔬菜')

# 注意接收StringVar的参数：textvariable
l = tk.Label(Window,textvariable=var,bg = "green",font =('Arial',12),width = 50, height =2)  
# 说明：bg为背景，font为字体，width为长度，height为高度，这里的长和高为字符的长和高，比如height=2，就是标签有2个字符这么高

# 第5步，放置标签 调用pack进行布局
l.pack()    # Label内容content区域放置位置，自动调节尺寸
# 放置Lable的方法有：1）l.pack();2）l.place()

# 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名

####################################################################################
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('甘薯') 
    else:
        on_hit = False
        var.set('紫菜')
####################################################################################

b = tk.Button(Window,text="点我",font=('宋体',12),width = 12,height = 1,command =hit_me)
b.pack()

# 在图形界面上设定输入框空间entry并放置控件
# Entry是tkinter类中提供的的一个单行文本输入域，用来输入显示一行文本，收集键盘输入(类似 HTML 中的 text)。
e1 = tk.Entry(Window,show = '*',font =("宋体",14))  # 显示成密文形式
e2 = tk.Entry(Window,show = None,font =("宋体",14))  # 显示成明文形式
e1.pack()
e2.pack() 

####################################################################################
# 第5步，定义两个触发事件时的函数insert_point和insert_end（注意：因为Python的执行顺序是从上往下，所以函数一定要放在按钮的上面）
def insert_point(): # 在鼠标焦点处插入输入内容
    var = e1.get()
    t.insert('insert', var)
    
def insert_end():   # 在文本框内容最后接着插入输入内容
    var = e1.get()
    t.insert('end', var)
####################################################################################
 
# 第6步，创建并放置两个按钮分别触发两种情况
b1 = tk.Button(Window, text='insert point', width=10,
               height=2, command=insert_point)
b1.pack()
b2 = tk.Button(Window, text='insert end', width=10,
               height=2, command=insert_end)
b2.pack()

# 在图形界面上设定输入框控件entry框并放置
# Text是tkinter类中提供的的一个多行文本区域，显示多行文本，可用来收集(或显示)用户输入的文字(类似 HTML 中的 textarea)，
# 格式化文本显示，允许你用不同的样式和属性来显示和编辑文本，同时支持内嵌图象和窗口。

t = tk.Text(Window,height=10)
#INSERT索引表示在光标处插入
t.insert('insert','I Love')
#END索引号表示在最后插入
t.insert('end',' you')

t.pack()

#主窗口LOGO图片
Window.iconbitmap('images\spoon.ico')

# 第6步，主窗口循环显示
Window.mainloop()
# 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
# 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。

