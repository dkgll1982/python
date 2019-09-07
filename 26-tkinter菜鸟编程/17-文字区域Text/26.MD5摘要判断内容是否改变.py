from tkinter import *
import hashlib

root = Tk()

text1 = Text(root,width=30,height=5)
text1.pack()

text1.insert(INSERT,'I Love FishC.com!')
contents = text1.get('1.0',END)

def getSig(contents):
     m=hashlib.md5(contents.encode())
     return m.digest()

sig=getSig(contents)

def check():
     contents = text1.get('1.0',END)
     if sig !=getSig(contents):
          print('警报,内容发生改变')
     else:
          print('风平浪静')

Button(root,text="检查",command=check).pack()

mainloop()