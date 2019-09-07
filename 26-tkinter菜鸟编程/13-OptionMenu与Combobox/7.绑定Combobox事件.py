from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('设置Combobox默认选项')
root.geometry('300x120')

def comboSelection(event):
    lbvar.set('您喜欢吃：%s'%var.get())

var = StringVar()
cb = Combobox(root,textvariable=var)

#或者在combobox外设置选项值
cb['value'] = ("芒果",'苹果','香蕉','桔子','菠萝','椰子','榴莲','山竹')
cb.pack(pady=10)

cb.current(2) 
#虚拟ComboboxSelected事件：选中
cb.bind('<<ComboboxSelected>>',comboSelection)

style = Style() 
style.configure("BW.TLabel", foreground="red", background="white",width=36,anchor=CENTER)  #anchor=CENTER:文本在内部居中显示

lbvar = StringVar()
lbl = Label(root,textvariable=lbvar,style='BW.TLabel')
lbvar.set('你使用的样式:%s,您喜欢吃：%s'%(lbl.winfo_class(),var.get()))
lbl.pack()

root.mainloop()
