from tkinter import *
from tkinter import messagebox

def hello():
    pass

root = Tk()
root.title('8.add_checkbutton方法')
root.geometry('500x200')

def new():
    messagebox.showinfo('新建文档','新建文档')
def open():
    messagebox.showinfo('打开文档','打开文档')
def save():
    messagebox.showinfo('保存文档','保存文档')
def saveas():
    messagebox.showinfo('另存为','另存为') 
def aboutme(*args): 
    messagebox.showinfo('关于','小李飞刀他妈所著') 

def lblstatus(*args): 
    if status.get():
        lbl.pack(side=BOTTOM,fill=X)
    else:
        lbl.pack_forget()       #移除控件，但并没有进行摧毁，可以再次使用pack或其他方式来显示

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
 
status = BooleanVar()
status.set(True)
filemenu.add_checkbutton(label='Status',command=lblstatus,variable=status,accelerator='Ctrl+L')

#字母大小写均进行绑定
root.bind('<Control-N>',aboutme) 
root.bind('<Control-n>',aboutme)  

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
menu.add_cascade(label='帮助',menu = helpmenu) 

helpmenu.add_command(label='检查更新')
helpmenu.add_command(label='关于',command = aboutme)

#显示菜单对象
root.configure(menu=menu)

var = StringVar()
var.set('显示')
lbl = Label(root,textvariable=var,relief='raised')
lbl.pack(side=BOTTOM,fill=X)

root.mainloop()