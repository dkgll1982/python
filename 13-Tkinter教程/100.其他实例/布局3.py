#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-24 20:32:45 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-24 20:32:45 
# @Software: vscode 
# 使用tkinter编写登录窗口
# Grid(网格)布局管理器会将控件放置到一个二维的表格里，主控件被分割为一系列的行和列
# stricky设置对齐方式，参数N/S/W/E分别表示上、下、左、右
# columnspan：指定控件跨越多列显示
# rowspan：指定控件跨越多行显示
# padx、pady分别设置横向和纵向间隔大小

import tkinter as tk

root = tk.Tk()
root.title("请登录")


def reg():
    '''登录校验'''
    username = e_user.get()
    passwd = e_pwd.get()
    len_user = len(username)
    len_pwd = len(passwd)
    if username == 'admin' and passwd == '123':
        l_msg['text'] = '登录成功！'
        l_msg['fg'] = 'green'
    else:
        l_msg.configure(text='登录失败！', fg='red')
    # e_user.delete(0, len_user)  # 清空输入框
    e_pwd.delete(0, len_pwd)


# 登录结果提示
l_msg = tk.Label(root, text='')
l_msg.grid(row=0, columnspan=2)  # 跨越两列显示

# 第一行用户名输入框
l_user = tk.Label(root, text='用户名：',bg="brown")
l_user.grid(row=1, sticky=tk.W)
e_user = tk.Entry(root)
e_user.grid(row=1, column=1, sticky=tk.E, padx=13)

# 第二行密码输入框
l_pwd = tk.Label(root, text='密码：',bg="brown")
l_pwd.grid(row=2, sticky=tk.E)
e_pwd = tk.Entry(root)
e_pwd['show'] = '*'  # 隐藏显示
e_pwd.grid(row=2, column=1, sticky=tk.E, padx=13)

# 第三行登录按钮
f_btn = tk.Frame(root)
b_login = tk.Button(f_btn, text='登录', width=6, command=reg)
b_login.grid(row=0, column=0)
b_cancel = tk.Button(f_btn, text='取消', width=6, command=root.quit)
b_cancel.grid(row=0, column=1)
f_btn.grid(row=3, columnspan=2, pady=10)

root.mainloop()

# 原始按钮布局
# b_login = tk.Button(root, text='登录', command=reg)
# b_login.grid(row=3, column=1, sticky=tk.W, pady=10)
# b_cancel = tk.Button(root, text='取消', command=root.quit)
# b_cancel.grid(row=3, column=1)