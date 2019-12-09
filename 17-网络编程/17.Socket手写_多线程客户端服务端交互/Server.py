from socket import *
import time
import threading

#实例化对象
serversock = socket(family=AF_INET,type=SOCK_STREAM)

ip =''
port = 15213
HOST = (ip,port)

#绑定IP、端口
serversock.bind(HOST)

#监听客户端连接
serversock.listen(15)
print('服务器启动成功,等待客户端连接...') 

def run(tcpclisock,clientAddress):
    while 1:  
        try:
            data = tcpclisock.recv(4096).decode('utf-8')
            if data is not None:
                print('接收',clientAddress,'消息:',data)
            msg = ''.join(('服务端反馈（', ''.join([str(x) for x in clientAddress]), '）的消息已收到，内容："%s"!'%data)) 
            tcpclisock.send(msg.encode('utf-8'))   
        except:
            print(clientAddress,'已掉线或退出连接\r\n') 
            break

while True: 
    clientSocket,clientAddress = serversock.accept()
    t = threading.Thread(target=run,args=(clientSocket,clientAddress,))
    t.start()
    #run(clientSocket,clientAddress)
    print(clientAddress,'连接上服务器...',sep='')
