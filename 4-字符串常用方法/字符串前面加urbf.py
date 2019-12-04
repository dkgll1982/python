import time

# Unicode 格式 进行编码，一般用在中文字符串前面，防止因为源码储存格式问题，导致再次使用时出现乱码。
print(u"我是含有中文字符组成的字符串。")

# b' ' 表示这是一个 bytes 对象
response = b'<h1>Hello World!</h1>'
bytes = '<h1>Hello World!</h1>'.encode('utf-8')
str = bytes.decode('utf-8')
print(response,type(response),bytes,type(bytes),str,type(str))

t0 = time.time()
time.sleep(1)
name = 'processing'

# 以 f开头表示在字符串内支持大括号内的python 表达式
print(f'{name} done in {time.time() - t0:.2f} s') 
