#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-24 16:55:33 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-24 16:55:33 
# @Software: vscode 

import tkinter as tk;
import os

dir = "images\ico"
icolist = os.listdir(dir)
count =len([x for x in icolist])
index = 0

root = tk.Tk()
root.geometry("500x300+200+222")
root.title("我的窗体") 

var = tk.StringVar()
var.set(icolist[index])

def change_ico(): 
    global index;  
    index+=1
    index= 0 if index == count else index 
    var.set(icolist[index])
    root.iconbitmap(dir+"\\"+icolist[index])

def delete_text():
    # def delete(self, index1, index2=None):
    # 从index1到index2的文字都删除，但是不包括index
    # 0.0表示开始，END表示结尾
    txt.delete(1.2, 1.4) 
    #txt.delete(1.2, "end") 

#按钮
btn = tk.Button(root,text = '切换图标',command = change_ico,bg="lightgreen")
btn.config(bg='green',fg='yellow',padx=10,pady=10,width=10,height=1)
btn.config(cursor='gumby')
btn.config(font=("Times", 14, "bold"))
btn.pack() 

#文本框
ent =tk.Entry(root,width=22,bd=6,fg='blue',bg='pink')
ent.config(textvariable=var)
root.iconbitmap(dir+"\\"+icolist[index])
ent.pack() 

#标签
lbl_user =tk.Label(root,text="用户名",fg='red',bg='blue',width=10,padx=1,compound='top',font = ('幼圆', 12))
lbl_pwd =tk.Label(root,text="密码",fg='red',bg='blue',width=10,padx=1,compound='top',font = ('幼圆', 12))
lbl_user.pack()
lbl_pwd.pack()

#多行文本
txt = tk.Text(root,width=50,height=10,bg='lightpink',fg='red')
# INSERT索引表示在光标处插入
txt.insert("insert", "我要吃饭")
 
# END索引号表示在最后插入
txt.insert("end", "，喝鸡蛋汤")
# 调用函数，清除文字
delete_text()
txt.pack( )

# 窗口大小是否可以改变，宽，高,True表示可以改变
root.resizable(True, True)
root.minsize(200, 200)
root.maxsize(800, 500)
root.mainloop()
