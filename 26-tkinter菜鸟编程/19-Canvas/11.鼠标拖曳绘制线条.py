from tkinter import *

def paint(event):
    x1,y1 = event.x,event.y
    canvas.create_oval(x1,y1,x1+2,y1+2,fill='blue')   #绘制极小圆

def cls():
    canvas.delete('all')                        #删除画布

root = Tk()
lab = Label(root,text='拖曳鼠标可以绘图')
lab.pack()
canvas = Canvas(root,width=640,height=300)
canvas.pack()

btn = Button(root,text='清除',command = cls)
btn.pack(pady=5)

canvas.bind('<B1-Motion>',paint)        #鼠标拖曳绑定paint

canvas.mainloop()