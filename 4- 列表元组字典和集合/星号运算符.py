fm = ("myname","youname","hername")

def fun(*args):
    for x in args:
        print(x) 

print('-'*40)
fun(fm)
print('-'*40)
fun(*fm)

def printStr(first, **dict):
    print(str(first) + "\n")
    print(dict)
 
print('-'*40)

#*second表示任意多个（包含0个）无名参数，又称为元组参数，最终的类型为tuple（注意：就算传递一个元素，也会最终变为tuple）
#**anything表示任意多个关键字参数，又称为字典参数，最终的类型为dictionary
#注意：俩者同时存在时，一定需要将*second放在**anything之前 （重要的事情说三遍）
#注意：俩者同时存在时，一定需要将*second放在**anything之前
#注意：俩者同时存在时，一定需要将*second放在**anything之前

printDic = {"name":"tyson", "age":"99"} 
 
printStr(100, **printDic)
 
printStr(100, name = "tyson", age = "99")               #等同于上面**printDic 

print('-'*40)

def print_str(first, second,three=3,*args,**kwargs):
    print('first:%s,second:%s,three:%s'%(first,second,three))
    for x in args:                          #可变参数
        print('可变参数：%s'%x)
    for key in kwargs:                      #字典参数
        print("%s=%s"%(key,kwargs[key]))
    
numbers_strings = ("11","12",'13','14','15','16','17',{'name':'张三',"age":'100',"sex":'男性'})     #解包

#*参数，虽然叫元组参数，你可别传个完整的元组对象进来哈（只算一个），如果是个元组，记得做解封，不然就要背锅了，就是要这样*turple传进去
print_str(*numbers_strings,**numbers_strings[7])

print('-'*40)

def printStr(**anything):
    print(anything)

printStr(first = 5, second = 100)

#**参数，虽然叫字典参数，你可别传个完整的字典对象进来哈（只算一个），如果是个字典，记得也是做解包，对，就是要这样 **dict传进去
printStr(**{'name':'张三',"age":'100',"sex":'男性'})      #字典参数解包
