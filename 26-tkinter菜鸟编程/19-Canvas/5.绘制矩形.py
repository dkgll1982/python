from tkinter import *
from random import *

root = Tk()
canvas= Canvas(root,width=640,height=480)
canvas.pack()

# for x in range(50):                          #随机绘制50个不同位置大小的矩形
#     x1,y1 = randint(1,640),randint(1,480)
#     x2,y2 = randint(1,640),randint(1,480)
#     if x1>x2:
#         x1,x2=x2,x1                          #确保左上角X坐标小于右下角X坐标
#     if y1>y2:           
#         y1,y2=y2,y1                          #确保左上角y坐标小于右下角y坐标
#     canvas.create_rectangle(x1,y1,x2,y2)


for x in range(200):                          #随机绘制500个不同位置大小的正方形
    x1,y1 = randint(1,590),randint(1,430)  
    x2,y2 = x1+50,y1+50 
    if x%4==0: 
        canvas.create_rectangle(x1,y1,x2,y2,fill='blue')    
    elif x%11==0: 
        canvas.create_rectangle(x1,y1,x2,y2,fill='yellow')    
    elif x%17==0: 
        canvas.create_rectangle(x1,y1,x2,y2,fill='green')    
    else:
        canvas.create_rectangle(x1,y1,x2,y2) 
    
root.mainloop()