import collections
#参考链接：https://www.php.cn/python-tutorials-358240.html

d = collections.deque()

d.append(1)

d.append(2)

d.appendleft(0)

d.extend(['a','b','c','d','e'])

#extendleft(从队列左边扩展一个列表的元素)
d.extendleft([3,4,5])

print(d)    #输出：deque([1, 2])

#pop（获取最右边一个元素，并在队列中删除）
x = d.pop()

print(x,d)  #输出：e deque(['a', 'b', 'c', 'd'])

#reverse（队列反转）
d.reverse()
print(d)#输出：deque(['e', 'd', 'c', 'b', 'a'])

#rotate（把右边元素放到左边）
d.rotate(2)   

print(d)