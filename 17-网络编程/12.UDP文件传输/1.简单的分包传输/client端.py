#!python
#文件名: demo_client.py

'''
     规定:
     客户端向服务端请求文件(音频或者视屏等完整性要求不高的)
     先打个招呼,要文件了(实际可以为要哪个文件)
     然后开始接受文件,不停的接受即可(这里我每接受一次就回复一句ok))
'''

import socket
import struct

BUF_SIZE = 1024
server_addr = ('127.0.0.1',8888)
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

count=0;
#不停的发送数据 ,没发一次尝试接受一次数据并打印
f=open(r'C:\Users\dkgll\Desktop\python目录\zipfile.zip','wb')
while True:
     if count==0:
          data='Yes,I\'m Ready'
          client.sendto(data.encode('utf-8'),server_addr)
     data,addr = client.recvfrom(BUF_SIZE)
     if str(data)!="b'end'":
          f.write(data)
          print(data)#此处打印注意被刷屏,仅测试用
     else:
          break;#接受到结束通知,结束循环,打印循环次数,然后去指定路径查找file_copy.jar尝试运行
     client.sendto('ok'.encode('utf-8'),addr)#向服务端发送成功通知
     count+=1;

print('循环了'+str(count))
f.close()
client.close()
