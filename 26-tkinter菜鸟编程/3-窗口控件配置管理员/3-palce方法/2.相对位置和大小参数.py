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
w_box1 = root.winfo_width()*0.8    #期望图像显示的大小（窗口大小）
h_box1 = root.winfo_height()*0.8     
 
pil_image1 = Image.open(r'images\jpg\07c5c367642e9bc66a3fbadabeb21067434f51512bbee-IxAozg_fw658.jpg')    #以一个PIL图像对象打开  【调整待转图片格式】   
pil_image_resized1 = resize( w_box1, h_box1, pil_image1)    #缩放图像让它保持比例，同时限制在一个矩形框范围内  【调用函数，返回整改后的图片】   
tk_image1 = ImageTk.PhotoImage(pil_image_resized1)    # 把PIL图像对象转变为Tkinter的PhotoImage对象  【转换格式，方便在窗口展示】  
#====================================================================   
    
lbl1 = Label(root,image=tk_image1)
lbl1.place(relx=0.1,rely=0.1, relwidth=0.8, relheight=0.8)  

def onResize(e):
    #    x = (root.winfo_screenwidth()-w)/2
    #    y = (root.winfo_screenheight()-h)/2    
    pil_image_resized1 = resize( e.width*0.8, e.height*0.8, pil_image1)    #缩放图像让它保持比例，同时限制在一个矩形框范围内  【调用函数，返回整改后的图片】   
    tk_image1 = ImageTk.PhotoImage(pil_image_resized1)    # 把PIL图像对象转变为Tkinter的PhotoImage对象  【转换格式，方便在窗口展示】  
 
    lbl1.configure(image = tk_image1)
    lbl1.image=tk_image1                      #keep a reference

#改变组件的形状（在某些平台上表示的是位置）。新形状以event对象中width 和 height属性的形式传递给callback。
root.bind("<Configure>",onResize)

root.mainloop()