from tkinter import *
import math

root = Tk()
canvas= Canvas(root,width=640,height=480)
canvas.pack()
canvas.create_line(30,30,500,30,width=10,capstyle=BUTT) 
canvas.create_line(30,130,500,130,width=10,capstyle='round') 
canvas.create_line(30,230,500,230,width=10,capstyle=PROJECTING)

#以下垂直线
canvas.create_line(30,20,30,240) 
canvas.create_line(500,20,500,250) 

root.mainloop()