# -*- coding: UTF-8 -*-
import M2Crypto
import base64

#私钥加密，公钥解密
def pri_encrypt(msg, file_name):
    rsa_pri = M2Crypto.RSA.load_key(file_name)
    ctxt_pri = rsa_pri.private_encrypt(msg, M2Crypto.RSA.pkcs1_padding) #这里的方法选择加密填充方式，所以在解密的时候 要对应。
    ctxt64_pri = base64.b64encode(ctxt_pri)  #密文是base64 方便保存 encode成str
    print ('密文:%s'% ctxt64_pri)
    return ctxt64_pri

def pub_decrypt_with_pubkeyfile(msg, file_name):
    rsa_pub = M2Crypto.RSA.load_pub_key(file_name)
    pub_decrypt(msg, rsa_pub)
    
def pub_decrypt_with_pubkeystr(msg, pub_key):
    #将pub_key转成bio对象,再将bio对象转换成公钥对象
    bio = M2Crypto.BIO.MemoryBuffer(pub_key)
    rsa_pub = M2Crypto.RSA.load_pub_key_bio(bio)
    pub_decrypt(msg, rsa_pub)
    
def pub_decrypt(msg, rsa_pub):
    ctxt_pri = base64.b64decode(msg) # 先将str转成base64
    maxlength = 128
    output = ''
    while ctxt_pri:
        input = ctxt_pri[:maxlength]
        ctxt_pri = ctxt_pri[maxlength:]
        out = rsa_pub.public_decrypt(input, M2Crypto.RSA.pkcs1_padding) #解密
        output = output + out
    print('明文:%s'% output)
    
if __name__ == "__main__":
    prikey_file = './rsa/rsa_private_key.pem'
    pubkey_file = './rsa/rsa_public_key.pem'
    msg = 'Test String.'
    primsg = pri_encrypt(msg, prikey_file)
    pub_decrypt(primsg, pubkey_file)