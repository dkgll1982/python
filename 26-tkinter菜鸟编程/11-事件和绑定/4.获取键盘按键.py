from tkinter import *
from tkinter import messagebox

def key(event):                                       #Esc事件处理程序
    txt = '按下'+repr(event.char)+'键'
    print(txt)
    # lbl["text"]、lbl.config或者设置textvariable变量的方式来更新值
    #lbl["text"]=txt
    lbl.config(text=txt)

root = Tk()
root.geometry('400x300+550+100')
root.title('获取键盘按键')

root.bind('<Key>',key)

lbl = Label(root,
            text="",
            bg='yellow',
            fg='blue',
            height=4,
            width=11,
            font='Times 12 bold')            
lbl.pack(padx=30,pady=30)

root.mainloop()