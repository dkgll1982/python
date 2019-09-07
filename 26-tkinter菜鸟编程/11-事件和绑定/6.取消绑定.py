from tkinter import *

def buttonClicked(event):
    print("I like tkinter")

def toggle(onoff):
    if var.get()==True:
        onoff.bind('<Button-1>',buttonClicked)
    else:
        onoff.unbind('<Button-1>')

root = Tk()
root.title('取消事件绑定')
root.geometry('300x100')

btn = Button(root,text='tkinter')
btn.pack(anchor=W,padx=10,pady=10)

var = BooleanVar()
cbtn = Checkbutton(root,text='bind/unbind',variable=var,command=lambda:toggle(btn))

cbtn.pack(anchor=W,padx=10)

root.mainloop()