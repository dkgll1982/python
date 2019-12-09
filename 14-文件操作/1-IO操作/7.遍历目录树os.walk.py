import os

for dir,subdir,file in os.walk(r'2-练习例子'):
    print('目前目录名称：',dir)
    print('目前子目录名称：',subdir)
    print('目前文件名称：',file)

s1 ='我是一个完成的字符串,请找出我的位置'
s2 = '字符串'
print("%s在%s中中第一次出现的位置%d"%(s2,s1,s1.find(s2)))