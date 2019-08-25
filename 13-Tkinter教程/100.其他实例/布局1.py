#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-24 19:14:15 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-24 19:14:15 
# @Software: vscode 

import tkinter as tk;

root = tk.Tk()
root.title("布局")
root.geometry("800x500+300+200")

btn1 = tk.Button(root,text="buttoon-1",height=2) 
btn2 = tk.Button(root,text="buttoon-2",height=2)
btn3 = tk.Button(root,text="buttoon-3",height=2)
btn4 = tk.Button(root,text="buttoon-4",height=2)
#relief=
#边框装饰。默认是 FLAT 平的。其他值是 SUNKEN 凹陷、 RAISED 凸起、 GROOVE 凹槽和 RIDGE 脊。
lbred=tk.Label(root,text="红色沟槽状边缘",fg="red",font=('微软雅黑',15),width=20,height=2,relief="groove")
lbred.pack()
lbgreen=tk.Label(root,text="绿色凸起的",fg="green",font=('微软雅黑',15),width=20,height=2,relief="raised")
lbgreen.pack()
lbblue=tk.Label(root,text="蓝色脊状边缘",fg="blue",font=('微软雅黑',15),width=20,height=2,relief="ridge")
lbblue.pack()
lbyellow=tk.Label(root,text="黄色凹陷的",fg="yellow",font=('微软雅黑',15),width=20,height=2,relief="sunken")
lbyellow.pack()
lbpink=tk.Label(root,text="粉红色平的",fg="pink",font=('微软雅黑',15),width=20,height=2,relief="flat")
lbpink.pack() 
btn1.pack(expand="yes", side="top",fill='both')
btn2.pack(expand="yes", side="left",fill='both')
btn3.pack(expand="yes", side="left",fill='both') 
btn4.pack(expand="yes", side="right",fill='both') 

lb=tk.Listbox(root,width=13)

for x in range(100):
    lb.insert('end',str(x*100))
lb.pack(side="bottom",fill='both')

s1=tk.Scrollbar(root,orient='horizontal')
s1.pack(side = "right",fill = 'y')

lb['yscrollcommand'] = s1.set

root.mainloop()