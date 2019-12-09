from conf import settings
import socketserver
from core.ftp_server import FtpHandler
import optparse
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


class ArgvHandler(object):
    def __init__(self, sys_args):
        self.parser = optparse.OptionParser()
        # parser.add_option("-s", "--host", dest="host", help="ftp server ip_address")
        # parser.add_option("-P", "--port", type="int", dest="port", help="ftp server port")
        # parser.add_option("-u", "--username", dest="username", help="username info")
        # parser.add_option("-p", "--pas sword", dest="password", help="password info")

        # 解析参数
        self.options, self.args = self.parser.parse_args()
        self.verify_args(self.options, self.args)

    def verify_args(self, options, args):
        '''校验并调用响应的功能'''
        if hasattr(self, args[0]):
            func = getattr(self, args[0])
            func()
        else:
            self.parser.print_help()

    def start(self):
        print('------going to start server-------')
        server = socketserver.ThreadingTCPServer(
            (settings.HOST, settings.PORT), FtpHandler)  # 多线程版
        server.serve_forever()
