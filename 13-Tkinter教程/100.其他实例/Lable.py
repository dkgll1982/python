#coding=utf-8
import tkinter as tk
 
if __name__ == "__main__":
    import tkinter as tk
    master = tk.Tk()
    str_obj = tk.StringVar()
    str_obj.set("这是TKinter所支持的字符串类型")
 
    #bitmap_image = tk.BitmapImage(file = "./tmp/11.bmp")
    normal_image = tk.PhotoImage(file = r"images\gif\1.gif")
    print(type(normal_image))
    print(normal_image)
    w = tk.Label(master,
                 #背景选项
                 #height = 5,
                 #width = 20,
                 padx=10,
                 pady=20,
                 background="blue",
                 relief="ridge",
                 borderwidth=10,
                 #文本
                 text = "123456789\nabcde\nABCDEFG",
                 #textvariable = str_obj,
                 justify = "left",
                 foreground = "red",  
                 fg="yellow",
                 font=('微软雅黑', 13, 'bold'),
                 underline = 4,
                 anchor = "ne",
                 #图像
                 image = normal_image,
                 compound = "center", 
                 #接受焦点
                 #takefocus = True,
                 #highlightbackground = "yellow",
                 #highlightcolor = "white",
                 #highlightthickness = 5
                 )
    w.pack()
    master.mainloop()