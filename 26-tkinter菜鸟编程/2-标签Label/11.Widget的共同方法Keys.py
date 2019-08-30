from tkinter import *  
from tkinter import ttk

# 引入字体模块
import tkinter.font as tkFont
import sys,os  
sys.path.append(os.path.dirname(os.path.dirname(__file__)) )   
from singlewindow  import *

root = Tk() 
window.show(root) 
 
root.geometry('1300x710+100+30')
root.title("获取控件的属性")

lbl = Label(root,text="I like tkinter",padx=10,height=2,relief='solid')
#lbl.pack(pady=20)

text = Text(width=80,height=45,fg="green")
text.pack() 

#################################################
#组件列表
entry = Entry(root)
listbox = Listbox(root)
check = Checkbutton(root)
radio = Radiobutton(root)
frm = Frame(root)
lblfrm = LabelFrame(root)
spin = Spinbox(root)
scroll = Scrollbar(root)
combox = ttk.Combobox(root)
menu = Menu(root)
menubtn = Menubutton(root) 
message = Message(root)
option = OptionMenu(root, "one", "two", "three")
scale = Scale(root)
notebook = ttk.Notebook(root)
Progress = ttk.Progressbar(root)
sep = ttk.Separator(root)
Tree = ttk.Treeview(root)
Paned = PanedWindow(root)
cancvs = Canvas(root)
toplvl = Toplevel(root)
sizegrip = ttk.Sizegrip(root)
################################################# 

def get(widge):
    text.delete('1.0','end') 
    text.insert(END,str(widge).replace('.!','')+'的key如下：\n')
    for item in widge.keys():  
        text.insert(END,item+'\n')
    
btn1 = Button(text = "label的key",command = lambda:get(lbl))
btn1.pack(side='left',padx = 10)

Button(text = "button的key",command = lambda:get(btn1)).pack(side='left') 
Button(text = "Text的key",command = lambda:get(text)).pack(side='left',padx =5)  
Button(text = "entry的key",command = lambda:get(entry)).pack(side='left') 
Button(text = "listbox的key",command = lambda:get(listbox)).pack(side='left',padx =5) 
Button(text = "checkbtn的key",command = lambda:get(check)).pack(side='left') 
Button(text = "radiobtn的key",command = lambda:get(radio)).pack(side='left',padx =5)  
Button(text = "Frame的key",command = lambda:get(frm)).pack(side='left')  
Button(text = "LabelFrame的key",command = lambda:get(lblfrm)).pack(side='left',padx =5)  
Button(text = "Spinbox的key",command = lambda:get(spin)).pack(side='left')  
Button(text = "Scrollbar的key",command = lambda:get(scroll)).pack(side='left',padx =5)  
Button(text = "Message的key",command = lambda:get(message)).pack(side='left')  
Button(text = "Combobox的key",command = lambda:get(combox)).pack(side='left',padx =5)  
Button(text = "Menu的key",command = lambda:get(menu)).pack(side='left')  
Button(text = "Menubutton的key",command = lambda:get(menubtn)).place(x=10,y=670)
Button(text = "OptionMenu的key",command = lambda:get(option)).place(x=130,y=670)
Button(text = "Scale的key",command = lambda:get(scale)).place(x=250,y=670)
Button(text = "Notebook的key",command = lambda:get(notebook)).place(x=330,y=670)
Button(text = "Progressbar的key",command = lambda:get(Progress)).place(x=440,y=670)
Button(text = "Separator的key",command = lambda:get(sep)).place(x=560,y=670)
Button(text = "Treeview的key",command = lambda:get(Tree)).place(x=670,y=670)
Button(text = "PanedWindow的key",command = lambda:get(Paned)).place(x=770,y=670)
Button(text = "Canvas的key",command = lambda:get(cancvs)).place(x=900,y=670)
Button(text = "Toplevel的key",command = lambda:get(toplvl)).place(x=990,y=670)
Button(text = "Sizegrip的key",command = lambda:get(sizegrip)).place(x=1090,y=670)

root.mainloop()