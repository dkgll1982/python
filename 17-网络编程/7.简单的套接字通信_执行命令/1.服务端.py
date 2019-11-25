#参考讲解：https://edu.csdn.net/course/play/24458/296237

import socket 
import subprocess

server = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
 
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)   #端口复用
server.bind(('127.0.0.1',8080))
 
server.listen(5)
print('服务器已上线...')

while True:                     #客户端链接循环 
    conn,client_addr = server.accept()
    print(client_addr,'已连接...')
 
    while True:                 #通信循环 
        try:
            #1.收命令
            cmd = conn.recv(10240)        
            #if not cmd:break               #适用于Linux操作系统
            
            #2.执行命令，拿到结果
            obj = subprocess.Popen(cmd.decode('gbk'),shell=True,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
            
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()

            #3.把命令的结果返回客户端
            conn.send(stdout+stderr)
            
        except ConnectionResetError:        #连接异常,适用于windows操作系统
            print(client_addr,'已掉线或退出连接\r\n')
            break
 
    conn.close()
 
server.close()


