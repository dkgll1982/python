from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('设置Combobox默认选项')
root.geometry('300x120')

var = StringVar()
cb = Combobox(root,textvariable=var)

#或者在combobox外设置选项值
cb['value'] = ("芒果",'苹果','香蕉','桔子','菠萝','椰子','榴莲','山竹')
cb.pack(pady=10)

cb.current(2)
#获得目前选项
print(var.get())

#由于用到绑定变量，此时也可以用var.set('xxxx')的方式建立默认选项
var.set('榴莲')

root.mainloop()
