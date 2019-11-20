#!/usr/bin/python
# -*-coding:utf-8 -*-
  
import copy
a = [1, 2, 3, 4, ['a', 'b']] #原始对象
  
b = a                       #直接赋值,默认浅拷贝传递对象的引用而已,原始列表改变，被赋值的b也会做相同的改变
c = copy.copy(a)            #copy浅拷贝，没有拷贝子对象，所以原始数据改变，子对象会改变
d = copy.deepcopy(a)        #深拷贝，包含对象里面的自对象的拷贝，所以原始对象的改变不会造成深拷贝里任何子元素的改变
  
print(id(a),id(b),id(c),id(d))
a.append(5)                 #修改对象a
d.append(6)

a[4].append('c')            #修改对象a中的['a', 'b']数组对象
c[4].append('d')            #修改对象a中的['a', 'b']数组对象
a[4].pop()

print( 'a = ', a )
print( 'b = ', b )
print( 'c = ', c )
print( 'd = ', d )

print('='*60)
 
numset = {1,2,3}
deep_numset = numset
deep_numset.add(10)
print('浅复制-观察numset        ',numset)
print('浅复制-观察deep_numset   ',deep_numset)

#此处自带的copy方法其实还是deep copy，即拷贝对象和原始对象已经是两个完全独立互相不影响的对象
shallow_numset = numset.copy()

print(id(numset),id(deep_numset),id(shallow_numset))

shallow_numset.add(100)
print('深复制-观察numset        ',numset)
print('深复制-观察deep_numset   ',shallow_numset)