from tkinter import *
import math

root = Tk()

canvas = Canvas(root,width=640,height=480)
canvas.pack()

x_center,y_center,r = 320,240,100
x,y=[],[]
for i in range(12):                 #建立圈外外围12个点
    x.append(x_center+r*math.cos(30*i*math.pi/180))
    y.append(y_center+r*math.sin(30*i*math.pi/180))

for i in range(12):
    for j in range(12):
        canvas.create_line(x[i],y[i],x[j],y[j])

root.mainloop()