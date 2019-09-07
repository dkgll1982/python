from tkinter import *

root =Tk()
root.title('菜单')
root.geometry('300x180')

var = StringVar(root)
menu = OptionMenu(root,var,"python","java","c","c++",'c#','Node','ruby','golan','php','dephi','perl','Javascript')
menu.pack()

var.set('Javascript')
root.mainloop()