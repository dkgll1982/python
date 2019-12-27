import zipfile
import time
import threading
#参考链接：https://blog.csdn.net/zhouchen1998/article/details/82015318

startTime = time.time()
# 判断线程是否需要终止
flag = True 
 
def extract(password, file):
    try:
        password = str(password)
        file.extractall(path=r'backup\zipfile2', pwd=password.encode('utf-8'))
        print("the password is {}".format(password))
        nowTime = time.time()
        print("spend time is {}".format(nowTime-startTime))
        global flag
        # 成功解压其余线程终止
        flag = False
    except Exception as e:
        print(e)
 
 
def do_main():
    zfile = zipfile.ZipFile(r"backup\zipfile.zip", 'r')
    # 开始尝试（暴力破解）
    #for number in range(123,124):
    #    if flag is True:
    t = threading.Thread(target=extract, args=(123, zfile))
    t.start()
    t.join()
 
 
if __name__ == '__main__':
    do_main()
