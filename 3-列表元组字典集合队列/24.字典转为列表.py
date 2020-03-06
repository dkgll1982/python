dit =  {'id': 309, 'name': '小白', 'sex': '男', 'age': 28, 'addr': '河南省济源市北海大道32号', 'grade': '天蝎座', 'phone': '18512572946', 'gold': 120} 
 
# 将字典的key转换成列表
lst = list(dit)
print(lst)    #['id', 'name', 'sex', 'age', 'addr', 'grade', 'phone', 'gold']
 
# 将字典的value转换成列表
lst2 = list(dit.values())
print(lst2)   #[309, '小白', '男', 28, '河南省济源市北海大道32号', '天蝎座', '18512572946', 120]

print([dit])  #[{'id': 309, 'name': '小白', 'sex': '男', 'age': 28, 'addr': '河南省济源市北海大道32号', 'grade': '天蝎座', 'phone': '18512572946', 'gold': 120}] 
 
tup = ('1',2,3,4,5,6)

print([tup],list(tup)) 
