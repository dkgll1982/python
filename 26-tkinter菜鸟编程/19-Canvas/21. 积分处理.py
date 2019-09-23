from tkinter import *
import time
from random import *

cn = 0                      #碰撞次数
len = 0                     #增加长度

class Racket:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,200,15,fill=color)    #球拍对象
        self.canvas.move(self.id,270,400)                           #设置球拍位置  
        self.x = 0
        self.canvas.bind_all('<KeyPress-Right>',self.moveRight)     #右键按下
        self.canvas.bind_all('<KeyPress-Left>',self.moveLeft)       #左键按下
        self.canvas.bind_all('<KeyRelease-Right>',self.release)     #右键松开
        self.canvas.bind_all('<KeyRelease-Left>',self.release)      #左键松开
    def racketMove(self):                           #设计球拍移动
        self.canvas.move(self.id,self.x,0)          
        pos = self.canvas.coords(self.id)
        if pos[0]<= 0:                              #移动时是否碰到画布左边
            self.x = 0      
        elif pos[2] >= width:                       #移动时是否碰到画布右边
            self.x = 0
    def moveLeft(self,event):                       #球拍每次向左移动的单位数           
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:                             #移动时是否碰到画布左边
            self.x = 0      
        else:
            self.x = -3
    def moveRight(self,event):                      #球拍每次向右移动的单位数             
        pos = self.canvas.coords(self.id)
        if pos[2] >= width:                         #移动时是否碰到画布右边
            self.x = 0      
        else:
            self.x = 3
    def release(self,event):                        #球拍每次向右移动的单位数     
        self.x = 0       

class Ball:
    def __init__(self,canvas,color,width,height,racket):
        self.canvas = canvas
        self.racket = racket
        self.id = canvas.create_oval(0,0,20,20,fill=color)
        self.canvas.move(self.id,width/2,height/2)  #设置球最初位置
        startPos = [-4,-3,-2,-1,1,2,3,4]            #球最初x轴位移的随机数
        shuffle(startPos)                           #打乱排列：shuffle() 方法将序列的所有元素随机排序。
        self.x = startPos[0]
        self.y = step
        self.noTouchBottom = True                   #未接触到画布底端
    def hitRacket(self,ballpos):
        racketPos = self.canvas.coords(self.racket.id)
        if ballpos[2] >= racketPos[0] and ballpos[0] <= racketPos[2]:
            if ballpos[3] >= racketPos[1] and ballpos[3] <= racketPos[3]:
                return True
        return False
    def ballMove(self):
        global cn
        self.canvas.move(self.id,self.x,self.y)     #step是正值表示往下移动
        ballPos = self.canvas.coords(self.id)       #获取球的位置坐标信息（左上角x,左上角y,右下角x,右下角y）
        if ballPos[0]<=0:                           #侦测球是否超过画布左方
            self.x = step
        if ballPos[1]<=0:                           #侦测球是否超过画布上方
            self.y = step
        if ballPos[2]>=width:                       #侦测球是否超过画布右方
            self.x = -step 
        if ballPos[3]>=height:                      #侦测球是否超过画布下方
            self.y = -step
        if self.hitRacket(ballPos) == True:         #侦测球是否撞到球拍
            cn=cn+1 
            print('积分：%d'%cn)
            self.y= - step 
        if ballPos[3] >= height:                    #如果球接触到画布底端
            self.noTouchBottom = False

width,height,step,speed = 640,480,3,0.03    

root = Tk()

#window.wm_attributes('-topmost', 1)  # 锁定窗口置顶
#window.wm_attributes('-topmost', 0)  # 释放窗口置顶
root.wm_attributes('-topmost',1)      #确保游戏在屏幕最上层

canvas = Canvas(root,width=width,height=height)

canvas.pack() 
# tk.update()让tkinter为我们游戏中的动画做好初始化
# 如果没有这一行，我们看到的东西会和期望的不一样
root.update() 
root.resizable(False,False)

# 绘制文字
lbltext = StringVar()             
lbltext.set('积分：0')   

racket = Racket(canvas,'purple')                #定义紫色球拍   
ball = Ball(canvas,'yellow',width,height,racket)#定义球对象

while ball.noTouchBottom:
    try:
        ball.ballMove()
    except:
        print('单击关闭按钮终止程序执行')
        break
    racket.racketMove()
    root.update()
    time.sleep(speed)
    
     