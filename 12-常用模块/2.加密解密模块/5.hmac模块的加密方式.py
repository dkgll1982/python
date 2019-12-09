'''python 还有一个 hmac 模块，它内部对我们创建 key 和 内容 进行进一步的处理然后再加密:'''
import hmac,hashlib


h = hmac.new('你好'.encode('utf8'),digestmod='MD5')  # hmac必须要加盐
print(h.hexdigest())  
h.update('hello'.encode('utf8'))
print(h.hexdigest())  # 1abaae8f65f68f2695a8545c5bc8e738

# 要想保证hmac最终结果一致，必须保证：
# 1:hmac.new括号内指定的初始key一样
# 2:无论update多少次，校验的内容累加到一起是一样的内容

# 下面单重方式得到的结果是一样的
h1 = hmac.new(b'tom',digestmod='MD5')  # 初始值必须保证一致，最终得到的结果就会不一样
h1.update(b'hello')
h1.update(b'world')
print(h1.hexdigest())

h2 = hmac.new(b'tom',digestmod='MD5')  # 初始值必须保证一致，最终得到的结果就会不一样
h2.update(b'helloworld')
print(h2.hexdigest())

h3 = hmac.new(b'tomhelloworld',digestmod='MD5')  # 初始值不一样，所以与上面两种的结果不一样
print(h3.hexdigest())

'''
0426ccec3b134e8c18fdcefee841ef25
0426ccec3b134e8c18fdcefee841ef25
ff1214d895bbaf5f1847db4ebae8212e
'''

print('-'*40)

key = '你好'
sign = "你好"
_sign1 = hashlib.md5(sign.encode(encoding='UTF-8')).hexdigest()
_sign2 = hmac.new(key.encode(encoding='UTF-8'),sign.encode(encoding='UTF-8'),digestmod='MD5').hexdigest()
#可以通过在线加密解密站点：http://encode.chahuo.com/进行验证
print(_sign1,_sign2)

print('-'*40)

message = b'123'
key = b'123'
h = hmac.new(key, message, digestmod='MD5')
# 如果消息很长，可以多次调用h.update(msg)
print(h.hexdigest())