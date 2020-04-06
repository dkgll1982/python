#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: guojun
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2020-04-06 11:36:52
# @Remark: 人生苦短，我用python！
# imageio库png合成gif：https://blog.csdn.net/qq_30650153/article/details/78374647?depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-4&utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-4

import imageio
import glob
import re

def create_gif(image_list, gif_name):
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    # Save them as frames into a gif
    imageio.mimsave(gif_name, frames, 'GIF', duration=0.8)
    return

def find_all_png():
    png_filenames = glob.glob(r"/home/py_learning/createGIF/*.png")
    buf = []
    for png_file in png_filenames:
        buf.append(png_file)
    return buf

if __name__ == '__main__':
    buff = find_all_png()
    create_gif(buff, 'created_gif.gif')
