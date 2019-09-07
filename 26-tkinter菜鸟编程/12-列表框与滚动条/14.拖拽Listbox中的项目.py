from tkinter import * 

def getIndex(event):
    #返回与给定参数 y 在垂直坐标上最接近的项目的序号
    lb.index = lb.nearest(event.y)   #目前选项的索引

def dragJob(event):
    newIndex = lb.nearest(event.y)
    if newIndex<lb.index:
        x = lb.get(newIndex)
        lb.delete(newIndex)
        lb.insert(newIndex+1,x)
        lb.index=newIndex
    elif newIndex>lb.index:
        x = lb.get(newIndex)
        lb.delete(newIndex)
        lb.insert(newIndex-1,x)
        lb.index=newIndex


fruits = ["芒果",'苹果','香蕉','桔子','菠萝','椰子','榴莲','山竹']

root = Tk()
root.title('拖拽Listbox中的项目')
root.geometry('450x350') 

lb = Listbox(root)  
for fruit in fruits:
    lb.insert(END,fruit)
    
lb.bind('<Button-1>',getIndex)
lb.bind('<B1-Motion>',dragJob) 

lb.pack(pady=10,padx=10)  

root.mainloop()
