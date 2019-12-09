from socket import *
import subprocess
import time
import json
import struct

server = socket(AF_INET,SOCK_STREAM)

server.bind(('127.0.0.1',10888))

server.listen(5)

print('服务器已上线...')

while True:             #链接循环
    conn,client = server.accept()                #建立链接
    print('客户端',client,'已连接服务器...',sep='')

    while True:         #通讯循环
        cmd = conn.recv(8096).decode('gbk')    #收到命令

        #执行命令
        obj = subprocess.Popen(cmd,
                            shell=True,
                            stderr=subprocess.PIPE,
                            stdout=subprocess.PIPE)

        #获取执行结果
        stdout = obj.stdout.read()
        #获取执行错误
        stderr = obj.stderr.read()

        #报头
        header_dic ={
            'author':'suixin',
            'company':"航天神舟智慧系统技术有限公司",
            'MD5':'12345',
            'total_size':len(stdout)+len(stderr),
        }

        header_str = json.dumps(header_dic,ensure_ascii=False)
        header_bytes =header_str.encode('gbk')
        header_len = len(header_bytes)

        #发送报头长度
        conn.send(struct.pack('i',header_len))
        #发送报头
        conn.send(header_bytes)
        #发送真实数据
        conn.send(stderr)
        conn.send(stdout)
    conn.close()
server.close()



