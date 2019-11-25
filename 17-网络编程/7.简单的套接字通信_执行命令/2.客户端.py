import socket
 
client = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
 
client.connect(('127.0.0.1',8080))
 
while True:
    #发送命令(lsntctl status、dir、ping 127.0.0.1)
    cmd = input('客户端发命令->').strip()
    if not cmd:
        continue
    client.send(cmd.encode('gbk'))  

    #返回执行命令的结果并打印
    data = client.recv(10240)
    print("服务端执行命令结果:",data.decode('gbk'))
 
client.close()