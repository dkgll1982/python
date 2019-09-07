from tkinter import * 

root = Tk()
root.title('选取指定索引项')
root.geometry('350x250')

var = StringVar()
var.set(("芒 果",'苹果','香蕉','桔子','菠萝','椰子','榴莲','山竹'))

#在 StringVar 类型的变量中，用空格分隔每个项目，例如 var.set(“鸡蛋 鸭蛋 鹅蛋 李狗蛋”)
#var.set("芒果 苹果 香蕉 桔子 菠萝 椰子 榴莲 山竹")
 
#.Listbox与变量绑定:listvariable
lb = Listbox(root,selectmode=EXTENDED,listvariable =var)    

lb.pack(pady=10)   
 
lb.select_set(1,2) 
lb.select_set(4,6) 

root.mainloop()
