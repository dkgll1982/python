from tkinter import * 

fruits = ["芒果",'苹果','香蕉','桔子','菠萝','椰子','榴莲','山竹']

root = Tk()
root.title('Listbox项目的排序')
root.geometry('450x350')
  
def itemsorted():  
    listTmp = list(lb.get(0,END))                       #取的项目内容
    sortedList = sorted(listTmp,reverse=var.get())      #从小到大是True，生成排序后的列表项
    lb.delete(0,END)                                    #删除原先Lixtbox的内容
    for item in sortedList:
        lb.insert(END,item)                             #将排序结果插入Listbox

lb = Listbox(root,selectmode=EXTENDED)  
for fruit in fruits:
    lb.insert(END,fruit)
    
lb.pack(side=TOP,pady=10,padx=10) 

btn = Button(root,text='排序',command=itemsorted)
btn.pack(side=LEFT,padx=10,pady=5)
 
var = BooleanVar() 
chk = Checkbutton(root,text='从小到大排序',variable=var)
chk.pack(side=LEFT,pady=5) 

root.mainloop()
