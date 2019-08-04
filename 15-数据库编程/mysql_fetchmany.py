# 导入访问MySQL的模块
import pymysql.cursors

# ①、连接数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='cig', charset='utf8', cursorclass=pymysql.cursors.DictCursor)

# ②、获取游标
c = conn.cursor()
# ③、调用执行select语句查询数据
c.execute('select * from user_tb where user_id > %s', (2,))
# 通过游标的description属性获取列信息
for col in (c.description):
    print(col[0], end='\t')
print('\n--------------------------------')
while True:
    # 每次抓取3条记录，该方法返回一个多个元组组成的列表
    rows = c.fetchmany(3)
    # 如果抓取的row为None，退出循环
    if not rows :
        break
    # 再次使用循环遍历获取的列表
    for r in rows:
        print(r)
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()