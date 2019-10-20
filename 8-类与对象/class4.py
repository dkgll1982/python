class Record:
    # 定义两个类变量
    item = '鼠标'
    date = '2016-06-16'
    def info (self):
        print('info方法中: ', self.item)
        print('info方法中: ', self.date)
rc = Record()
print(rc.item) # '鼠标'
print(rc.date) # '2016-06-16'

rc.item = '键盘'
rc.info()

print('-'*40)

# 静态方法，其实就是我们学过的函数，和函数唯一的区别是，静态方法定义在类这个空间（类命名空间）中，
# 而函数则定义在程序所在的空间（全局命名空间）中。

# 静态方法没有类似 self、cls 这样的特殊参数，因此 Python 解释器不会对它包含的参数做任何类或对象的绑定，
# 也正是因为如此，此方法中无法调用任何类和对象的属性和方法，静态方法其实和类的关系不大。
class Bird:
    # staticmethod修饰的方法是静态方法
    @staticmethod
    def info (p):
        print('静态方法info: ', p)

Bird.info("classname")

f = Bird()
f.info("类对象")

class User:
    def walk ():
        print('正在慢慢地走')
# 通过类调用实例方法

u = User()
User.walk()