import  struct as s

print(s.calcsize('4s5si'))
print(s.calcsize('3s2s')) 
print(s.calcsize('ii'))
# 系统是按照4字节对齐，所以多出一个字符,即4+4=8
print(s.calcsize('2si')) 
print(s.calcsize('8si'))
# 系统是按照4字节对齐，所以多出一个字符,即8+4+4=16
print(s.calcsize('=9si'),s.calcsize('@9si'))
print(s.calcsize('=13si'),s.calcsize('13si'))
# short为2字节，int为4字节，2*2+4=8。
print(s.calcsize('hhi'))
print(s.calcsize("4ch"))
# ‘3ch’：如果使用默认设置需要6个字节，这是由于字节对齐造成的，
# 系统是按照4字节对齐，所以多出一个字符。使用‘=’可以设置系统不按字节对齐，所以需要5个字节。
print(s.calcsize("=3ch"))

# (1) h short integer 2 
# (3) H unsigned short integer 2 
# (3) i int integer 4 
# (3) I unsigned int integer 4 
# (3) l long integer 4 
# (3) L unsigned long integer 4 
# (3) q long long integer 8 (2), 
# (3) Q unsigned long long integer 8 (2), 
# (3) n ssize_t integer   
# (4) N size_t integer   
# (4) f float float 4 
# (5) d double float 8  