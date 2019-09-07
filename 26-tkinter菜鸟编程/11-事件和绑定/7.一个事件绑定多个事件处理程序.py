from tkinter import *

def buttonClicked1(*args):
    if (args==()): 
        print("Command event handle,I like tkinter")
    else: 
        print("1):Bind event handle,I like tkinter") 

def buttonClicked2(event):
    print("2):Bind event handle,I like tkinter") 

root = Tk()
root.title('取消事件绑定')
root.geometry('300x100')

btn = Button(root,text='tkinter',command = buttonClicked1 )
btn.pack(anchor=W,padx=10,pady=10)

btn.bind('<Button-1>',buttonClicked2,add='+')                #添加事件处理程序
btn.bind('<Button-1>',buttonClicked1,add='+')                #添加事件处理程序,多个事件增加参数 add='+'

#先执行bind（）绑定的事件，再执行command命令

root.mainloop()