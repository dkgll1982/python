from tkinter import *

fruits = ["芒果",'苹果','香蕉','桔子','菠萝','椰子']

root = Tk()
root.title('ListBox')
root.geometry('350x250')

#lb = Listbox(root,selectmode=MULTIPLE)      #建立可以多选项的listbox
lb = Listbox(root,selectmode=EXTENDED)       #可以用拖拽的方式选择区间多个项目

for fruit in fruits:
    lb.insert(END,fruit)


#activate(index)：-- 将给定索引号对应的选项激活（在其文本下方画一条下划线）
#测试发现激活项只能设置一个
lb.activate(1)
lb.activate(2)

lb.pack(pady=10)

root.mainloop()
