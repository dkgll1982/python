# 重点
'''模拟撞库破解密码'''
import hashlib
passwds=[                      #可以通过random实现对passwds中的内容
    'alex3714',
    'alex1313',
    'alex94139413',
    'alex123456',
    '123456alex',
    'a123lex',
    ]

def make_passwd_dic(passwds):                #通过明文密码列表，造出与之对应的hash值得字典
    dic={}
    for passwd in passwds:
        m=hashlib.md5()                      #使用md5算法，造了一个工厂
        m.update(passwd.encode('utf-8'))     #给工厂运送原材料(即我们要加密的内容)
        dic[passwd]=m.hexdigest()            #产出hash值（即最终的产品），将其加入到我们事先造好的空字典中，字典形式:{密码：hash值}
    return dic

def break_code(cryptograph,passwd_dic):      #判断拦截的hash值是否与字典中事先造好的hash值相等，相等则说明成功进行破解
    for k,v in passwd_dic.items():
        if v == cryptograph:
            print('密码是===>\033[46m%s\033[0m' %k)

cryptograph='aee949757a2e698417463d47acac93df'     #我们拦截拿到的密码，经过加密的hash值
break_code(cryptograph,make_passwd_dic(passwds))   #将要破解的密码hash值，和事先造好的hash的字典当做函数的实参传给对应的形参