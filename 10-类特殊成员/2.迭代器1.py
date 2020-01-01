# 对比可迭代对象，迭代器其实就只是多了一个函数而已。就是__next__()，
# 我们可以不再使用for循环来间断获取元素值。而可以直接使用next()方法来实现。

# 迭代器，是在可迭代的基础上实现的。要创建一个迭代器，我们首先，得有一个可迭代对象。
# 现在就来看看，如何创建一个可迭代对象，并以可迭代对象为基础创建一个迭代器。

from collections.abc import Iterable, Iterator, Generator

class MyList(object):  # 定义可迭代对象类

    def __init__(self, num):
        self.end = num  # 上边界

    # 返回一个实现了__iter__和__next__的迭代器类的实例
    def __iter__(self):
        return MyListIterator(self.end)


class MyListIterator(object):  # 定义迭代器类

    def __init__(self, end):
        self.data = end  # 上边界
        self.start = 0

    # 返回该对象的迭代器类的实例；因为自己就是迭代器，所以返回self
    def __iter__(self):
        return self

    # 迭代器类必须实现的方法，若是Python2则是next()函数
    def __next__(self):
        while self.start < self.data:
            self.start += 1
            return self.start - 1
        raise StopIteration

if __name__ == '__main__':
    my_list = MyList(5)  # 得到一个可迭代对象
    print(isinstance(my_list, Iterable))  # True
    print(isinstance(my_list, Iterator))  # False
    # 迭代
    for i in my_list:
        print(i)

    my_iterator = iter(my_list)  # # 通过iter()，将可迭代对象转换为一个迭代器
    print(isinstance(my_iterator, Iterable))  # True
    print(isinstance(my_iterator, Iterator))  # True

    # 迭代
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))

    iter =MyListIterator(5)
    print(isinstance(iter, Iterable))  # True
    print(isinstance(iter, Iterable))  # True
    # 扩展知识:
    # 迭代器，是其内部实现了，__next__ 这个魔术方法。(Python3.x)
    # 可以通过，dir()方法来查看是否有__next__来判断一个变量是否是迭代器的。