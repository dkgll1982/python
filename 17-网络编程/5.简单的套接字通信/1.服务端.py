import socket

#1：买手机
phone = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)

#2：绑定手机卡
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)   #端口复用
phone.bind(('127.0.0.1',8080))

print('服务器已上线...')
#3：开机
phone.listen(5)

#4：等待别人打电话过来
conn,client_addr = phone.accept()
print(client_addr,'已连接...')

#5：收、发消息
while True:             #通信循环
    try:
        data = conn.recv(1024)          #Windows系统如果客户端掉线直接此处就报粗
        #if not data:break               #适用于Linux操作系统
        
        print('客户端发送的数据：',data.decode('utf-8'))

        msg = input('服务端回消息->').strip()
        if not msg:
            msg = input('服务端回消息->').strip()

        conn.send(msg.encode('utf-8'))

    except ConnectionResetError:        #连接异常,适用于windows操作系统
        print(client_addr,'已掉线或退出连接\r\n')
        break

#6：挂电话
conn.close()

#7：关机
phone.close()


