from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('消息对话框')
root.geometry('300x200+590+360')

def myMsg1():
    ret = messagebox.askretrycancel('Test1','安装失败，重来一次？')
    print('安装失败',ret)

def myMsg2():
    ret = messagebox.askyesnocancel('Test2','编辑完成，是或者否取消？')  #对应传回的值分别是True，False，None
    print('编辑完成',ret)

Button(root,text='安装失败',command =myMsg1).pack()
Button(root,text='编辑完成',command =myMsg2).pack(pady=10)

root.mainloop()
