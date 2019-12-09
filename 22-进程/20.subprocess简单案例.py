import subprocess
#参考链接：https://www.jb51.net/article/57208.htm

# 概述：由subprocess去执行系统命令的时候并不会让主进程去执行，而是主进程会开辟出一个子进程去执行，并不会影响到主进程的运行，主进程该干嘛就干嘛，
# 那么又有个问题，大家都知道进程之间的内存空间是独立的，也就是说进程之间是不能相互访问的，那么在subprocess中，有个管道的概念，既然固定死了进程之间不能相互访问，
# 那么可以将执行命令的结果输出到管道里，该管道其实就是一块共享的内存空间，可以让主进程去获取到该共享内存空间存放的数据

# 创建一个子进程去执行系统命令
obj = subprocess.Popen(
    #'ps -ef',                       # 执行的系统命令（必须是字符串格式）
    #'ipconfig',                     # 执行的系统命令（必须是字符串格式）
    'lsnrctl status',                # 执行的系统命令（必须是字符串格式）
    shell = True,                    # 指定命令解释器来解释执行的这条命令
    stdout = subprocess.PIPE,        # 将执行的正确结果丢到管道(共享内存空间，用于进程之间共享)
    stderr = subprocess.PIPE         # 将执行的错误结果丢到另一个新的管道
)

'''
当从任意一个管道，例如正确或者错误结果管道中获取值，
''' 

# 从正确管道中获取值 
res = obj.stdout.read()               # 主进程去管道里获取正确的结果
print('正确管道：',res.decode('gbk'))  # 获取的结果是bytes类型，需要指定decode指定编码 （windows：GBK,Linux：UTF-8）

# 从错误管道中获取值 
res2 = obj.stderr.read()
print('错误管道：',res2.decode('gbk'))
