#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-13 11:39:47 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-13 11:39:47 
# @Software: vscode 
# 参考链接：
# https://blog.csdn.net/cungudafa/article/details/85871871
# https://blog.csdn.net/m0_38106923/article/details/100603516

'''
==============================
test1：生成二维码及查看
==============================
'''
from PIL import Image
import qrcode

qr = qrcode.QRCode(
    version=5, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=8, border=4)
qr.add_data('https://user.qzone.qq.com/350606539/main')
qr.make(fit=True)

img = qr.make_image()
img = img.convert("RGBA")

icon = Image.open(r"images\jpg\20160704101150_fUYEw.jpeg")  # 这里是二维码中心的图片

img_w, img_h = img.size
factor = 4
size_w = int(img_w / factor)
size_h = int(img_h / factor)

icon_w, icon_h = icon.size
if icon_w > size_w:
    icon_w = size_w
if icon_h > size_h:
    icon_h = size_h
icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

w = int((img_w - icon_w) / 2)
h = int((img_h - icon_h) / 2)
icon = icon.convert("RGBA")
img.paste(icon, (w, h), icon)
img.show()   # 显示图片,可以通过save保存
