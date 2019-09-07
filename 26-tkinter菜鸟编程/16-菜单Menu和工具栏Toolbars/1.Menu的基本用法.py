from tkinter import *
from tkinter import messagebox

def hello():
    pass

root = Tk()
root.title('Menu的基本用法')
root.geometry('300x100')

def use():
    messagebox.showinfo('Hello','欢迎使用菜单')

#建立最上层菜单
menu = Menu(root)

#建立菜单类别对象
filemenu = Menu(menu,tearoff=0)
menu.add_cascade(label='文件',menu = filemenu)

#在filemenu里建立菜单列表
filemenu.add_command(label='菜单1',command = use)
filemenu.add_command(label='菜单2')
 
menu.add_cascade(label='退出',command = root.destroy) 

#显示菜单对象
root.configure(menu=menu)
root.mainloop()