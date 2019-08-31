from tkinter import *

#以下是callback方法
def selAll():
    entry.select_range(0,END)

def deSel():
    entry.select_clear()

def clr():
    entry.delete(0,END)
    
def readonly():
    if var.get()==True:
        entry.config(state=DISABLED)
    else:
        entry.config(state=NORMAL)

root = Tk()
root.title("my demo")
root.geometry('500x300+200+200')

#以下row=0建立Entry
entry = Entry(root)
entry.grid(row=0,column=0,columnspan=4,padx=5,pady=5,sticky=W)

#以下row=1建立Button
btnSel = Button(root,text='选取',command=selAll)
btnSel.grid(row=1,column=0,padx=5,pady=5,sticky=W)

btnDelSel = Button(root,text='取消选取',command=deSel)
btnDelSel.grid(row=1,column=1,padx=5,pady=5,sticky=W)

btnClr = Button(root,text="删除",command=clr)
btnClr.grid(row=1,column=2,padx=5,pady=5,sticky=W)

btnQuit = Button(root,text='结束',command=root.destroy)
btnQuit.grid(row=1,column=3,padx=5,pady=5,sticky=W)

#以下row=2建立Checkboxes
var = BooleanVar()
var.set(False)

chkReadonly = Checkbutton(root,text='只读',variable=var,command=readonly)
chkReadonly.grid(row=2,column=0)

root.mainloop()