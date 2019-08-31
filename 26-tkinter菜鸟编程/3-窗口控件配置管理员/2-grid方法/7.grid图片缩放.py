import threading
from tkinter import *  
# 引入字体模块
import tkinter.font as tkFont
import sys,os  
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))   
from singlewindow  import *
from PIL import Image,ImageTk

root = Tk()   
window.show(root)    

root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
#对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例   
 
def resize( w_box, h_box, pil_image): #参数是：要适应的窗口宽、高、Image.open后的图片
  w, h = pil_image.size #获取图像的原始大小   
  f1 = 1.0*w_box/w 
  f2 = 1.0*h_box/h    
  factor = min([f1, f2])   
  width = int(w*factor)    
  height = int(h*factor)    
  return pil_image.resize((width, height), Image.ANTIALIAS)     
 
#resize函数使用过程：  
#==================================================================
w_box1 = 300    #期望图像显示的大小（窗口大小）
h_box1 = 220    
 
pil_image1 = Image.open(r'images\jpg\07c5c367642e9bc66a3fbadabeb21067434f51512bbee-IxAozg_fw658.jpg')    #以一个PIL图像对象打开  【调整待转图片格式】   
pil_image_resized1 = resize( w_box1, h_box1, pil_image1)    #缩放图像让它保持比例，同时限制在一个矩形框范围内  【调用函数，返回整改后的图片】   
tk_image1 = ImageTk.PhotoImage(pil_image_resized1)    # 把PIL图像对象转变为Tkinter的PhotoImage对象  【转换格式，方便在窗口展示】  
#====================================================================   
  
#==================================================================
w_box2 = 400    #期望图像显示的大小（窗口大小）
h_box2 = 240    
 
pil_image2 = Image.open(r'images\miaomiao.png')    #以一个PIL图像对象打开  【调整待转图片格式】   
pil_image_resized2 = resize( w_box2, h_box2, pil_image2)    #缩放图像让它保持比例，同时限制在一个矩形框范围内  【调用函数，返回整改后的图片】   
tk_image2 = ImageTk.PhotoImage(pil_image_resized2)    # 把PIL图像对象转变为Tkinter的PhotoImage对象  【转换格式，方便在窗口展示】  
#====================================================================    

lbl1 = Label(root,image=tk_image1)
lbl1.grid(row=0,column=0)

lbl2 = Label(root,image=tk_image2)
lbl2.grid(row=0,column=1)

root.mainloop()