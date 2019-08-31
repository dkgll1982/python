from tkinter import * 
root = Tk()
root.geometry('500x420+400+100')

#城市字典
cdict ={
    '32011':'长兴县',
    '320012':'安吉县',
    '430000':'武汉',
    '430001':'随州',
    '430002':'恩施',
    '430003':'十堰',
    '430004':'天门',
    '330000':'信阳'
}

def printSelection(): 
  label.config(text='选择城市:'+cdict[var.get()]) 

var = StringVar()
var.set('430000')

label = Label(root,text='选择城市:'+cdict[var.get()],bg = 'lightyellow',width=30)
label.pack()

for key,value in cdict.items():
    Radiobutton(root,text=value,variable=var,value=key,command=printSelection).pack()
 
root.mainloop()