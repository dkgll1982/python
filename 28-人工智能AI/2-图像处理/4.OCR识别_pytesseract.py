#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
import pytesseract
from PIL import Image
 
# open image
image = Image.open(r'backup\3.jpg')
code = pytesseract.image_to_string(image, lang='chi_sim')

print(code)

#————————————————
#版权声明：本文为CSDN博主「冰海228」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/qianbin3200896/article/details/82892805