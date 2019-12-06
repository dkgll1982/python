import socket
import struct
import json
import os.path

# 定义一个共享用文件夹的路径，注意：这部分一般应该写在配置文件中
SHARE_DIR = r'C:\Users\dkgll\Downloads'


def get(conn, cmds):  # get内容放入函数中
    filename = cmds[1]

    # 第一步：生成数据的报头信息数据(非固定长度)
    header_dic = {
        'filename': filename,
        'md5': 'xxxx',
        'total_size': os.path.getsize(os.path.join(SHARE_DIR, filename))
    }

    # 将报头encode（网络传输准备）
    header_json = json.dumps(header_dic)
    header_bytes = header_json.encode('utf-8')

    # 第二部：发送报头长度
    conn.send(struct.pack('i', len(header_bytes)))

    # 第三部：再发报头
    conn.send(header_bytes)

    # 第四部：最后发真实数据
    # 以read的模式读取文件内容(由于用于网络传输，所以是rb模式)，并且发送给客户端
    with open(os.path.join(SHARE_DIR, filename), 'rb') as f:
        # conn.send(f.read())  # 如果文件很大，内存会占满
        for line in f:  # 这样更加节省内存
            conn.send(line)


def run():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', 8080))
    server.listen(3)

    while True:
        conn, addr = server.accept()  # 等待连接，连接成功时实例化conn对象用来接下来的通信
        while True:
            try:
                # 收命令
                res = conn.recv(1024)  # 接收客户端命令(bytes类型),格式get a.txt
                if not res: break  # 异常处理：防止客户端强制断开连接，导致linux系统死循环
                # 解析命令，提取相应命令参数
                cmds = res.decode('utf-8').split()  # 解码后用空格分割
                if cmds[0] == 'get':
                    get(conn, cmds)  # 用函数封装了get的内容
            except ConnectionResetError as e:
                print(e)
                break
        conn.close()
    server.close()


if __name__ == '__main__':  # 这个写法是防止这个py文件被当做模块调用时，执行run()
    run()