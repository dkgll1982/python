#主要用来显示短消息，功能与Label类似，但是使用更灵活，可自动分行，对于一些不想再做进一步编辑的短文，可以使用Message显示
from tkinter import *

root = Tk()

root.title('短消息组件')

info ='''
我兴冲冲地来了
沐浴着清风与骄阳
带着憧憬和向往
用力的伸展着双臂
想要将你揽入胸膛
深深地、深深地
感受着你温暖的气息 
一切未知的你的神秘
总是让我惊喜、赞叹 ！
就要离开了...........
'''

msg = Message(root,bg='yellow',text=info,font='times 12 italic',cursor='star',relief='raised')
msg.pack(padx=10,pady=10)

root.mainloop()