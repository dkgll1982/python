from tkinter import *
import time
from random import *

class Ball:
    def __init__(self,canvas,color,width,height):
        self.canvas = canvas
        self.id = canvas.create_oval(0,0,20,20,fill=color)
        self.canvas.move(self.id,width/2,height/2)      #设置球最初位置
    def ballMove(self):
        self.canvas.move(self.id,0,step)                #step是正值表示往下移动
        ballPos = self.canvas.coords(self.id)           #获取球的位置坐标信息（左上角、右下角）
        print('球的坐标：',ballPos)

width,height,step,speed = 640,480,3,0.03    

root = Tk()

#window.wm_attributes('-topmost', 1)                    # 锁定窗口置顶
#window.wm_attributes('-topmost', 0)                    # 释放窗口置顶
root.wm_attributes('-topmost',1)                        #确保游戏在屏幕最上层

canvas = Canvas(root,width=width,height=height)

canvas.pack() 
# tk.update()让tkinter为我们游戏中的动画做好初始化
# 如果没有这一行，我们看到的东西会和期望的不一样
root.update()

ball = Ball(canvas,'yellow',width,height)               #定义球对象

while True:
    ball.ballMove()
    root.update()
    time.sleep(speed)
    
    