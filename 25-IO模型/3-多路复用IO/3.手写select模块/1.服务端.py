#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-12-29 12:53:00 
# @Last Modified by: guojun 
# @Last Modified time: 2019-12-29 12:53:00 
# @Software: vscode
#参考链接：https://www.cnblogs.com/liugp/p/11027878.html

import socket
import queue  
from select import select
  
SERVER_IP = ('127.0.0.1',9999)  
  
# 保存客户端发送过来的消息,将消息放入队列中  
message_queue = {}  
input_list = []  
output_list = []  
  
if __name__ == "__main__":  
    server = socket.socket()  
    server.bind(SERVER_IP)  
    server.listen(10)  
    # 设置为非阻塞  
    server.setblocking(False)  
  
    # 初始化将服务端加入监听列表  
    input_list.append(server)  
  
    while True:  
        # 开始select监听,对input_list中的服务端server进行监听
        # 要不断的调用select函数来检查给定的类文件对象是否有数据就绪,当且仅当有新客户端连接进来的时候,
        # server服务端这个套接字对象才是读就绪的,也就是才会存在于stdinput列表中；
        stdinput,stdoutput,stderr = select(input_list,output_list,input_list)  
  
        # 循环判断是否有客户端连接进来,当有客户端连接进来时select将触发  
        for obj in stdinput:  
            # 判断当前触发的是不是服务端对象,当触发的对象是服务端对象时,说明有新客户端连接进来了
            # 当客户端第一次连接服务端时,server服务端套接字对象,通过调用accept方法获取到新进来的客户端套接字,
            # 然后把新进来的客户端套接字对象追加到待select检测的inputs列表中。
            if obj == server:  
                # 接收客户端的连接,获取客户端对象和客户端地址信息  
                conn,addr = server.accept()  
                print("Client {0} connected!".format(addr))  
                # 将客户端对象也加入到监听的列表中,当客户端发送消息时select 将触发  
                input_list.append(conn)  
                # 为连接的客户端单独创建一个消息队列,用来保存客户端发送的消息  
                message_queue[conn] = queue.Queue()  
  
            else:  
                # 由于客户端连接进来时服务端接收客户端连接请求,将客户端加入到了监听列表中(input_list),客户端发送消息将触发  
                # 所以判断是否是客户端对象触发  
                try:  
                    recv_data = obj.recv(1024)  
                    # 客户端未断开,能正常接收客户端发送的数据时
                    if recv_data:
                        #getsockname与getpeername是返回套接口关联的本地协议地址和远程协议地址。
                        #getpeername:返回远程协议地址描述结构
                        #getsockname:返回本地协议地址描述结构
                        print("received {0} from client {1}".format(recv_data.decode('gbk'),obj.getpeername()))
                        # 将收到的消息放入到各客户端的消息队列中  
                        message_queue[obj].put(recv_data)  
  
                        # 将回复操作放到output列表中,让select监听  
                        if obj not in output_list:  
                            output_list.append(obj)  
  
                except ConnectionResetError:  
                    # 客户端断开连接了,将客户端的监听从input列表中移除  
                    input_list.remove(obj)  
                    # 移除客户端对象的消息队列  
                    del message_queue[obj]  
                    print("\n[input] Client  {0} disconnected".format(addr))  
  
        # 如果现在没有客户端请求,也没有客户端发送消息时,开始对发送消息列表进行处理,是否需要发送消息  
        for sendobj in output_list:  
            try:  
                # 如果消息队列中有消息,从消息队列中获取要发送的消息  
                if not message_queue[sendobj].empty():  
                    # 从该客户端对象的消息队列中获取要发送的消息  
                    send_data = message_queue[sendobj].get()  
                    sendobj.sendall(send_data)  
                else:  
                    # 将监听移除等待下一次客户端发送消息  
                    output_list.remove(sendobj)  
  
            except ConnectionResetError:  
                # 客户端连接断开了  
                del message_queue[sendobj]  
                output_list.remove(sendobj)  
                print("\n[output] Client  {0} disconnected".format(addr))