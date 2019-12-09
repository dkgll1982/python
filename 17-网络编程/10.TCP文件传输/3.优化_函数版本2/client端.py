import socket
import struct
import json
import os.path

# 定义下载的目录路径，注意：这部分一般应该写在配置文件中
DOWNLOAD_DIR = r"backup"


def get(client):
    # 接受服务器发来的文件内容，以write模式打开新文件，接受服务端发来的文件内容并写入
    # 第一步：先收报头长度(4bytes)的数据
    obj = client.recv(4)  # 接收服务器发来的，由struct打包的4bytes包
    header_size = struct.unpack('i', obj)[0]  # 解包，获得报头长度

    # 第二部：收报头
    header_bytes = client.recv(header_size)  # 根据报头长度收报头

    # 第三部：从报头中解析出真实数据的描述信息
    header_json = header_bytes.decode('utf-8')
    header_dic = json.loads(header_json)
    total_size = header_dic['total_size']
    filename = header_dic['filename']

    # 第四部：接受真实收据
    with open(os.path.join(DOWNLOAD_DIR, filename), 'wb') as f:
        recv_size = 0
        while recv_size < total_size:  # 循环直到收完指定长度的包
            line = client.recv(1024)
            f.write(line)
            recv_size += len(line)
            print('总大小%s，已经下载%s' % (total_size, recv_size))  # 这样我们可以知道进度


def run():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8080))  # 连接服务器IP和端口
    while True:
        # 发命令
        cmd = input(">>>>:").strip()
        if not cmd:continue
        client.send(cmd.encode('utf-8'))  # 注意：这部分不需要放在get()函数中，因为发送数据是通用的操作
        cmds = cmd.split()
        if cmds[0] == 'get':
            get(client)
    client.close()


if __name__ == '__main__':
    run()