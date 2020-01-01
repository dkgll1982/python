
def test():  
    arg1 = '局部1'
    print('变量：%s，%s'%(arg1,arg2))
    #arg1 ='局部1'

arg1 = '全局1'
arg2 = '全局2'
test() 
print('变量：%s，%s'%(arg1,arg2))

print('------------------------------------------------------')

a = 10  # a1 当前模块全局变量
def outer():
    a = 9 # a2 outer局部变量
    def inner():
        #nonlocal关键字：声明此变量与外层同名变量为相同变量 
        #用于在内层函数中改变外层函数变量
        nonlocal a
        a = 8  # a3  既是inner局部变量，又是外层outer局部变量
        print(a)  # a3 8，在inner的局部作用域中找到了a3
    inner()  # inner()函数结束，a3作为外层变量(outer局部变量)被保留成为a2
    print(a)  # a2 8,在outer局部作用域中找到a2（在inner中被改变）
outer()  # outer()函数结束，a2作为outer局部变量被释放
print(a)  # a1 10，在当前模块全局作用域中找到了a1 

print('------------------------------------------------------')

#注意：如果在外层没有找到变量a,则会继续在再外层寻找，直到全局作用域的下一层为止
a = 10  # a1 当前模块全局变量
def outer2():
    a = 9 # a2 outer2作用域局部变量
    print(a) # a2 9,还未被a3改变
    def outer1():
        print(a) # a2 9,在outer1中没找到局部变量a，则寻找外层(outer2)变量a2(还未被a3改变)
        def inner():
            nonlocal a
            a = 0  # a3 既是inner局部变量，又是再外层outer2作用域变量
            print(a)  # a3 0, 找到inner局部变量a3
        inner()  # inner()函数结束，a3作为外层变量(outer2局部变量)被保留成为a2
        print(a)  # a2 0,在outer1中没找到局部变量a，则寻找外层(outer2)变量a2(被a3改变)
    outer1()
    print(a) # a2 0, 在outer1中找到outer1局部变量a2(被a3改变)
outer2() 
print(a)  # a1 10，在当前模块全局作用域中找到了a1
# 9 9 0 0 0 10

print('------------------------------------------------------')

#全局变量不是外层变量，不被nonlocal寻找
a = 10  # a1 当前模块全局变量
def outer():
    #此处声明相同的全局变量a也同样不能被nonlocal找到
    #global a 
    #a = 1
    def inner():
        #nonlocal a  # 在当前作用域外层即outer局部作用域中没找到outer局部变量a，outer外层为全局作用域，nonlocal不继续寻找，报错
        a = 8
        print(a)
    inner()
    print(a)
outer() 
print(a)  # a1 10，在当前模块全局作用域中找到了a1 