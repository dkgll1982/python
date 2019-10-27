import time,datetime 

try:
    #使用with语句，Python可以自动调用close()方法
    with open(r'C:\Users\dkgll\Desktop\python目录\note.txt','r') as f:
        print(f.read())
except:
    pass

#写文件
with open(r'C:\Users\dkgll\Desktop\python目录\note.txt','a+') as f:
    s = '写入的内容,%s\r\n'%time.strftime('%Y-%m-%d %H:%M:%S')
    f.write(s)

#照片
import PIL.Image as image
with image.open(r'images\jpg\20150616223657_PQmRF.jpeg') as pic:
    pic.show()