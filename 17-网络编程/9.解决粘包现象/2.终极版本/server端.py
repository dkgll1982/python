import socket
import subprocess
import struct
import json

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.bind(('127.0.0.1',8081))
phone.listen(5)

print('服务器已上线...')

while True:                 #链接循环
    conn,clientaddress = phone.accept()
    print(clientaddress)

    while True:             #通信循环
        try:
            #1：收命令
            cmd = conn.recv(8096)
           
            #if not cmd:break               #适用于Linux操作系统
            
            #2：执行命令，拿到结果
            obj = subprocess.Popen(cmd.decode('gbk'),shell=True,
                                    stdout = subprocess.PIPE,
                                    stderr = subprocess.PIPE)
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()

            #3：把命令的结果返回给客户端
            #第一步:制作固定长度的报头
            header_dict = {
                'fileName':'a.txt',
                'author':'suixin',
                'comapany':'航天神舟智慧系统技术有限公司',
                'total_size':len(stdout) + len(stderr)
            }
            
            #json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False
            header_str = json.dumps(header_dict,ensure_ascii=False)
            header_bytes = header_str.encode('gbk')

            #第二步:发送报头的长度
            header_size = struct.pack('i',len(header_bytes))
            conn.send(header_size)

            #第二步:把报头发送给客户端
            conn.send(header_bytes)

            #第三步:再发送真实的数据
            conn.send(stdout)
            conn.send(stderr)
        except ConnectionResetError:        #适用于windows操作系统
            print(clientaddress,'已掉线或退出连接\r\n')
            break
    conn.close()

phone.close()

