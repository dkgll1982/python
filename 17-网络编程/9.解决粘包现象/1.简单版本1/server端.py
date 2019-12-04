#参考链接：https://www.cnblogs.com/xiao-apple36/p/9276777.html
import socket
import subprocess
import struct
 
def cmd_exec(cmd):
    """
    执行shell命令
    :param cmd:
    :return:
    """
    p = subprocess.Popen(cmd, shell=True,
    stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        return stderr
    return stdout
 
sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 重用地址端口
sock_server.bind(('127.0.0.1', 8088))
 
sock_server.listen(1)  # 开始监听，1代表在允许有一个连接排队，更多的新连接连进来时就会被拒绝
print('starting...')
while True:
    conn, client_addr = sock_server.accept()  # 阻塞直到有连接为止，有了一个新连接进来后，就会为这个请求生成一个连接对象
 
    print(client_addr)
 
    while True:
        try:
            data = conn.recv(1024) # 接收1024个字节
            if not data: break  # 适用于linux操作系统,防止客户端断开连接后死循环
            print('客户端的命令', data.decode('gbk'))
            res = cmd_exec(data.decode('gbk'))  # 执行cmd命令
            # 第一步：制作固定长度的报头4bytes
            total_size = len(res)
            header = struct.pack('i',total_size)
 
            #  第二步：把报头发送给客户端
            conn.send(header)
 
            # 第三步：再发送真实的数据
            conn.sendall(res)
 
        except ConnectionResetError:  # 适用于windows操作系统,防止客户端断开连接后死循环
            break
    conn.close()
 
server.close()