from socket import *
import json
import struct

client = socket(AF_INET,SOCK_STREAM)

client.connect(('127.0.0.1',10888))

while True:
    cmd = input('->').strip()   #发送命令
    if not cmd:continue
    #发送命令
    client.send(cmd.encode('gbk'))
    #解包（报头长度）
    header_len = struct.unpack('i',client.recv(4))[0]
    #接收报头
    header = client.recv(header_len).decode('gbk')

    print(header)

    header_dict = json.loads(header)
    #解析报头信息
    total_size = header_dict['total_size']
    #获取真实数据
    recv_size = 0
    recv_date = b''
    while recv_size<total_size:
        res = client.recv(1024)
        recv_date += res
        recv_size+=len(res)

    print(recv_date.decode('gbk'))

client.close()
