#!/usr/bin/python3
import time
import os;

path="C:\\Users\dkgll\\Desktop\python目录";
time2=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime());
isExists=os.path.exists(path);

di3={
    "name":"张三ssss",
    "age":122,
    "sex":"男4",
    "birthday":time2
}

def fub(b):
    print ("你输入的参数是："+b);

# 打开一个文件
value = ('www.runoob.com', 14)
s = str(value)

f = open("C:\\Users\dkgll\\Desktop//处理消息.txt", "a")
f.write(s+"\n");
num2 = f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )

for i in range(100):
    f.write(str(i)+'\r\n')
f.close();

f2=open("C:\\Users\dkgll\\Desktop//分类施策接口.txt", "r")
for line in f2.readlines():
    print (line)
f2.close();
# 关闭打开的文件

print("s—>"+str(type(s)));
print("f—>"+str(type(f)));
print("isExists—>"+str(type(isExists)));
print("num2—>"+str(type(num2)));
print("value—>"+str(type(value)));
print("time2—>"+str(type(time2)));
print("di3—>"+str(type(di3)));
print("__name__—>"+str(type(__name__)));
print("{0:'zero'}—>"+str(type({0:'zero'})));
print("fub—>"+str(type(fub)));

#不存在则创建目录
#存在则直接写入文件
if(isExists):
    print(path+"已存在！");
else:
    print("不存在，将自动创建目录"+path);
    os.mkdir(path);
    print(path+"创建成功！");

xxoo = path + '\\1.txt'  # 在当前py文件所在路径下的new文件中创建txt

isExists=os.path.exists(xxoo);
if(isExists):
    print(xxoo+"已存在！");

file = open(xxoo, 'a')

file.write("append文件测试内容\n")  # 写入内容信息
file.close();