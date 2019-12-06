from socket import *
ip_port=('127.0.0.1',9003)
#如果接收的字节大于发送的字节，windows系统会报一下错误：
#OSError: [WinError 10040] 一个在数据报套接字上发送的消息大于内部消息缓冲区或其他一些网络限制，或该用户用于接收数据报的缓冲区比数据报小。
#bufsize=1024
bufsize=10240

udp_client=socket(AF_INET,SOCK_DGRAM)
while True:
    msg=input('>>: ').strip()
    udp_client.sendto(msg.encode('gbk'),ip_port)

    data,addr=udp_client.recvfrom(bufsize)
    print(data.decode('gbk'),end='')