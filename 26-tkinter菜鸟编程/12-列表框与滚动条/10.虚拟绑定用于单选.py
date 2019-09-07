from tkinter import *

def itemSelect(event):                        #取得所选单一项目
    obj = event.widget                        #取得事件的对象，也可以直接使用lb对象
    print('调用对象是否标签lb：%s'%(lb==obj))   #当选中lb时触发调用本方法时，event.widget就是lb本身  
    #index = lb.curselection()          
    index = obj.curselection()                #取得索引
    var.set(obj.get(index))                   #设置标签内容

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
root.title('虚拟绑定用于单选')
root.geometry('450x350')
 
var = StringVar()                             #建立标签 
lbl = Label(root,text="",textvariable=var) 
lbl.pack(pady=5)

lb = Listbox(root)  
for fruit in fruits:
    lb.insert(END,fruit)
lb.bind('<<ListboxSelect>>',itemSelect) 
#早期用双击方式进行处理，因为单击用于选取项目
#lb.bind('<Double-Button-1>',itemSelect) 
lb.pack(pady=10) 

btn = Button(root,text='检查是否选中',command=callback)
btn.pack(pady=5)

root.mainloop()
