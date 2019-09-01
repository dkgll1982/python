from tkinter import *
from tkinter import messagebox

def key(event):                                         #Esc事件处理程序
    txt = '按下'+repr(event.char)+'键' 
    lbl.config(text=txt)

def coordXY(event):
    frm.focus_set()                                     #只能先鼠标单击时，获得焦点，这时才能使<KEY>事件生效
    txt = '鼠标坐标：%d,%d'%(event.x,event.y)
    lbl.config(text=txt)

root = Tk()
root.geometry('400x300+550+100')
root.title('获取键盘按键')

frm = Frame(root,width=100,height=100,bg='pink')
frm.bind('<Key>',key)                   #frame对象的<KEY>绑定Key
frm.bind('<Button-1>',coordXY)          #frame对象单击绑定绑定coordXY 

#在root窗口执行绑定，启动时此窗口已经获得焦点，不需要先进行单击获得焦点
#root.bind('<Key>',key)                   #frame对象的<KEY>绑定Key
#root.bind('<Button-1>',coordXY)          #frame对象单击绑定绑定coordXY 

frm.pack()

lbl = Label(root,
            text="",
            bg='yellow',
            fg='blue',
            height=4,
            width=31,
            font='Times 12 bold')            
lbl.pack(padx=30,pady=30)

root.mainloop()