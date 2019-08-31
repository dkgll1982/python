from tkinter import *
import random

root=Tk()
root.title('顶层窗口')
root.geometry('600x400+500+200')

msgyes,msgno,msgExit = 1,2,3

def MessageBox():
    msgType = random.randint(1,3)   #随机数产生对话框方式
    if msgType == msgyes:           #产生Yes字符串
        lblTxt = 'Yes'
    elif msgType == msgno:
        lblTxt = 'No'
    elif msgType == msgExit:
        lblTxt = 'Exit'
 
    t1 = Toplevel()
    t1.title("消息对话框")
    t1.geometry('300x180+550+220')
    Label(t1,text=lblTxt).pack(fill=BOTH,expand=True)

btn = Button(root,text='Click Me',command = MessageBox)
btn.pack()

root.mainloop()