#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
'''
 * @Author: Yanta 
 * @Date: 2018-08-16 15:32:52 
 * @Last Modified by:   Yanta 
 * @Last Modified time: 2018-08-16 15:32:52 
 * @Desc: 
'''
 



TI=input("\n\n按下 enter 键后退出");
print(TI);

list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john'] 
list.append('Google')   ## 使用 append() 添加元素
list.append('Runoob')
del list[2]
list[2] = 2001;

print ('%d,%s'%(len(list),'jerry')) 
print (list);                   # 输出完整列表
print (list[0]);                # 输出列表的第一个元素
print (list[1:3]);              # 输出第二个至第三个元素 
print (list[2:]);               # 输出从第三个开始至列表末尾的所有元素
print (tinylist * 2);           # 输出列表两次
print (list + tinylist);        # 打印组合的列表

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:            # 第二个实例
   print ('当前水果 :', fruit);

tinydict = {'name': 'john','code':6734, 'dept': 'sales'};
for a in tinydict:
    print (a);                  # 输出完整的字典
print (tinydict.keys());        # 输出所有键
print (tinydict.values());      # 输出所有值
