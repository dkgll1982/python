#省略号也是对象
print(...,type(...),bool(...))

#如果一个or表达式中所有值都为真,Python会选择第一个值,而and表达式则会选择第二个.
l = (2 or 3) * (5 and 7)
print(l)

def func(item, item_list=[]):
    item_list.append(item)
    print(item_list) 

# 对于参数中提供了初始值的参数,由于 Python 中的函数参数传递的是对象,也可以认为是传地址,
# 在第一次初始化 def 的时候,会先生成这个可变对象的内存地址,然后将这个默认参数 item_list 会与这个内存地址绑定.
# 在后面的函数调用中,如果调用方指定了新的默认值,就会将原来的默认值覆盖.如果调用方没有指定新的默认值,那就会使用原来的默认值.
func('iphone')
func('huawei') 
func('oppo') 
func('xiaomi', item_list=['oppo','vivo'])

class Kls():
    def public(self):
        print('Hello public world!')

    def __private(self):
        print('Hello private world!')

    def call_private(self):
        self.__private()

ins = Kls() 
# 调用公有方法，没问题
ins.public() 
# 直接调用私有方法，不行(AttributeError: 'Kls' object has no attribute '__private')
#ins.__private()

# 但你可以通过内部公有方法，进行代理
# 调用私有方法，以下两种等价
ins._Kls__private()
ins.call_private()
print(dir(ins)) #可以看出有_Kls__private和call_private方法