# 字符串模板中使用key
temp = '教程是:%(name)s, 价格是:%(price)010.2f, 出版社是:%(publish)s'
book = {'name':'Python基础教程', 'price': 99, 'publish': 'C语言中文网'}
# 使用字典为字符串模板中的key传入值
print(temp % book)
book = {'name':'C语言小白变怪兽', 'price':159, 'publish': 'C语言中文网'}
# 使用字典为字符串模板中的key传入值
print(temp % book)

dict = [
    {
        "name":'张三',
        "age":24,
        "sex":"男",
        "aihao":'美女'
    },
    {
        "name":'吴霞',
        "age":14,
        "sex":"女",
        "aihao":'美食'
    },
    {
        "name":'李强',
        "age":28,
        "sex":"男",
        "aihao":'电玩'
    }
]
for it in dict:
    print('姓名:%(name)s,年龄:%(age)d,性别:%(sex)s,爱好:%(aihao)s'%it)