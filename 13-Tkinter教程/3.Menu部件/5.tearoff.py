#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-23 23:32:41 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-23 23:32:41 
# @Software: vscode 

 
import tkinter

root = tkinter.Tk()
root.title('菜单练习')
menu = tkinter.Menu(root)

#多了一个虚线，点击的话就会发现，这个菜单框可以独立出来显示,默认值是1-True
submenu = tkinter.Menu(menu, tearoff = 1)
submenu.add_command(label = '打开')
submenu.add_command(label = '保存')
submenu.add_command(label = '关闭')
menu.add_cascade(label = '文件', menu = submenu)
root.config(menu = menu) 

root.mainloop()