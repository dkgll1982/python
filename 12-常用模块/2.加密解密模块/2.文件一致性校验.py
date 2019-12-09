import binascii
import hashlib 

print('-'*40)
print('-- 文件一致性校验                     --')
print('-'*40)

# -----------文件一致校验----------------
'''可以拷贝一个文件放在两个不同的盘中，然后通过判断两个文件的hash值是否相等，判断两个文件是否是同一个文件'''
m = hashlib.md5()
with open(r'backup\1.txt','rb') as f:
    for line in f:
        m.update(line)
print(m.hexdigest())          #47a6b079cc33a4f312786b46e61e0305
 
n = hashlib.md5()
with open(r'backup\2.txt','rb') as f:
    for line in f:
        n.update(line)
print(n.hexdigest())
if m.hexdigest() == n.hexdigest():
    print('文件一致！')
else:
    print('文件校验失败！')

# -----------文件一致校验----------------