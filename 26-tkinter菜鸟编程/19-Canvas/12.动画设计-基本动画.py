from tkinter import *
import time

root = Tk()
canvas = Canvas(root,width=500,height=550)
canvas.pack()
canvas.create_oval(10,50,60,100,fill='yellow',outline='lightgray')

for x in range(0,400):
    canvas.move(1,1,1)          # ID=1 x轴移动5像素,y轴不变
    root.update()
    time.sleep(0.01)