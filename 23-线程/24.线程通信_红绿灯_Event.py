#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-22 21:23:49 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-22 21:23:49 
# @Software: vscode 
# 参考链接：https://blog.csdn.net/weixin_42205776/article/details/89740015

import time, threading
event = threading.Event()

# 交通灯
def lighter():
    count = 0
    while True:
        if count < 5:       # 绿灯
            event.set()     #设置标志位，True，不再阻塞
            print("绿灯亮")
        elif count > 10:
            count =0        # 清零重新计数
        else:               # 红灯
            event.clear()   # 清空标志位，False，阻塞
            print("红灯亮")

        time.sleep(1)
        count += 1

# 车辆
def car(name):
    while True:
        if event.is_set():  # 绿灯亮
            print("[%s]绿灯行..." % name)
            time.sleep(1)
        else:
            print("[%s]红灯停!!!" % name)
            event.wait()    # 等待标志位设定
            print("绿灯出发")

# 启动交通灯
t_lighter = threading.Thread(target=lighter)
t_lighter.start()

# 放入车辆
t_car1 = threading.Thread(target=car, args=("奥迪车",))
t_car2 = threading.Thread(target=car, args=("大众车",))
t_car1.start()
t_car2.start()