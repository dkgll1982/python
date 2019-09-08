from tkinter import *
import math

root = Tk()
canvas= Canvas(root,width=640,height=480)
canvas.pack()
canvas.create_line(50,30,500,30,width=10,capstyle=BUTT,stipple='gray25') 
canvas.create_line(50,130,500,130,width=40,capstyle='round',stipple='questhead') 
canvas.create_line(50,230,500,230,width=10,capstyle=PROJECTING,stipple='info')
 

root.mainloop()