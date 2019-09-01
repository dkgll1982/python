from tkinter import *
from tkinter import messagebox

def leave(event):                                       #Esc事件处理程序
    msg = messagebox.askyesno('确认窗口','是否离开？')
    if msg == True:                                     #接收对话框回传值，进行下一步预处理
        #destroy：Destroy this and all descendants widgets. This will end the application of this Tcl interpreter.
        #quit: Quit the Tcl interpreter. All widgets will be destroyed
        root.destroy()
        #root.quit()
    else:
        return

root = Tk()
root.geometry('500x400+550+200')
root.title('键盘事件')

root.bind('<Escape>',leave)

lbl = Label(root,
            text="测试Esc键",
            bg='yellow',
            fg='blue',
            height=4,
            width=15,
            font='Times 12 bold')            
lbl.pack(padx=30,pady=30)

root.mainloop()