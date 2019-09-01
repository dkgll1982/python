from tkinter import *

def pythonclick():
    if var_python.get():
        lbl_var.set('Select Python')
    else:
         lbl_var.set('Unselect Python')

def javaclick():
    if var_java.get():
         lbl_var.set('Select Java')
    else:
        lbl_var.set('Unselect Java')

def btnclick(event):
     lbl_var.set('Button Clicked!,exent_x:%d,event_y:%d'%(event.x,event.y))     #列出单击事件时的坐标

def enter(event):
    lbl_var.set('鼠标进入Click按钮!,exent_x:%d,event_y:%d'%(event.x,event.y)) 

def leave(event):
    lbl_var.set('鼠标离开Click按钮!,exent_x:%d,event_y:%d'%(event.x,event.y)) 

root = Tk()
root.geometry('500x400+550+200')
root.title('command参数复习')

#用鼠标单击事件代替command命令（实际上单击功能按钮就是执行command方法）
#btn = Button(root,text='Click me',command=btnclick)
btn = Button(root,text='Click me')

btn.bind('<Button-1>',btnclick)
btn.bind('<Enter>',enter)
btn.bind('<Leave>',leave)

btn.pack(anchor=W) 

var_python,var_java,lbl_var = BooleanVar(),BooleanVar(),StringVar()

# 区分variable、textvariable
# variable（通常绑定组件的 value）、textvariable（通常绑定组件显示的文本）
cbnPython = Checkbutton(root,text="Python",variable=var_python,command=pythonclick)
cbnPython.pack(anchor=W)

cbnjava = Checkbutton(root,text="Java",variable=var_java,command=javaclick)
cbnjava.pack(anchor=W)

lbl = Label(root,bg='yellow',fg='blue',height=2,width=35,font='Times 16 bold',textvariable=lbl_var)
lbl.pack()

root.mainloop()