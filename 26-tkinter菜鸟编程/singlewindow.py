
from tkinter import *

class window:
    def show(root): 
        root.title("MyWindow")

        w,h,x,y = 500,300,200,200

        root.geometry('%dx%d+%d+%d'%(w,h,x,y))

        root.configure(bg = 'lightgray')

        root.iconbitmap(r'images\ico\Porsche.ico') 
        
# if __name__ =="__main__":
#     window.show()