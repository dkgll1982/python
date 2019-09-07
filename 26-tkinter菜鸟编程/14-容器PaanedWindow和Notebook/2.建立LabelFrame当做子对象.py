from tkinter import *

root = Tk()
root.title('建立LabelFrame当做子对象')

pw = PanedWindow(orient=HORIZONTAL)

leftfrm = LabelFrame(pw,text='left pane',width=120,height=150)
pw.add(leftfrm)

midfrm = LabelFrame(pw,text='middle pane',width=120)
pw.add(midfrm)

rightfrm = LabelFrame(pw,text='right pane',width=120)
pw.add(rightfrm)

pw.pack(fill=BOTH,expand=True,padx=10,pady=10) 

root.mainloop()