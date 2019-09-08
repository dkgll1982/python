from tkinter import *
import math

root = Tk()
canvas= Canvas(root,width=640,height=680,bg='lightpink')
canvas.pack()  
canvas.create_text(150,110,text='好好学习天天上香', fill='red')    
canvas.create_text(50,200,text='多对多22',fill='blue' ) 
canvas.create_text(350,400,text='my name is han meimei',fill='blue' ) 

root.mainloop()