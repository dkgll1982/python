from socketserver import *

# 初始化控制器类Handler【Handler是一个继承BaseRequestHandler的类Handler中的handle方法决定了每一个连接过来的操作】 
#【控制器类的类名可以是其他的，不一定是Handler，只要继承了BaseRequestHandler就行】
class MvTCPHandler(BaseRequestHandler):
    def handle(self):
        try:
            while True:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address))
                print(self.data.decode('gbk'))
                self.request.sendall(self.data.upper())
        except Exception as e:
            print(self.client_address,"连接断开")
        finally:
            self.request.close()
    def setup(self):
        print("before handle,连接建立：",self.client_address)
    def finish(self):
        print("finish run after handle")

if __name__ == "__main__":
    HOST, PORT = "localhost", 9000

    #server = TCPServer((HOST, PORT), MvTCPHandler)             #单线程版
    server = ThreadingTCPServer((HOST, PORT), MvTCPHandler)     #多线程版
    server.allow_reuse_address=True                 #端口复用
    #持续循环运行：serve_forever()，即使一个连接报错了，但不会导致程序停止，而是会持续运行，与其他客户端通信
    server.serve_forever()
    #停止server_forever：shutdown()
    #server.shutdown()