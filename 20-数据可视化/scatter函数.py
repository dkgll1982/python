#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-04 15:06:31 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-04 15:06:31 
# @Software: vscode 

import matplotlib.pyplot as plt
import numpy as np
plt.figure()
# 定义从-pi到pi之间的数据，平均取64个数据点
x_data = np.linspace(-np.pi, np.pi, 64, endpoint=True)  # ①
# 将整个figure分成两行两列，第三个参数表示该图形放在第1个网格
# 沿着正弦曲线绘制散点图
plt.scatter(x_data, np.sin(x_data), c='purple', # 设置点的颜色
    s=50, # 设置点半径
    alpha = 0.5, # 设置透明度
    marker='p', # 设置使用五边形标记
    linewidths=1, # 设置边框的线宽
    edgecolors=['green', 'yellow']) # 设置边框的颜色
# 绘制第二个散点图（只包含一个起点），突出起点
plt.scatter(x_data[0], np.sin(x_data)[0], c='red', # 设置点的颜色
    s=150, # 设置点半径
    alpha = 1) # 设置透明度
# 绘制第三个散点图（只包含一个结束点），突出结束点
plt.scatter(x_data[63], np.sin(x_data)[63], c='black', # 设置点的颜色
    s=150, # 设置点半径
    alpha = 1) # 设置透明度
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['left'].set_position(('data', 0))
plt.title('正弦曲线的散点图')
plt.show()