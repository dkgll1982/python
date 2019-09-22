
from tkinter import *

class window:
    def show(root): 
        root.title("MyWindow")

        w,h = 800,500
        x = (root.winfo_screenwidth()-w)/2
        y = (root.winfo_screenheight()-h)/2  

        root.geometry('%dx%d+%d+%d'%(w,h,x,y))

        root.configure(bg = 'lightgray')

        #设置窗口小图标（必须位于geometry、resizeable方法之后）
        root.iconbitmap(r'images\ico\Porsche.ico') 
        
# if __name__ =="__main__":
#     window.show()