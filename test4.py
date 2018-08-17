#!/usr/bin/python3
 
from sys import stdout,argv,path  #  导入特定的成员
x = 'runoob'; 
stdout.write(x + '\n');

a = [1, 2, 3, 4, 5, 6]
a[0] = 9
a[2:5] = [13, 14, 15]
#a[2:5] = []   # 将对应的元素值设置为 [] 

print(a); 
tuple2 = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
print (tuple2[0])          # 输出元组的第一个元素
print (tuple2[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple2[2:])   

#print('================Python import mode==========================');
#print ('命令行参数为:')
#for i in argv:
#   print (i)
#print ('\n python 路径为',path)


a, b, c, d = '20', 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

print(isinstance(a, int))

v='1234567890'
v2=str(v[1:2]);

print((str(1)+v2+'-DFFS师傅师傅说--\n') * 3);
print(str(v[:]));