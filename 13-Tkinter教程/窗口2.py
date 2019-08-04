from tkinter import *

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        # 创建一个输入组件
        e = Entry(relief=SUNKEN, font=('Courier New', 24), width=25)
        # 对该输入组件使用Pack布局，放在容器顶部
        e.pack(side=TOP, pady=10)
        p = Frame(self.master)
        p.pack(side=TOP)
        # 定义字符串的元组
        names = ("0" , "1" , "2" , "3"
            , "4" , "5" , "6" , "7" , "8" , "9"
            , "+" , "-" , "*" , "/" , ".", "=")
        # 遍历字符串元组
        for i in range(len(names)):
            # 创建Button，将Button放入p组件中
            b = Button(p, text=names[i], font=('Verdana', 20), width=6)
            b.grid(row=i // 4, column=i % 4)
root = Tk()
root.title("Grid布局")
App(root)
root.mainloop()

import random
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        # 定义字符串元组
        books = ('疯狂Python讲义', '疯狂Swift讲义', '疯狂Kotlin讲义',\
            '疯狂Java讲义', '疯狂Ruby讲义')
        for i in range(len(books)):
            # 生成3个随机数
            ct = [random.randrange(256) for x in range(3)]
            grayness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
            # 将元组中3个随机数格式化成16进制数,转成颜色格式
            bg_color = "#%02x%02x%02x" % tuple(ct)
            # 创建Label，设置背景色和前景色
            lb = Label(root,
                text=books[i],
                fg = 'White' if grayness < 120 else 'Black',
                bg = bg_color)
            # 使用place()设置该Label的大小和位置
            lb.place(x = 20, y = 36 + i*36, width=180, height=30)
root = Tk()
root.title("Place布局")
# 设置窗口的大小和位置
# width x height + x_offset + y_offset
root.geometry("250x250+30+30")  
App(root)
root.mainloop()