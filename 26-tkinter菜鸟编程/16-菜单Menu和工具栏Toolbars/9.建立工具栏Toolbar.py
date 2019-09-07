from tkinter import *

root = Tk()
root.title('建立工具栏Toolbar')
root.geometry('300x100')

menu = Menu(root)
#建立菜单类别对象，并将此菜单类别命名File
filemenu = Menu(menu,tearoff=False)
menu.add_cascade(label='File',menu=filemenu)
#在file菜单内建立菜单列表Exit
filemenu.add_command(label='Exit',command=root.destroy)

#建立工具栏
toolbar = Frame(root,relief=RAISED,bd=3)
#在工具栏里创建按钮
sunGif = PhotoImage(file=r'images\remove.gif')
btn = Button(toolbar,image=sunGif,command=root.destroy)
btn.pack(side=LEFT,padx=3,pady=3)       #包装按钮
toolbar.pack(side=TOP,fill=X)           #包装工具栏

root.config(men=menu)
root.mainloop()