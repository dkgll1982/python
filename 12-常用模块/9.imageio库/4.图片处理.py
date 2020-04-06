#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: guojun
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2020-04-06 12:25:59
# @Remark: 人生苦短，我用python！
# 参考链接：https://www.cnblogs.com/devilmaycry812839668/p/9344581.html

import imageio
import numpy

img = imageio.imread(r"images\lufei.PNG")
 
img1 = img.copy()
img2 = img.copy()
img3 = img.copy()
img4 = img.copy() 
img5 = img.copy() 
img6 = img.copy() 
img7 = img.copy()  

#读取一个通道
img1[:, :, 0] = 0
img1[:, :, 1] = 0

img2[:, :, 0] = 0
img2[:, :, 2] = 0

img3[:, :, 1] = 0
img3[:, :, 2] = 0

#读取俩个通道
img4[:, :, 0] = 0 

img5[:, :, 1] = 0 

img6[:, :, 2] = 0 

#RGB通道都不读取，图片全黑
img7[:, :, 0] = 0 
img7[:, :, 1] = 0 
img7[:, :, 2] = 0 

imageio.imwrite(r"images\lufei1.png", img1)
imageio.imwrite(r"images\lufei2.png", img2)
imageio.imwrite(r"images\lufei3.png", img3)
imageio.imwrite(r"images\lufei4.png", img4)
imageio.imwrite(r"images\lufei5.png", img5) 
imageio.imwrite(r"images\lufei6.png", img6)
imageio.imwrite(r"images\lufei7.png", img7)


 