from socket import *
import struct
import json
import time
import os

client = socket(AF_INET,SOCK_STREAM)

client.connect(('127.0.0.1',9999))

while True:
    inp = input('->').strip()                   #发送命令
    path = inp[4:].strip()                      #文件路径
    file_name = path.split("\\")[-1]            #文件名称(不含全路径)
    if not inp:
        continue

    #发送命令到服务器
    client.send(inp.encode('gbk'))

    cmd = inp[:3].lower().strip()               #命令名称
    if (cmd == 'get'):
        start = time.time()
        print('开始从服务器下载文件：', file_name, sep='')

        #1：接收报头长度
        header_len = struct.unpack('i',client.recv(4))[0]
        #2：接收报头
        header = client.recv(header_len)
        #解析报头信息
        header_str = header.decode('gbk')
        header_json = json.loads(header_str)
        file_size = header_json['file_size']
        full_path = r"backup\\"+file_name
        #3：接收文件
        with open(full_path,'wb') as f:
            recv_size = 0
            while recv_size<file_size:
                s = client.recv(1024)
                f.write(s)
                recv_size+=len(s)
                print('文件的总大小：%d,已下载的打开：%d'%(file_size,recv_size))
        end = time.time()
        shi = end - start
        print("下载完成！！总耗时%s秒！" % round(shi,2))

    if (cmd == 'put'):
        print('开始上传文件到服务器：', file_name, sep='')
        #先发送报头，表明文件信息
        header_dict ={
            'file_name': path,                          # 文件名，含全路径
            'author': 'suixin',
            'comapany': '航天神舟智慧系统技术有限公司',
            'md5': '12345',
            'file_size': os.path.getsize(path)          
        }

        header_str = json.dumps(header_dict,ensure_ascii=False)
        header_bytes = header_str.encode('gbk')

        #此处解决粘包问题：分三步-1：发送报头长度，2：发送报头，3：发送真实数据
        #1：发送报头长度
        header_len = struct.pack('i',len(header_bytes))
        client.send(header_len)

        #2：把报头发送给客户端
        client.send(header_bytes)

        #3：发送文件
        with open(path,'rb') as f:
            for line in f:
                client.send(line)
client.close()