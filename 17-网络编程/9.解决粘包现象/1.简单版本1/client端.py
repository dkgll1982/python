import socket
import struct
 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(client)
 
 
client.connect(('127.0.0.1', 8088))
 
while True:
    data = input('input >>>')
    if not data:  # 如果数据为空，继续输入
        continue
 
    client.send(data.encode('GBK'))  # 发送数据
 
    # 第一步：先收报头
    header = client.recv(4)
    # 第二步：从报头中解析出对真实数据的描述信息（数据的长度）
    total_size = struct.unpack('i',header)[0]
    print('收到数据长度=',total_size)
 
    # 第三步：接收真实的数据
    recv_size = 0
    recv_data = b''
    while recv_size < total_size:
        data = client.recv(1024)   # 接收数据
        recv_data += data
        recv_size += len(data)  # 不能加1024，如果加进度条，会计算有误
 
 
 
    print('接收数据 =', recv_data.decode('gbk', 'ignore'))  # 如果设置为ignore，则会忽略非法字符；
 
client.close()  # 关闭