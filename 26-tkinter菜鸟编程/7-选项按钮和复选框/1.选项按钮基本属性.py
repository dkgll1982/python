from tkinter import * 
root = Tk()
root.geometry('400x220+400+100')

def printSelection(): 
  label.config(text='你是'+var.get()) 

var = StringVar()
var.set('未知')

label = Label(root,text='你是'+var.get(),bg = 'lightyellow',width=30)
label.pack()

rbman = Radiobutton(root,text='男生',variable=var,value='男生',command=printSelection,highlightcolor='blue')
rbman.pack()

rbwoman =  Radiobutton(root,text='女生',variable=var,value='女生',command=printSelection,cursor='heart',activeforeground='red')
rbwoman.pack()

rbwz =  Radiobutton(root,text='未知',variable=var,value='未知',command=printSelection)
rbwz.pack()
 
root.mainloop()