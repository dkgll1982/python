#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-22 21:23
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : dict
# @Software: PyCharm

scores = {'语文': 89, '数学': 92, '英语': 93} 
scores['政治']=40
scores['数学']=40  
#删除元素，找不到传回Default设定的内容，没有设定则传回KeyError
scores.pop('2语文','DDDD')  
#存在则返回对应键的值数据，不存在则将键-值假如字典设置默认值，返回该默认值，如果未设置默认值，则返回None
yw = scores.setdefault('语文',182)  
wl = scores.setdefault('物理',82) 
print('语文：%d,物理：%d'%(yw,wl))
scores.setdefault('化学',92)
print(scores)
# 空的花括号代表空的dict
empty_dict = {}
print(empty_dict)
# 使用元组作为dict的key
dict2 = {(20, 30):'good',30:[1,2,3]}
print(dict2[(20, 30)])
print(dict2[30])

knowledge = {'语文':22, '数学':1, '英语':2}
scores = dict.fromkeys(knowledge,[22,88])
print(scores)

#通过 dict() 映射函数创建字典
a = dict(one=1, two=2, three=3)
print(a);

demo = [('two',2),('one',1),('three',3)] #方式1
a = dict(demo)
print(a);
demo = [['two',2],['one',1],['three',3]] #方式2
a = dict(demo)
print(a);
demo = (('two',2),('one',1),('three',3)) #方式3
a = dict(demo)
print(a);
demo = (['two',2],['one',1],['three',3]) #方式4
a = dict(demo)
print(a);

demokeys = ['one','two','three'] #还可以是字符串或元组
demovalues = [21,(2,),[3,6]] #还可以是字符串或元组
a = dict(zip(demokeys,demovalues))
print(a);

#dict.get(key[,default])
#其中，dict 指的是所创建的字典名称；key 表示指定的键；default 用于指定要查询的键不存在时，此方法返回的默认值，如果不手动指定，会返回 None。
print(a.get('four',"字典中无此键值！"))
del a["one"]
print(a);
#添加新键值对
a['语文'] = 89
print(a)
#再次添加新键值对
a['英语'] = 90
print(a)

#判断字典中是否存在指定键值对
print('英语' in a) # True
# 判断 a 是否包含名为'物理'的key
print('物理' in a) # False

print(type(a.keys()))
print(a.values())
print(a.items())
b= list(a.keys());
c=list(a.values());

for x in range(len(a)):
    print("%s=%s"%(b[x],c[x]),end=' ');

print("\n---------------")
for k,v in a.items():
    print("%s=%s"%(k,v),end='    ');

print("\n---------------")
#copy() 方法用于返回一个具有相同键值对的新字典，例如：
a = {'one': 1, 'two': 2, 'three': [1,2,3]}
b = a.copy()
a["three"].insert(2,43)
a["three"].remove(1)
print(b)

#update()方法
#update() 方法可使用一个字典所包含的键值对来更新己有的字典。
#在执行 update() 方法时，如果被更新的字典中己包含对应的键值对，那么原 value 会被覆盖；如果被更新的字典中不包含对应的键值对，则该键值对被添加进去。
a.update({'one':4.5, 'three': [1,2,3,4]})
print(a)
print(b)

# 将弹出项的key赋值给k、value赋值给v
k, v = b.popitem()
print(k, v)

#setdefault() 方法也用于根据 key 来获取对应 value 的值。
# 但该方法有一个额外的功能，即当程序要获取的 key 在字典中不存在时，该方法会先为这个不存在的 key 设置一个默认的 value，然后再返回该 key 对应的 value。
a = {'one': 1, 'two': 2, 'three': 3}
# 设置默认值，该key在dict中不存在，新增键值对
print(a.setdefault('four', 9.2))
print(a)
# 设置默认值，该key在dict中存在，不会修改dict内容
print(a.setdefault('one', 3.4))
print(a)

# 字符串模板中使用key
temp = '教程是:%(name)s, 价格是:%(price)010.2f, 出版社是:%(publish)s'
book = {'name':'Python基础教程', 'price': 99, 'publish': 'C语言中文网'}
# 使用字典为字符串模板中的key传入值
print(temp % book)
book = {'name':'C语言小白变怪兽', 'price':159, 'publish': 'C语言中文网'}
# 使用字典为字符串模板中的key传入值
print(temp % book)
print('-'*40)
users1 = {"name":"张三","age":22,"sex":"男","height":176,"edu":"研究生","nation":"汉族"}
users2 = {"name":"李四","age":32,"sex":"男","height":186,"edu":"博士","nation":"汉族"}
users3 = {"name":"柯洁","age":25,"sex":"男","height":166,"edu":"小学未毕业","nation":"汉族"}
stu1 = "姓名：%(name)s，年龄：%(age)d，性别：%(sex)s，身高:%(height)d,学历：%(edu)s，民族：%(nation)s"
stu2 = "姓名：{name}，年龄：{age}，性别：{sex}，身高:{height},学历：{edu}，民族：{nation}"
stu3 = "姓名：{0}，年龄：{1}，性别：{2}，身高:{3},学历：{4}，民族：{5}"

print(stu1 % users1)
print(stu2.format(**users2))
print(stu3.format("王五",12,"女",169,"文盲","汉族"))

olddict={'C语言中文网': 6, 'c.biancheng.net': 15}
newdict = {v: k for k, v in olddict.items() if v>10}
print(newdict)