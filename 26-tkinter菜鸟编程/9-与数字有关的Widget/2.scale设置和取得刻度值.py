from tkinter  import *

root = Tk()

root.title('刻度')
var = StringVar()
slider1 = Scale(root,
                label='垂直方向',
                relief='solid',
                from_ = 0,
                to=10,
                orient=VERTICAL,
                troughcolor='yellow',
                tickinterval=2,
                width=10,               #槽的高度
                length=200)
slider1.set(5)                
slider1.pack()

slider2 = Scale(root,
                label='水平方向',
                relief='raised',
                from_ = 0,
                to=10,
                length=400,
                tickinterval=1,
                troughcolor='pink',
                width=20,               #槽的高度
                orient=HORIZONTAL)
slider2.set(2)                
slider2.pack()

var.set('垂直尺度值=%d,水平刻度值=%d'%(slider1.get(),slider2.get()))
lbl = Label(root,textvariable=var,padx=10,fg='#FA8072')
lbl.pack()           

def gettick(*args):
    var.set('垂直尺度值=%d,水平刻度值=%d'%(slider1.get(),slider2.get()))

#slider1.config(command=gettick)    
slider2.config(command=gettick)

btn = Button(root,text='获取刻度值',command=gettick)
btn.pack()

root.mainloop()