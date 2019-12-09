import socket
import struct
import json
import time
import math

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1',8081))

while True:
    # 1.发命令
    cmd = input('->:').strip()  # 与服务端约定获取文件命令：get filename
    if not cmd:
        continue
    phone.send(cmd.replace(r'/', '\\').encode('gbk'))

    # 2.以写的方式打开一个文件，接受服务端发来的文件内容写入客户端文件
    # 第一步：先收报头长度
    obj = phone.recv(4)
    header_size = struct.unpack('i', obj)[0]

    # 第二步：再收报头
    header_bytes = phone.recv(header_size)

    # 第三步：从从报头中解析出对真实数据的描述信息
    header_str = header_bytes.decode('gbk')
    print(header_str)

    header_dict = json.loads(header_str)

    total_size = header_dict['file_size']
    file_name = header_dict['file_name'].split("\\")[-1]
    print(file_name)
    file_path = r"backup\\"+file_name
    print(file_path)

    start = time.time()
    # 第四步：接受真实的数据
    with open(file_path, 'wb') as f:        #以二进制方式读写
        recv_size = 0
        while recv_size < total_size:
            line = phone.recv(10240)
            f.write(line)
            recv_size += len(line)
            print('文件的总大小：%d,已下载的打开：%d'%(total_size,recv_size))

    end = time.time()
    shi = end - start
    print("下载完成！！总耗时%s秒！" % round(shi,2))
phone.close()
