#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-22 11:11:29 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-22 11:11:29 
# @Software: vscode 
from tkinter import *


def main():
    # 这个函数要写在前面
    # 如果要是写在所有代码的后面，找不到的
    global on_hit 
    on_hit = False
    def hit_me():
        global on_hit
        if on_hit == False:
            on_hit = True
            var.set('甘薯')
            print(var)
        else:
            on_hit = False
            var.set('花菜')

    root = Tk()

    # 两个框架
    frame1 = Frame(root,height = 200, width=300)
    frame2 = Frame(root,height = 200, width=300)

    # Label显示的文字要是会变化的话，只接受这种类型的变量
    var = StringVar()
    var.set("紫菜")

    text_label = Label(frame1,
                       textvariable=var,
                       justify=LEFT
                       )
    text_label.pack()

    the_button = Button(frame2,
                        text='下一句',
                        command=hit_me  # 点击时调用的函数
                        )
    the_button.config(bg='green',fg='yellow')
    the_button.config(cursor='gumby')
    the_button.config(font=("Times", 16, "bold"))

    the_button.pack()

    # 可以把这两个调换一下位置，2先1后。
    frame1.pack(padx=20, pady=20)
    frame2.pack(padx=40, pady=40)

    mainloop()


if __name__ == '__main__':
    main()