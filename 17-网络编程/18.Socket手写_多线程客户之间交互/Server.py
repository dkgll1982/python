from socket import *
import time
import threading

#实例化对象
serversock = socket(family=AF_INET,type=SOCK_STREAM)
serversock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)   #端口复用

ip =''
port = 15245
HOST = (ip,port)

#客户端用户列表
users={}

#绑定IP、端口
serversock.bind(HOST)

#监听客户端连接
serversock.listen(15)
print('服务器启动成功,等待客户端连接...') 

def run(tcpclisock,clientAddress):
    usersName = tcpclisock.recv(4096)
    users[usersName.decode("utf-8")] = tcpclisock 
    print(users)

    while 1:  
        try:
            data = tcpclisock.recv(4096).decode('utf-8')
            #if data is not None:
            #    print('接收',clientAddress,'消息:',data)
            
            infolist = data.split(":")
            print((usersName.decode("utf-8")+":"+infolist[1]))
            users[infolist[0]].send((usersName.decode("utf-8")+":"+infolist[1]).encode("utf-8"))  
        except:
            print(clientAddress,'已掉线或退出连接\r\n') 
            break

while True: 
    clientSocket,clientAddress = serversock.accept()
    t = threading.Thread(target=run,args=(clientSocket,clientAddress,))
    t.start()
    print(clientAddress,'连接上服务器...',sep='')
