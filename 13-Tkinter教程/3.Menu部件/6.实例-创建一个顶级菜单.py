#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-25 22:54:17 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-25 22:54:17 
# @Software: vscode 

import tkinter as tk

root = tk.Tk()

menubar =tk.Menu(root)
 
def callback():
    print("你好")

menubar.add_command(label="文件",command=callback)
menubar.add_command(label="退出",command=root.quit)

root.config(menu=menubar)

root.mainloop()