from tkinter import *

fruits = ["芒果",'苹果','香蕉',]

root = Tk()
root.title('在前一组前面补充建立项目')
root.geometry('350x250')

#lb = Listbox(root,selectmode=MULTIPLE)      #建立可以多选项的listbox
lb = Listbox(root,selectmode=EXTENDED)       #可以用拖拽的方式选择区间多个项目

for fruit in fruits:
    lb.insert(END,fruit)

lb.insert(ACTIVE,'桔子','菠萝','椰子')        #在前一组前面补充建立三个项目

lb.pack(pady=10)

root.mainloop()
