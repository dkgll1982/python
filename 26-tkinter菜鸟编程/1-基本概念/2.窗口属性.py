
from tkinter import * 
import sys,os 

# __file__ 为当前文件
curr_dir = os.path.dirname(__file__)  #返回当前文件所在的目录  
#获得curr_dir所在的目录,即curr_dir的父级目录   
parent_dir = os.path.dirname(curr_dir) 
sys.path.append(parent_dir)   

#sys.path.append(os.path.dirname(os.path.dirname(__file__)))   
from singlewindow  import *

root = Tk()
window.show(root)
root.mainloop()