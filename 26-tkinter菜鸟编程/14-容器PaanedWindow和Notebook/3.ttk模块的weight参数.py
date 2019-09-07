from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('建立LabelFrame当做子对象')

pw = PanedWindow(orient=HORIZONTAL)

leftfrm = LabelFrame(pw,text='left pane',width=120,height=150)
#pw.add(leftfrm,weight=1)                                #按比例缩放
pw.add(leftfrm,weight=3)                                #按比例缩放

midfrm = LabelFrame(pw,text='middle pane',width=120)
pw.add(midfrm,weight=1)

rightfrm = LabelFrame(pw,text='right pane',width=120)
pw.add(rightfrm,weight=1)

pw.pack(fill=BOTH,expand=True,padx=10,pady=10) 

root.mainloop()