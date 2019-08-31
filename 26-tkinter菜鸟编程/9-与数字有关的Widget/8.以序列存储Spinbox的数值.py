from tkinter import *

root = Tk()
root.title()
root.geometry('300x100+200+200')

def printInfo():            #打印显示的值
    print(spin.get())

citied=('新家坡','马来西亚','印度尼西亚','泰国','印度','菲律宾','巴基斯坦','以色列','上海','北京','天津','广州')  #以元组形式存储数值
spin = Spinbox(root,values=citied,command = printInfo) 
spin.pack(pady=20,padx=20)

root.mainloop()