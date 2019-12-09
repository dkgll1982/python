# 应用：对明文密码进行加密（暴力破解-------用明文密码用一种算法算出一个hash值，与截取的hash值进行比对，比对成功说明明文密码一致，就可以破解用户的密码）
'''如用户在某网站进行注册信息，这个时候防止信息被恶意拦截获取，可以对用户明文密码进行加密，存成hash值得形式，这样用户每次登陆虽然输的是明文密码，校验hash值即可'''
import hashlib

password = input('>>>>>:').strip()
m = hashlib.md5()
m.update(password.encode('utf-8'))
print(m.hexdigest())  # 00dcbdaede875d5e23f1f9f64c7849ef


# 对密码进行加盐（暗号）----------进一步加强密码的安全性
password = input('>>>>>:').strip()
m = hashlib.md5()
m.update('一行白鹭上青天'.encode('utf-8'))  # 对密码加盐
m.update(password.encode('utf-8'))
print(m.hexdigest())
