#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-04 16:45:20 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-04 16:45:20 
# @Software: vscode 

from exec_select import *
from tkinter import *

def main():
    description, rows = query_db()
    # 创建窗口
    win = Tk()
    win.title('数据库查询')
    # 通过description获取列信息
    # for i, col in enumerate(description):
    #     lb = Button(win, text=col[0], padx=50, pady=6)
    #     lb.grid(row=0, column=i)
    # # 直接使用for循环查询得到的结果集
    # for i, row in enumerate(rows):
    #     for j in range(len(row)):
    #         en = Label(win, text=row[j])
    #         en.grid(row=i+1, column=j)
    win.mainloop()
if __name__ == '__main__':
    main()