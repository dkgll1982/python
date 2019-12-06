from socket import *
import struct
import json
import struct
import os
import time
 
server = socket(AF_INET,SOCK_STREAM)

server.bind(('127.0.0.1',9999))
server.listen(5)
print('服务器已上线...')

while True:         #链接循环
    conn,clientaddr = server.accept()       #建立链接
    print('客户端',clientaddr,'已上线',sep='')
    
    while True:
        try:
            data = conn.recv(8096).decode('gbk')          #收到命令
            cmd = data[:3].lower().strip()                #命令名称
            path = data[4:].strip()                       #文件名称，含全路径
            file_name = path.split("\\")[-1]              #文件名称(不含全路径)

            if (cmd=='get'):
                print('客户端',clientaddr,'开始下载文件：',file_name,sep='')

                #先发送报头，表明文件信息
                header_dict ={
                    'file_name': path, 
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
                conn.send(header_len)

                #2：把报头发送给客户端
                conn.send(header_bytes)

                #3：发送文件
                with open(path,'rb') as f:
                    for line in f:
                        conn.send(line)

            elif (cmd=='put'):
                start = time.time()
                print('客户端',clientaddr,'开始上传文件：',file_name,sep='')
                #1：接收报头长度
                header_len = struct.unpack('i',conn.recv(4))[0]
                #2：接收包头
                header = conn.recv(header_len)
                #解析包头信息
                header_str = header.decode('gbk')
                header_json = json.loads(header_str)
                file_size = header_json['file_size']
                full_path = r"C:\Users\dkgll\Desktop\python目录\server\\"+file_name
                #3：接收文件
                with open(full_path,'wb') as f:
                    recv_size = 0
                    while recv_size<file_size:
                        s = conn.recv(1024)
                        f.write(s)
                        recv_size+=len(s)
                        print('文件的总大小：%d,已下载的打开：%d'%(file_size,recv_size))
                end = time.time()
                shi = end - start
                print("下载完成！！总耗时%s秒！" % round(shi,2))

        except ConnectionError:
            print('客户端已下线或失去连接！')
            break
    conn.close()
server.close()
