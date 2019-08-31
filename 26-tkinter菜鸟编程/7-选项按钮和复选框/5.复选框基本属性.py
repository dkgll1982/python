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

def printSelection(): 
  #label.config(text='选择中意的汽车品牌:'+cdict[var.get()]) 
  pass

img1,img2,img3,img4,img5,img6,img7,img8 = getlogo('Alfa Romeo'),getlogo('Aston Martin'),getlogo('Bugatti'),getlogo('Ferrari'),getlogo('Lamborghini'),getlogo('Louts'),getlogo('Maserati'),getlogo('Porsche')
 
label = Label(root,text='选择汽车:',bg = 'lightyellow',width=50)
label.grid(row=0,columnspan=2,pady=5) 

Checkbutton(root,text=cdict['Alfa Romeo'],compound=LEFT,width=330 ,image=img1,command=printSelection,anchor='w').grid(row=1,pady=5,padx=10)
Checkbutton(root,text=cdict['Aston Martin'],compound=LEFT,width=330 ,image=img2,command=printSelection,anchor='w').grid(row=2,pady=5,padx=10)
Checkbutton(root,text=cdict['Bugatti'],compound=LEFT,width=330 ,image=img3,command=printSelection,anchor='w').grid(row=3,pady=5,padx=10)
Checkbutton(root,text=cdict['Ferrari'],compound=LEFT,width=330 ,image=img4,command=printSelection,anchor='w').grid(row=4,pady=5,padx=10)
Checkbutton(root,text=cdict['Lamborghini'],compound=LEFT,width=330 ,image=img5,command=printSelection,anchor='w').grid(row=5,pady=5,padx=10)
Checkbutton(root,text=cdict['Louts'],compound=LEFT,width=330 ,image=img6,command=printSelection,anchor='w').grid(row=6,pady=5,padx=10)
Checkbutton(root,text=cdict['Maserati'],compound=LEFT,width=330 ,image=img7,command=printSelection,anchor='w').grid(row=7,pady=5,padx=10)
Checkbutton(root,text=cdict['Porsche'],compound=LEFT,width=330,image=img8,command=printSelection,anchor='w').grid(row=8,pady=5,padx=10)
 
root.mainloop()