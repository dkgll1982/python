from tkinter import *
from tkinter import messagebox

def hello():
    pass

root = Tk()
root.title('Menu的基本用法')
root.geometry('500x200')

def new():
    messagebox.showinfo('新建文档','新建文档')
def open():
    messagebox.showinfo('打开文档','打开文档')
def save():
    messagebox.showinfo('保存文档','保存文档')
def saveas():
    messagebox.showinfo('另存为','另存为') 

#建立最上层菜单
menu = Menu(root)

#建立菜单类别对象
filemenu = Menu(menu,tearoff=0)
menu.add_cascade(label='文件',menu = filemenu)

#在filemenu里建立菜单列表
filemenu.add_command(label='新建',command = new)
filemenu.add_command(label='打开',command = open)

#加上分隔线
filemenu.add_separator()

filemenu.add_command(label='保存',command = save)
filemenu.add_command(label='另存为',command = saveas) 
filemenu.add_separator()
filemenu.add_command(label='退出',command = root.destroy) 

#显示菜单对象
root.configure(menu=menu)
root.mainloop()