import binascii
import hashlib

m, n = hashlib.md5(), hashlib.md5()
print(type(m), m.hexdigest(), type(m.hexdigest()))
m.update(b'123')
print(m, m.hexdigest())
# 重复调用update(arg)方法，是会将传入的arg参数进行拼接，而不是覆盖。也就是说，m.update(a); m.update(b) 等价于m.update(a+b)。
m.update(b'123')
print(m, m.hexdigest())
n.update(b'123123')
print(n.hexdigest() == m.hexdigest())

print('-'*40)

# 或者可以这样（最常见的写法，常用于图片的命名）
print(hashlib.md5(b'123').hexdigest())  # '202cb962ac59075b964b07152d234b70'

# 也可以使用hash.new()这个一般方法，hashlib.new(name[, data])，name传入的是哈希加密算法的名称，如md5
print(hashlib.new('md5', b'123').hexdigest())

# 中文加密：先将数据转换成UTF-8格式的，使用网上工具对比下加密的结果，发现有的md5加密工具并不是使用UTF-8格式加密的。
# 经测试目前发现可以转为UTF-8、GBK、GB2312、GB18030，不分大小写
# (因为GBK/GB2312/GB18030均是针对汉字的编码，所以md5加密后结果一样)。
data = '你好'
m1 = hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()      #十六进制
m2 = hashlib.md5(data.encode(encoding='gbk')).hexdigest()
m3 = hashlib.md5(data.encode(encoding='GB2312')).hexdigest()
m4 = hashlib.md5(data.encode(encoding='GB18030')).hexdigest()
print(m1)
print(m2)
print(m3)
print(m4) 

print('-'*40)

d1 = hashlib.md5(data.encode(encoding='UTF-8')).digest()         #hexdigest：十六进制；digest：二进制
print(d1)
 
# md5.digest()与md5.hexdigest()之间的转换
n1 = binascii.unhexlify(m1)
print(n1, n1 == d1)