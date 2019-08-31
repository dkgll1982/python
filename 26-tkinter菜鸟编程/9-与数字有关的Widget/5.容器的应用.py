from tkinter import *

#R,G,B三颜色值转化为十六进制颜色码
#print('#%02x%02x%02x'%(255,182,193))
#print('#%02x%02x%02x'%(218,112,214))

def bgUpdate(source):
    '''更改窗口背景颜色'''
    red = rSlider.get()
    green = gSlider.get()
    blue = bSlider.get()
    print('R=%d,G=%d,B=%d' %(red,green,blue))
    myColor ='#%02x%02x%02x'  %(red,green,blue)    #将色彩转为十六进制字符串
    root.config(bg=myColor)

root =Tk()
root.title('色彩调节器')
root.geometry('500x300+200+200')

frm =Frame(root)
frm.pack()

rSlider = Scale(frm,from_=0,to=255,command=bgUpdate)
gSlider = Scale(frm,from_=0,to=255,command=bgUpdate)
bSlider = Scale(frm,from_=0,to=255,command=bgUpdate)

gSlider.set(125)
rSlider.grid(row=0,column=0)
gSlider.grid(row=0,column=1)
bSlider.grid(row=0,column=3)

root.mainloop()
