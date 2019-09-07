from tkinter import *  

fruits = ["芒果",'苹果','香蕉','桔子','菠萝','椰子','榴莲','山竹','沙果','海棠','野樱莓','枇杷','欧楂','山楂','梨(香梨,雪梨 等)','温柏','蔷薇果']

root = Tk()
root.title('带滚动条的Listbox')
root.geometry('250x300+400+200') 

scroll  = Scrollbar(root,troughcolor='blue',cursor='star',highlightcolor='red',bg='green')
scroll.pack(side=RIGHT,fill=Y)

#xscrollcommand： 为 Listbox 组件添加一条水平滚动条，将此选项与 Scrollbar 组件相关联即可 
#yscrollcommand：为 Listbox 组件添加一条垂直滚动条，将此选项与 Scrollbar 组件相关联即可
lb = Listbox(root,yscrollcommand=scroll.set)  
for fruit in fruits:
    lb.insert(END,fruit)
     
lb.pack(pady=10,padx=10,fill=BOTH,side=LEFT,expand=True)  

scroll.config(command=lb.yview)

root.mainloop()
