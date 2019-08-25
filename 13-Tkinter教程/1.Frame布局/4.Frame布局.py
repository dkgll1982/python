#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-25 21:09:45 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-25 21:09:45 
# @Software: vscode 

import tkinter as tk
 
master = tk.Tk()
 
tk.Label(text="天王盖地虎", font=("华文行楷", 20), fg="green").pack()
 
#组件可以用于装饰界面，bd=1表示边框宽度为1，heiht=2表示最终显示效果是一个间隔线 
separator = tk.Frame(height=2, bd=1, relief="ridge")
separator.pack(fill="x", padx=5, pady=5)
 
tk.Label(text="小鸡炖蘑菇", font=("华文行楷", 20), fg="green").pack()
separator = tk.Frame(height=2, bd=1, relief="ridge")
separator.pack(fill="x", padx=5, pady=5)

#三引号定义跨越多行的字符串
longtext = """
Label 可以显示多行文本，你可以直接使用换行符
或使用 wraplength 选项来实现。当文本换行的时
候，你可以使用 anchor 和 justify 选项来使得
文本如你所希望的显示出来。
"""
#justify：指定组件内部内容的对齐方式，该选项支持LEFT（左对齐）、CENTER（居中对齐）或RIGHT（右对齐）这三个值
w = tk.Label(master, wraplength=300,
    text=longtext, 
    anchor="w", 
    justify="left", 
    font=("宋体", 12), 
    fg="green",
    cursor='gumby'
).pack() 
 
master.mainloop()
