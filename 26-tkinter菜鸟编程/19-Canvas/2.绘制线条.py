from tkinter import *
import math

root = Tk()
canvas= Canvas(root,width=640,height=480)
canvas.pack()
canvas.create_line(100,100,200,100,200,200,100,200,100,100,width=5,fill='lightblue',joinstyle=BEVEL) 
canvas.create_line(150,150,250,150,250,250,150,250,150,150,width=5,fill='lightblue',joinstyle='round') 

canvas.create_line(350,150,550,150,450,200,350,150,width=5,fill='lightblue',joinstyle='miter') 

root.mainloop()