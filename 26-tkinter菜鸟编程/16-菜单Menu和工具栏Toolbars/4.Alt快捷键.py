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
def aboutme():
    messagebox.showinfo('关于','小李飞刀他妈所著') 

#建立最上层菜单
menu = Menu(root)

#建立菜单类别对象
filemenu = Menu(menu,tearoff=0)
menu.add_cascade(label='File',menu = filemenu)

#在filemenu里建立菜单列表
filemenu.add_command(label='NewFile',command = new,underline=0)
filemenu.add_command(label='Open',command = open,underline=0)

#加上分隔线
filemenu.add_separator()

filemenu.add_command(label='Save',command = save,underline=0)
filemenu.add_command(label='Save as',command = saveas,underline=5) 
filemenu.add_separator()
filemenu.add_command(label='Exit',command = root.destroy,underline=0)
 
#再建立一个新的菜单类别对象
#每次新建一组菜单类别，需要增加以下两行代码
om1 = Menu(menu,tearoff=0)
menu.add_cascade(label='编辑',menu = om1) 

om2 = Menu(menu,tearoff=0)
menu.add_cascade(label='选择',menu = om2) 

om3 = Menu(menu,tearoff=0)
menu.add_cascade(label='查看',menu = om3) 

om4 = Menu(menu,tearoff=0)
menu.add_cascade(label='转到',menu = om4) 

om5 = Menu(menu,tearoff=0)
menu.add_cascade(label='调试',menu = om5) 

om6 = Menu(menu,tearoff=0)
menu.add_cascade(label='终端',menu = om6)  

helpmenu = Menu(menu,tearoff=0)
menu.add_cascade(label='Help',menu = helpmenu,underline=0) 

helpmenu.add_command(label='检查更新')
helpmenu.add_command(label='About me',command = aboutme,underline=1)

#显示菜单对象
root.configure(menu=menu)
root.mainloop()