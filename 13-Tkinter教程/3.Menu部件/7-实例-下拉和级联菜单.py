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
root.geometry('500x300+200+200')
root.title('my window')

def callback():
    print("你好")
    
menubar = tk.Menu(root)  
subm1_1_1=tk.Menu(menubar);
subm1_1=tk.Menu(menubar);
subm1 = tk.Menu(menubar,tearoff=False)
subm2 = tk.Menu(menubar, tearoff=False)

#最底层菜单
subm1_1_1.add_command(label="美剧",command=callback)
subm1_1_1.add_command(label="韩剧",command=callback)
subm1_1_1.add_command(label="日剧",command=callback)
subm1_1_1.add_command(label="港剧",command=callback)

subm1_1.add_cascade(label='好剧推荐', menu=subm1_1_1)
subm1_1.add_command(label="电影",command=callback)
subm1_1.add_command(label="电视剧",command=callback)
subm1_1.add_command(label="综艺节目",command=callback)
subm1_1.add_command(label="纪录片",command=callback)
 
#子级菜单1
subm1.add_cascade(label='打开', menu=subm1_1)
subm1.add_command(label='保存',command=callback)
subm1.add_separator() #添加分割线
subm1.add_command(label='退出',command=root.quit)
 
#子级菜单2
subm2.add_command(label='剪切', command=callback)
subm2.add_command(label='拷贝', command=callback)
subm2.add_separator()  #添加分割线
subm2.add_command(label='粘贴', command=callback)

#创建级联菜单，menu选项指定下一级的菜单是什么
menubar.add_cascade(label='文件',menu=subm1)  
menubar.add_cascade(label='编辑', menu=subm2) 

root.config(menu=menubar)
root.mainloop()
