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

def btnclick():
     lbl_var.set('Button Clicked')

root = Tk()
root.geometry('500x400+550+200')
root.title('command参数复习')

btn = Button(root,text='Click me',command=btnclick)
btn.pack(anchor=W)

var_python,var_java,lbl_var = BooleanVar(),BooleanVar(),StringVar()

# 区分variable、textvariable
# variable（通常绑定组件的 value）、textvariable（通常绑定组件显示的文本）
cbnPython = Checkbutton(root,text="Python",variable=var_python,command=pythonclick)
cbnPython.pack(anchor=W)

cbnjava = Checkbutton(root,text="Java",variable=var_java,command=javaclick)
cbnjava.pack(anchor=W)

lbl = Label(root,bg='yellow',fg='blue',height=2,width=15,font='Times 16 bold',textvariable=lbl_var)
lbl.pack()

root.mainloop()