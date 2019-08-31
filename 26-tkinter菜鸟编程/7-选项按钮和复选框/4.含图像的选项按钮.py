from tkinter import * 
import sys,os  
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from singlewindow  import *
from PIL import Image,ImageTk

root = Tk()
root.geometry('500x420+400+100')

#汽车字典
cdict = {
    'Alfa Romeo':'阿尔法罗密欧',
    'Aston Martin':'阿斯顿马丁',
    'Bugatti':'布加迪',
    'Ferrari':'法拉利',
    'Lamborghini':'兰博基尼',
    'Louts':'路特斯',
    'Maserati':'玛莎拉蒂',
    'Porsche':'保时捷'
}

def getlogo(var): 
    ico = Image.open('images\\ico\\'+var+'.ico')  
    pil_image_resized = ico.resize((20, 20), Image.ANTIALIAS)
    tk_image = ImageTk.PhotoImage(pil_image_resized)  
    return tk_image  

img1,img2,img3,img4,img5,img6,img7,img8 = getlogo('Alfa Romeo'),getlogo('Aston Martin'),getlogo('Bugatti'),getlogo('Ferrari'),getlogo('Lamborghini'),getlogo('Louts'),getlogo('Maserati'),getlogo('Porsche')

def printSelection(): 
  label.config(text='选择汽车:'+cdict[var.get()]) 

var = StringVar()
var.set('Ferrari')

label = Label(root,text='选择汽车:'+cdict[var.get()],bg = 'lightyellow',width=30)
label.pack() 

Radiobutton(root,text=cdict['Alfa Romeo'],compound=LEFT,width=330,variable=var,value='Alfa Romeo',image=img1,command=printSelection).pack(pady=5)
Radiobutton(root,text=cdict['Aston Martin'],compound=LEFT,width=330,variable=var,value='Aston Martin',image=img2,command=printSelection).pack(pady=5)
Radiobutton(root,text=cdict['Bugatti'],compound=LEFT,width=330,variable=var,value='Bugatti',image=img3,command=printSelection).pack(pady=5)
Radiobutton(root,text=cdict['Ferrari'],compound=LEFT,width=330,variable=var,value='Ferrari',image=img4,command=printSelection).pack(pady=5)
Radiobutton(root,text=cdict['Lamborghini'],compound=LEFT,width=330,variable=var,value='Lamborghini',image=img5,command=printSelection).pack(pady=5)
Radiobutton(root,text=cdict['Louts'],compound=LEFT,width=330,variable=var,value='Louts',image=img6,command=printSelection).pack(pady=5)
Radiobutton(root,text=cdict['Maserati'],compound=LEFT,width=330,variable=var,value='Maserati',image=img7,command=printSelection).pack(pady=5)
Radiobutton(root,text=cdict['Porsche'],compound=LEFT,width=330,variable=var,value='Porsche',image=img8,command=printSelection).pack(pady=5)
 
root.mainloop()