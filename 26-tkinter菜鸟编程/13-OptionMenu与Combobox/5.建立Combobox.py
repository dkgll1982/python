from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('建立Combobox')
root.geometry('300x120')

var = StringVar()
cb = Combobox(root,textvariable=var, state='readonly',
            value=("python","java","c","c++",'c#','Node','ruby','golan','php','dephi','perl'))

#或者在combobox外设置选项值
cb['value'] = ("芒果",'苹果','香蕉','桔子','菠萝','椰子','榴莲','山竹')
cb.pack(pady=10)

root.mainloop()
