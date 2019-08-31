from tkinter import *

def calW(*args):
    xl.set(xe.get())

def calR(*args): 
    print("Waring:数据被读取！！！")

def hit():
    print("读取数据：",xe.get())

root = Tk()
root.geometry('200x120+400+100')

xe = StringVar()
 
entry = Entry(root,textvariable=xe)
entry.pack(pady=5,padx=10)
xe.trace('w',calW)
xe.trace('r',calR)

xl = StringVar()
lbl =Label(root,textvariable=xl)
xl.set("同步显示")
lbl.pack(pady=5,padx=10)

btn = Button(root,text="读取",command=hit)
btn.pack(pady=5)

root.mainloop()