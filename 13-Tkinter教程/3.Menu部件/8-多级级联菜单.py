#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-25 23:44:16 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-25 23:44:16 
# @Software: vscode 

import tkinter as tk

root = tk.Tk()
root.geometry('800x500+200+200')
root.title('my window')

def callback():
    print("你好")
    
menubar = tk.Menu(root)  
menu1 = tk.Menu(menubar);
menu2 = tk.Menu(menubar);

def setmenu(menu,mn,ln): 
    submenu = tk.Menu(menubar) 
    menu.add_cascade(label='有子菜单'+str(mn),menu=submenu) 
    for x in range(ln):
        submenu.add_command(label='底层菜单'+str(mn)+'-'+str(x),command=callback); 
    if(mn>1):
        mn-=1
        setmenu(submenu,mn,ln)       

setmenu(menu1,6,6) 
setmenu(menu2,6,6) 

menu1.add_command(label='底层菜单1',command=callback,); 
menu1.add_command(label='底层菜单2',command=callback);  
menubar.add_cascade(label='根菜单',menu=menu1)   
menubar.add_cascade(label='根菜单',menu=menu2)   

root.config(menu=menubar)
root.mainloop()
