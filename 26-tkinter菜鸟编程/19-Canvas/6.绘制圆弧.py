from tkinter import *
import math

root = Tk()
canvas= Canvas(root,width=640,height=480)
canvas.pack()

#以下以圆形为基础
canvas.create_arc(10,10,110,110,extent=45,style=ARC) 
canvas.create_arc(210,10,310,110,extent=90,style=PIESLICE) 
canvas.create_arc(410,10,510,110,extent=180,fill='yellow') 
canvas.create_arc(210,110,310,220,extent=359,style=ARC,width=5) 
 
#以下以椭圆形为基础 
canvas.create_arc(320,250,620,350,extent=180,style=CHORD,width=5) 
canvas.create_arc(320,360,620,460,extent=359,style=ARC,width=5,outline='blue') 

root.mainloop()