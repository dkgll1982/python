from tkinter import *
from time import time, localtime, strftime
 
clist = {"top_tee":'T型上',"tcross":'T型十字',"right_tee":'T型右',"left_tee":'T型左',"bottom_tee":'T型底',"X_cursor":'X型指针',
         "gumby":'gumby（卡通角色）',"center_ptr":'中指针',"middlebutton":'中间按钮',"exchange":'交换',"man":'人',"plus":'加',
         "cross":'十字',"crosshair":'十字线',"fleur":'十字花',"diamond_cross":'十字钻',"double_arrow":'双箭头',"top_right_corner":'右上角',
         "ur_angle":'右上角度',"bottom_right_corner":'右下角',"lr_angle":'右下角度',"right_ptr":'右指针',"rightbutton":'右按钮',
         "coffee_mug":'咖啡杯',"spraycan":'喷枪',"icon":'图标',"circle":'圆',"based_arrow_down":'基础向上箭头',"based_arrow_up":'基础向下箭头',
         "draft_large":'大拖拽',"sb_up_arrow":'宽上箭头',"sb_down_arrow":'宽下箭头',"sb_right_arrow":'宽右箭头',"sb_v_double_arrow":'宽垂直双箭头',
         "sb_left_arrow":'宽左箭头',"sb_h_double_arrow":'宽水平双箭头',"draft_small":'小拖拽',"top_left_arrow":'左上箭头',"ul_angle":'左上角度',
         "bottom_left_corner":'左下角',"ll_angle":'左下角度',"left_ptr":'左指针',"leftbutton":'左按钮',"sailboat":'帆船',"heart":'心型',
         "hand1":'手型1',"hand2":'手型2',"sizing":'改变大小',"dotbox":'方点',"box_spiral":'方螺旋',"star":'星星',"top_side":'最上边',
         "bottom_side":'最下边',"right_side":'最右边',"left_side":'最左边',"shuttle":'梭子型',"pirate":'海盗',"gobbler":'火鸡',"dot":'点',
         "target":'目标',"arrow":'箭头',"cross_reverse":'米字',"boat":'船',"bogosity":'虚假度',"spider":'蜘蛛',"clock":'表',"watch":'表',
         "draped_box":'褶皱盒子',"trek":'跋涉',"iron_cross":'铁十字',"pencil":'铅笔',"question_arrow":'问题箭头',"umbrella":'雨伞',"mouse":'鼠标'}


from tkinter import *  
# 引入字体模块
import tkinter.font as tkFont
import sys,os  
sys.path.append(os.path.dirname(os.path.dirname(__file__)) )   
from singlewindow  import *

root = Tk() 
window.show(root) 

row,col =0,0
for key,value in clist.items(): 
    lbl = Label(root,text=value,cursor=key,width=15);
    lbl.grid(row=row,column=col,padx=2,pady=1)
    if key.find("hea")>=0:
        lbl.config(bg='pink')
    elif key.find("hand")>=0:
        lbl.config(bg='lightgreen')
    elif key.find("spra")>=0:
        lbl.config(bg='yellow')
    elif key =="gobbler":
        lbl.config(bg='red')
    col+=1;
    if col%7 == 0 :
        col=0
        row+=1
    print('%s:%s'%(key,value)) 

root.mainloop()