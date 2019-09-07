from tkinter import *
from tkinter import messagebox

def callback():
    res = messagebox.askokcancel('okcancel','结束或取消？')
    if res == True:
        root.destroy()
    else:
        return

root = Tk()
root.title('Protocols')
root.geometry('300x100')
#关闭窗体的协议：WM_DELETE_WINDOW
root.protocol('WM_DELETE_WINDOW',callback)

#WM_TAKE_FOCUS，WM_SAVE_YOURSELF：[这两个不知道什么来的。]
root.protocol('WM_TAKE_FOCUS',callback)
root.protocol('WM_SAVE_YOURSELF',callback)

root.mainloop()