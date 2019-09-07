from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title('插入图像')
root.geometry('600x600+400+50')

img = Image.open(r'images\jpg\timg7.jpg')
myPhoto = ImageTk.PhotoImage(img)

text = Text()
text.image_create(END,image=myPhoto)
text.insert(END,'\n')
text.insert(END,'二次元美少女')

b1 = Button(text,text='文中钮')
text.window_create(INSERT,window=b1)

l1 = Label(text,text='文中标签')
text.window_create(INSERT,window=l1)

ent = Entry(text,width=25,bg='lightgreen',fg='red')
text.window_create(INSERT,window=ent)

text.pack(fill=BOTH,expand=True)

root.mainloop()