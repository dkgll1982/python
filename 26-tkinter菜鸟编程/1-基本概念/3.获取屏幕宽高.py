
from tkinter import *

root =  Tk()

screenWidth = root.winfo_screenwidth()      #屏幕宽度
screenHeight = root.winfo_screenheight()    #屏幕高度

w = 800                                     #窗口宽度
h = 500                                     #窗口高度
x = (screenWidth - w)/2                     #窗口左上角x轴位置
y = (screenHeight - h)/2                    #窗口左上角y轴位置

root.geometry('%dx%d+%d+%d'%(w,h,x,y))

root.mainloop()


