# -*- coding: utf-8 -*-
# python通过udp传输图片：https://blog.csdn.net/qq_36852276/article/details/90761122

import socket
import cv2
import numpy as np

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口:
s.bind(('127.0.0.1', 9999))

print('Bind UDP on 9999...')

while True:
    # 接收数据:
    data, addr = s.recvfrom(40000000)
    print('Received from %s:%s.' % addr)
    #解码
    nparr = np.fromstring(data, np.uint8)
    #解码成图片numpy
    img_decode = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imshow('result',img_decode)
    cv2.waitKey()
    reply = "get message!!!"
    s.sendto(reply.encode('gbk'), addr)
    cv2.destroyAllWindows()
