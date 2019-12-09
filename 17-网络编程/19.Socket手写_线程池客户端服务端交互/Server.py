from socket import *
import time
from concurrent.futures import ThreadPoolExecutor

def run(tcpclisock,clientAddress): 
    while 1:  
        try:
            data = tcpclisock.recv(4096).decode('gbk')
            if data is not None:
                print('接收',clientAddress,'消息:',data)
            msg = ''.join(('服务端反馈（', ''.join([str(x) for x in clientAddress]), '）的消息已收到，内容："%s"!'%data))
            tcpclisock.send(msg.encode('gbk'))
        except:
            print(clientAddress,'已掉线或退出连接\r\n')
            break
    tcpclisock.close()

if __name__ == "__main__":
    pool = ThreadPoolExecutor(2)

    # 实例化对象
    serversock = socket(family=AF_INET, type=SOCK_STREAM)

    ip = ''
    port = 15213
    HOST = (ip, port)

    # 绑定IP、端口
    serversock.bind(HOST)

    # 监听客户端连接
    serversock.listen(15)
    print('服务器启动成功,等待客户端连接...')

    while True:
        clientSocket,clientAddress = serversock.accept()
        pool.submit(run,clientSocket,clientAddress)
        print(clientAddress,'连接上服务器...',sep='')
        
    serversock.close()