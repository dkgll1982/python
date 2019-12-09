import time  
import sys
import os
 
while True:
    os.system("cls")
    print("Loading",end = "")
    for i in range(10):
        print(".",end = '')
        sys.stdout.flush()
        if i <9:
            time.sleep(0.2) 

#!/user/bin env python
# author:Simple-Sir
# time:20180918
#打印进度条
# import sys,time
# print('\r\n打印进度条：',end='')
# for i in range(20):
#     sys.stdout.write('-') #标准化输出，类似print,print默认换行
#     sys.stdout.flush() #强制刷新，将内存中的内容写入硬盘
#     time.sleep(0.1) #推迟执行的秒数
#     if i == 19:
#         sys.stdout.write('100%')