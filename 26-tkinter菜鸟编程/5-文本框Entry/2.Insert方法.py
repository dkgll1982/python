import threading
from tkinter import *  
# 引入字体模块
import tkinter.font as tkFont 
from PIL import Image,ImageTk

root = Tk()    
root.geometry('500x390+500+200')
root.title('图片管理系统')
root.configure(bg='#FFFFFF')
root.iconbitmap(r'images\ico\Alfa Romeo.ico') 
root.resizable(False, False)

frm = Frame(root)
frm.grid(row=0,column=0,padx=100,pady=5)
frm.configure(bg='#FFFFFF')

hyy = '欢迎使用图片管理系统！！！'

def printinfo():
    print("用户名：%s，密码：%s"%(entusername.get(),entpwd.get()))      #获取文本框的字符串内容

image = Image.open(r'images\jpg\6.JPG')
#重新设置图片大小
image = image.resize((300, 200), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
logo =  Label(frm,text=hyy,image = photo,compound=TOP, bg='#FFFFFF') 
logo.grid(row=0,column=0,columnspan=2,pady=10 )

lblusername = Label(frm,text="用户名",anchor=W,padx=5,bg='#FFFFFF')
lblpwd = Label(frm,text="密  码",anchor=W,padx=5,bg='#FFFFFF')

entusername = Entry(frm,width=30,bg='lightgreen')
entpwd = Entry(frm,width=30,bg='lightgreen',show='*',fg='red')

lblusername.grid(row=1,stick=W+E,pady=15 )
lblpwd.grid(row=2,stick=W+E)

entusername.grid(row=1,column=1,stick=W+E)
entpwd.grid(row=2,column=1,stick=W+E)

btkok = Button(frm,text="登录",width=7,command=printinfo)
btnquit = Button(frm,text="退出",width=7,command=root.quit)

btkok.grid(row=3,stick=W,pady=20,padx=7 )
btnquit.grid(row=3,column=1,stick=W)

entusername.insert(END,'guojun')
entpwd.insert(END,'3210')


root.mainloop()