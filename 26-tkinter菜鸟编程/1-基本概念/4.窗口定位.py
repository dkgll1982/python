
from tkinter import *

root =  Tk()

screenWidth = root.winfo_screenwidth()      #屏幕宽度
screenHeight = root.winfo_screenheight()    #屏幕高度

w = 400                                     #窗口宽度
h = 400                                     #窗口高度
x = (screenWidth - w)                       #窗口右下角x轴位置
y = (screenHeight - h)                      #窗口右下角y轴位置

root.geometry('%dx%d+%d+%d'%(w,h,x,y))
root.title("窗口右下角")
lbl = Label(root,text="窗口右下角")
lbl.pack(fill=BOTH,side=LEFT,expand=Y)
root.mainloop()


