from tkinter import *
import time
import random

root = Tk()
canvas = Canvas(root,width=500,height=580)
canvas.pack()
id1 = canvas.create_oval(10,50,60,100,fill='yellow',outline='lightgray')
id2 = canvas.create_oval(10,550,60,500,fill='aqua',outline='lightgray')

# for x in range(0,450):
#     canvas.move(id1,1,1)          # ID=1 x轴移动5像素,y轴不变
#     canvas.move(id2,1,-1)         # ID=1 x轴移动5像素,y轴不变
#     root.update()
#     time.sleep(0.01)

 #随机移动
for x in range(0,800):
    if random.randint(1,100)>40:
        canvas.move(id2,1,0)        # ID=1 x轴移动5像素,y轴不变
    else:
        canvas.move(id1,1,0)        # ID=1 x轴移动5像素,y轴不变 
    root.update()
    time.sleep(0.01)   