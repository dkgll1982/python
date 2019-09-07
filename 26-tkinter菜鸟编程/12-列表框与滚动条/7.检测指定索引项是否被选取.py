from tkinter import *

def callback():                               #打印检查结果
    print('选中情况：1:%s,2:%s,3:%s,4:%s,5:%s,6:%s,7:%s,8:%s,'%(
        lb.select_includes(0),
        lb.select_includes(1),
        lb.select_includes(2),
        lb.select_includes(3),
        lb.select_includes(4),
        lb.select_includes(5),
        lb.select_includes(6),
        lb.select_includes(7) 
        )    )

fruits = ["芒果",'苹果','香蕉','桔子','菠萝','椰子','榴莲','山竹']

root = Tk()
root.title('检查列表项是否选中')
root.geometry('350x250')
 
lb = Listbox(root,selectmode=MULTIPLE)  

for fruit in fruits:
    lb.insert(END,fruit)
 
lb.pack(pady=10) 

btn = Button(root,text='检查是否选中',command=callback)
btn.pack(pady=5)

root.mainloop()
