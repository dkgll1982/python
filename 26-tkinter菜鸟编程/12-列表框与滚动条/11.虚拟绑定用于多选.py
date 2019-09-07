from tkinter import *

def itemSelect(event):                        #取得所选单一项目
    obj = event.widget                        #取得事件的对象，也可以直接使用lb对象  
    indexs = obj.curselection()               #取得索引
    str = ''
    for ind in indexs:
        str+=obj.get(ind)+','
    var.set(str[:-1])                         #设置标签内容 

fruits = ["芒果",'苹果','香蕉','桔子','菠萝','椰子','榴莲','山竹']

root = Tk()
root.title('虚拟绑定用于多选')
root.geometry('450x350')
 
var = StringVar()                             #建立标签 
lbl = Label(root,text="",textvariable=var) 
lbl.pack(pady=5)

lb = Listbox(root,selectmode=EXTENDED)  
for fruit in fruits:
    lb.insert(END,fruit)
lb.bind('<<ListboxSelect>>',itemSelect)  
lb.pack(pady=10) 
 
root.mainloop()
