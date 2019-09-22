from tkinter import *

root=Tk()
root.title('顶层窗口') 
 
cur_width = 800
cur_height = 600

#获取电脑屏幕的宽高（root.maxsize()或者winfo_screenwidth()、winfo_screenheight()）
scn_width,scn_height = root.maxsize()

print('%dx%d'%(root.maxsize()))
print('%dx%d'%(root.winfo_screenwidth(),root.winfo_screenheight()))

cnf = '%dx%d+%d+%d'%(cur_width,cur_height,(scn_width-cur_width)/2,(scn_height-cur_height)/2)

#获取当前窗口的宽高
cur_width = root.winfo_width()
cur_height = root.winfo_height()
 
root.geometry(cnf)

root.iconbitmap(r'images\ico\Porsche.ico') 

t1 = Toplevel()
t1.title("子窗体")
t1.geometry('300x180+600+300')
Label(t1,text="I am a Toplevel").pack()

t1.iconbitmap(r'images\ico\Ferrari.ico') 
#设置它所依托的父窗口(焦点永远在顶层)
t1.transient(root)

#传入True时，去除窗口边框
#root.overrideredirect(True)

t1.mainloop()
root.mainloop()