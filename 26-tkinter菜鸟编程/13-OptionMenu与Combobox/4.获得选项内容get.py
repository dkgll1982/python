from tkinter import *

root =Tk()
root.title('菜单')
root.geometry('300x180')

def printselection():
    print('you select：%s'%var.get())
    
var = StringVar()

omTuple = ("python","java","c","c++",'c#','Node','ruby','golan','php','dephi','perl')   
menu = OptionMenu(root,var,*omTuple ) 
menu.pack()

var.set('ruby')
#也可以采用元组变量名称+索引方式设置默认选项
var.set(omTuple[4])


btn = Button(root,text='获取选中项',command = printselection)
btn.pack(pady=10,anchor=S,side=BOTTOM)

root.mainloop()