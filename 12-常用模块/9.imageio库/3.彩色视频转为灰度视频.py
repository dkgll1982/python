#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-04-06 12:16:11 
# @Remark: 人生苦短，我用python！
# 参考链接：https://blog.csdn.net/anymake_ren/article/details/78753707

# 将彩色视频转为灰度视频
import imageio
 
reader = imageio.get_reader('imageio:cockatoo.mp4')
fps = reader.get_meta_data()['fps']
 
writer = imageio.get_writer('~/cockatoo_gray.mp4', fps=fps)
 
for im in reader:
    writer.append_data(im[:, :, 1])
writer.close()

# 版权声明：本文为CSDN博主「Anymake」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/anymake_ren/article/details/78753707
