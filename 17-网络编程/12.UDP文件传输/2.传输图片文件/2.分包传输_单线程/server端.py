# -*- coding: utf-8 -*-
# python通过udp传输图片：https://blog.csdn.net/qq_36852276/article/details/90761122

import socket
import cv2
import numpy as np
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口:
s.bind(('127.0.0.1', 9999))

print('Bind UDP on 9999...')

while True:
    # 接收文件头，文件头的长度由calcsize函数确定，注意这里recvfrom是接收UDP消息，recv是接收TCP消息
    fhead_size = struct.calcsize('l')
    buf,addr = s.recvfrom(fhead_size)
    print(addr)
    if buf:
    #这里结果是一个元组，所以把值取出来
        data_size = struct.unpack('l',buf)[0]
	#接收图片码流长度的码流
    recvd_size = 0
    data_total = b''

    #分包取数据
    while not recvd_size == data_size:
        if data_size -recvd_size >10240:
            data,addr = s.recvfrom(10240)
            recvd_size += len(data)
        else:
            data,addr = s.recvfrom(10240)
            recvd_size = data_size
        data_total += data

    print('Received')
#    reply = 'Hello, %s!' % data.decode('utf-8')
#    s.sendto(reply.encode('utf-8'), addr)
	#把接到的码流解码成numpy数组，显示图像
    nparr = np.fromstring(data_total, np.uint8)
    img_decode = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imshow('result',img_decode)
    cv2.waitKey()
    #应答
    reply = "get message!!!"
    s.sendto(reply.encode('gbk'), addr)
    cv2.destroyAllWindows()

