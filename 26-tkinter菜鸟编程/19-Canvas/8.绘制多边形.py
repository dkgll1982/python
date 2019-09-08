from tkinter import *
import math

root = Tk()
canvas= Canvas(root,width=640,height=680)
canvas.pack() 
canvas.create_polygon(10,10,100,10,50,80) 
canvas.create_polygon(150,10,300,160,300,300,fill='yellow')    
canvas.create_polygon(10,200,310,350,400,200) 
canvas.create_polygon(350,200,550,300,500,300,200,600,fill='aqua',outline='blue',width=5) 

root.mainloop()