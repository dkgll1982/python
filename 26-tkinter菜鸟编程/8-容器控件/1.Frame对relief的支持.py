from tkinter import Tk
from tkinter.ttk import Frame,Style,Button

root = Tk()
root.title("框架")

style = Style()
style.theme_use('alt')
style.layout("RoundedFrame", [("RoundedFrame", {"sticky": "nsew"})])
style.configure("TEntry", borderwidth=0)

#('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
print(style.theme_names())  

frm1 = Frame(root,width=150,height=100,relief='flat')
frm1.grid(row=0,column=0,padx=5,pady=5)

frm2 = Frame(root,width=150,height=100,relief='groove')
frm2.grid(row=0,column=1,padx=5,pady=5) 

frm3 = Frame(root,width=150,height=100,relief='raised')
frm3.grid(row=0,column=2,padx=5,pady=5) 

frm4 = Frame(root,width=150,height=100,relief='ridge')
frm4.grid(row=1,column=0,padx=5,pady=5)

frm5 = Frame(root,width=150,height=100,relief='solid')
frm5.grid(row=1,column=1,padx=5,pady=5)

frm6 = Frame(root,width=150,height=100,relief='sunken')
frm6.grid(row=1,column=2,padx=5,pady=5)

#ttk—Tkinter的进阶版，界面美化，用法如下：
style = Style()
style.configure("BW.TButton",font=('Times',15,'bold'),foreground='white',background='pink')
style.configure("BW.TLabel",font=('Times',20)) 

btn =Button(root,text='ttk.button',style="BW.TButton")
btn.grid(row=2,column=0,padx=5,pady=5)

root.mainloop()



