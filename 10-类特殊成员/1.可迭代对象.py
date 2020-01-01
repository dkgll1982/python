import collections
from collections.abc import Iterable, Iterator, Generator
# 参考链接：https://www.cnblogs.com/wongbingming/p/9060989.html

# 使用isinstance()来类别一个对象是否是可迭代的(Iterable),是否是迭代器(Iterator),是否是生成器(Generator)

# 字符串
astr = "XiaoMing"
print("字符串：{}".format(astr))
print(isinstance(astr, Iterable))
print(isinstance(astr, Iterator))
print(isinstance(astr, Generator))

# 列表
alist = [21, 23, 32,19]
print("列表：{}".format(alist))
print(isinstance(alist, Iterable))
print(isinstance(alist, Iterator))
print(isinstance(alist, Generator))

# 字典
adict = {"name": "小明", "gender": "男", "age": 18}
print("字典：{}".format(adict))
print(isinstance(adict, Iterable))
print(isinstance(adict, Iterator))
print(isinstance(adict, Generator))

# deque
adeque=collections.deque('abcdefg')
print("deque：{}".format(adeque))
print(isinstance(adeque, Iterable))
print(isinstance(adeque, Iterator))
print(isinstance(adeque, Generator))

# 从结果来看,这些可迭代对象都不是迭代器,也不是生成器.它们有一个共同点,就是它们都可以使用for来循环
# 扩展知识:
# 可迭代对象,是其内部实现了,__iter__ 这个魔术方法.
# 可以通过,dir()方法来查看是否有__iter__来判断一个变量是否是可迭代的.