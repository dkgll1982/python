#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-22 19:57
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 3.设置样式.py
# @Software: PyCharm

from tkinter import *
from tkinter import ttk


def set_app_style():
    style = ttk.Style()
    style.theme_create("htsz-app", parent="alt", settings={
        ".": {"configure": {"background": StColors.dark_grey,
                            "foreground": StColors.light_grey,
                            "relief": "flat",
                            "highlightcolor": StColors.bright_green}},

        "TLabel": {"configure": {"foreground": StColors.bright_green,
                                 "padding": 10,
                                 "font": ("Calibri", 12)}},

        "TNotebook": {"configure": {"padding": 5}},
        "TNotebook.Tab": {"configure": {"padding": [25, 5],
                                        "foreground": "white"},
                          "map": {"background": [("selected", StColors.mid_grey)],
                                  "expand": [("selected", [1, 1, 1, 0])]}},

        "TCombobox": {"configure": {"selectbackground": StColors.dark_grey,
                                    "fieldbackground": "white",
                                    "background": StColors.light_grey,
                                    "foreground": "black"}},

        "TButton": {"configure": {"font": ("Calibri", 13, 'bold'),
                                  "background": "black",
                                  "foreground": StColors.bright_green},
                    "map": {"background": [("active", StColors.bright_green)],
                            "foreground": [("active", 'black')]}},

        "TEntry": {"configure": {"foreground": "black"}},
        "Horizontal.TProgressbar": {"configure": {"background": StColors.mid_grey}}
    })
    style.theme_use("htsz_app")

root = Tk()
root.geometry('600x500+300+200')
style = ttk.Style()

#定义一个全局样式作为默认样式（"."表示此样式将应用于顶级窗口以及所有子元素）
set_app_style()

#未指定样式时，使用全局默认样式
ttk.Button(root,text="默认样式").pack()

root.mainloop();