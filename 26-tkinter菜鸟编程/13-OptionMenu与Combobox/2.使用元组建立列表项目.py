from tkinter import *

root =Tk()
root.title('菜单')
root.geometry('300x180')

var = StringVar()

omTuple = ("python","java","c","c++",'c#','Node','ruby','golan','php','dephi','perl')  

# 此处采用逆向参数收集，将元组元素“拆开”后传给函数的参数，相当于OptionMenu(root,var,"python","java","c","c++",'c#','Node','ruby','golan','php','dephi','perl')
# 如果不使用逆向收集（不在元组参数之前添加星号），整个元组将会作为一个参数，而不是将元组的元素作为多个参数，最终只会显示由元组元素拼成的一项
menu = OptionMenu(root,var,*omTuple )
#menu = OptionMenu(root,var,omTuple )

menu.pack()

root.mainloop()