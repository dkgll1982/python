import time
import os

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

while(True):
    # 暂停一秒
    time.sleep(1)

    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))