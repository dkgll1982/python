from tkinter import  *
from tkinter.messagebox import *
import tkinter.constants, tkinter.filedialog
from PIL import Image, ImageTk
import os
 
def read_image():
    #choose a image
    imagefile = tkinter.filedialog.askopenfilename(parent=root, initialdir="./images/jpg", filetypes=[('二次元美少女', '.jpg')],title='我的后宫')
 
    # use PIL.Image to open a image
    image = Image.open(imagefile)
 
    # resize image with high-quality
    x_s = 800  # define standard width
    y_s = 600  # define standard height
    image = image.resize((x_s, y_s), Image.ANTIALIAS)
 
 
    # convert the form of image to ImageTk.PhotoImage
    image = ImageTk.PhotoImage(image)
 
    # creat a panel to draw image
    panel1.configure(image=image)
    panel1.image = image
    panel1.pack(side='top')
 
    # creat a label to display the image's name
    imagefile = imagefile.encode('gbk')
    label1.configure(text=('Image : {}'.format(os.path.split(imagefile)[1].decode('gbk').encode('utf8'))),
                     font=('Arial', 20))
    label1.pack(side='bottom')
 
 
 
if __name__ == '__main__':
    # create display
    root = Tk()
    root.title('Show a image')
    # resize display
    root.geometry("1024x760+100+10")    #is x ,not *
    frm = Frame(root)
    Button(frm, text="Load Image ", font=('Arial', 18) , command = read_image).pack()     #command = lambda : read_image(value)
    panel1 = Label(frm,image=None)
    label1 = Label(frm,text='')
    frm.pack()
    # run display
    root.mainloop() 