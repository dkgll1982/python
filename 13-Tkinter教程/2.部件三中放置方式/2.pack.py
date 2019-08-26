#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-22 16:27:34 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-22 16:27:34 
# @Software: vscode 

import tkinter as tk  # 使用Tkinter前需要先导入
 
# 第1步，实例化object，建立窗口window
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('My Window')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x
 
# 第4步，pack 放置方法
tk.Label(window, text='P',bg='pink', fg='red').pack(side='top',fill='x')    # 上
tk.Label(window, text='P',bg='pink', fg='red').pack(side='bottom',fill='x') # 下
tk.Label(window, text='P',bg='pink', fg='red').pack(side='left',fill='y' )   # 左
tk.Label(window, text='P',bg='pink', fg='red').pack(side='right',fill='y')  # 右
 
# 第5步，主窗口循环显示
window.mainloop()