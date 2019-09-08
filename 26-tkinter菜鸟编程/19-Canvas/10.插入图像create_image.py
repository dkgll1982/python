from tkinter import *
from PIL import Image,ImageTk

root = Tk()
img = Image.open(r'images\jpg\07c5c367642e9bc66a3fbadabeb21067434f51512bbee-IxAozg_fw658.jpg')
rushMore = ImageTk.PhotoImage(img)

canvas= Canvas(root,width=img.size[0]+40,height=img.size[1]+40)
canvas.create_image(20,15,anchor=NW,image=rushMore)

canvas.pack(fill=BOTH,expand=True)

root.mainloop()