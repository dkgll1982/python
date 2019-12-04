import socket
import subprocess
import struct
import json
import os

def get(file_name,conn):
    #3：以读的方式打开文件，读取文件内容发送到客户端
    #第一步:制作固定长度的报头
    header_dict = {
        'file_name':file_name,           #文件名，不含全路径
        'author':'suixin',
        'comapany':'航天神舟智慧系统技术有限公司',
        'md5':'12345',
        'file_size':os.path.getsize(file_name)
    }
    
    #json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False
    header_str = json.dumps(header_dict,ensure_ascii=False)
    header_bytes = header_str.encode('gbk')

    #第二步:发送报头的长度
    header_size = struct.pack('i',len(header_bytes))
    conn.send(header_size)

    #第二步:把报头发送给客户端
    conn.send(header_bytes)

    #第三步:再发送真实的数据
    with open(file_name,'rb') as f:
        for line in f:
            conn.send(line)

def run():
    phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    phone.bind(('127.0.0.1',15212))
    phone.listen(5)

    print('服务器已上线...')

    while True:                 #链接循环
        conn,clientaddress = phone.accept()
        print(clientaddress)

        while True:                                  #通信循环
            try:
                #1：收命令
                res = conn.recv(8096) 
                #if not res:break                    #适用于Linux操作系统
                
                #2：解析命令，提取相应参数
                #cmds = res.decode('gbk').split()    #得到['get,'xxxx.txt']的列表形式,这种方式文件路径不能带空格
                #file_name = cmds[1]

                cmd = res.decode('gbk')
                file_name = cmd[4:]    #得到'xxxx.txt'的列表形式,前边约定为'get '的形式
                if cmd.startswith("get"):
                    get(file_name,conn)
                
            except ConnectionResetError:        #适用于windows操作系统
                print(clientaddress,'已掉线或退出连接\r\n')
                break
        conn.close()

    phone.close()

if __name__=="__main__":
    run()