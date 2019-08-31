from tkinter import * 
import sys,os  
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from singlewindow  import * 

root = Tk()
root.geometry('500x420+400+100')

#汽车字典
clist = [
    {"code":'Alfa Romeo',"name":'阿尔法罗密欧'},
    {"code":'Aston Martin',"name":'阿斯顿马丁'},
    {"code":'Bugatti',"name":'布加迪'},
    {"code":'Ferrari',"name":'法拉利'},
    {"code":'Lamborghini',"name":'兰博基尼'},
    {"code":'Louts',"name":'路特斯'},
    {"code":'Maserati',"name":'玛莎拉蒂'},
    {"code":'Porsche',"name":'保时捷'}
]
 
def printinfo():
    selection = ''
    for i in checkboxes:
        if checkboxes[i].get() == True:
            selection = selection + clist[i]["name"]+','
    labFrame.config(text='选择汽车:'+selection[:-1])

#label = Label(root,text='选择汽车:',bg = 'lightyellow',width=50)
#label.grid(row=0,columnspan=2,pady=5) 
 
labFrame = LabelFrame(root,text='选择汽车')

checkboxes = {}
for i in range(len(clist)):
    checkboxes[i] = BooleanVar()
    Checkbutton(labFrame,text = clist[i]["name"],variable=checkboxes[i],anchor='w',width=40).grid(row=i) 

labFrame.grid(row=0 ,pady=5,padx=100) 

btn = Button(root,text="确定",width=10,command=printinfo) 
btn.grid(row=1)
root.mainloop()