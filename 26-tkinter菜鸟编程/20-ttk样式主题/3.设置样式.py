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
    style.theme_create("st_app", parent="alt", settings={
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
    style.theme_use("st_app")