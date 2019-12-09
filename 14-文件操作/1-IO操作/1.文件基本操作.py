import time,datetime 

try:
    #使用with语句，Python可以自动调用close()方法
    with open(r'backup\note.txt','r') as f:
        print(f.read())
except:
    pass

#写文件
with open(r'backup\note.txt','a+') as f:
    s = '写入的内容,%s\r\n'%time.strftime('%Y-%m-%d %H:%M:%S')
    f.write(s)

#照片
import PIL.Image as image
with image.open(r'images\jpg\20150616223657_PQmRF.jpeg') as pic:
    pic.show()

# python 读写文件中 w与wt ; r与rt 的区别

# w,r,wt,rt都是python里面文件操作的模式。
# w是写模式，r是读模式。
# t是windows平台特有的所谓text mode(文本模式）,区别在于会自动识别windows平台的换行符。
# 类Unix平台的换行符是\n，而windows平台用的是\r\n两个ASCII字符来表示换行，python内部采用的是\n来表示换行符。
# rt模式下，python在读取文本时会自动把\r\n转换成\n.
# wt模式下，Python写文件时会用\r\n来表示换行。   