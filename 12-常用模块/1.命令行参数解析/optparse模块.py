import optparse

class Wang_opt:
    def __init__(self):
        #初始化
<<<<<<< HEAD
        #OptionParser 不要求一定要传递参数，不过传递一些参数，可以方便程序使用。
        # %prog 在这里会自动替换为程序名字
        # usage 可以打印用法
        # version 在使用 %prog --version 的时候输出版本信息
        parser = optparse.OptionParser(usage="%prog [-s] [-P] [-u] [-p]",version="%prog 1.0")
=======
        parser = optparse.OptionParser()
>>>>>>> 8c71f90a755f435117c304b5b10d4370e123be32
        parser.add_option("-s", "--server", dest="server", help="ftp server ip_address")
        parser.add_option("-P", "--port", type="int", dest="port", help="ftp server port")
        parser.add_option("-u", "--username", dest="username", help="username info")
        parser.add_option("-p", "--password", dest="password", help="password info")
        #解析参数
        self.options, self.args = parser.parse_args()
        print(self.options,self.args)  

    def verification(self):
        if not self.options.server or not self.options.port:
            exit('ERROR!must support server and port parameters!')

if __name__ == '__main__':
    whw_opt = Wang_opt()
    #如果要求用户必须有输入的话，我们可以这样来优化一下程序
    whw_opt.verification()