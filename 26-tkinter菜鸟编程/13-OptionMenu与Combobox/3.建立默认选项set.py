from tkinter import *

root =Tk()
root.title('菜单')
root.geometry('300x180')

var = StringVar()

omTuple = ("python","java","c","c++",'c#','Node','ruby','golan','php','dephi','perl')   
menu = OptionMenu(root,var,*omTuple ) 
menu.pack()

var.set('ruby')
#也可以采用元组变量名称+索引方式设置默认选项
var.set(omTuple[4])

root.mainloop()