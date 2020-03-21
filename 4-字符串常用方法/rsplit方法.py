/* * @Author: guojun  
* @Date: 2020-03-21 21:28:40  
* @Last Modified by:   mikey.zhaopeng  
* @Last Modified time: 2020-03-21 21:28:40  */
S = "this is string example....wow!!!"
print (S.rsplit( ))
print (S.rsplit('i',1))
print (S.rsplit('w'))

s = '2,3,4,5,6,7,7,8,'
print(s.rsplit(',')[:-1])
print(s.rsplit(',',1)[0])


s = '2,3,4,5,6,7,7,8,'
print(s.split(',')[:-1])
print(s.split(',',1))
