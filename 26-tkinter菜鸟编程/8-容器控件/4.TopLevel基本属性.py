from tkinter import *

root=Tk()
root.title('顶层窗口')
root.geometry('600x400+500+200')

t1 = Toplevel()
t1.title("子窗体")
t1.geometry('300x180+200+200')
Label(t1,text="I am a Toplevel").pack()

root.mainloop()