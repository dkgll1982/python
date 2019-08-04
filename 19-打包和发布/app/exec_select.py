# 导入访问MySQL的模块
import pymysql.cursors

def query_db(): 
    # ①、连接数据库
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='cig', charset='utf8', cursorclass=pymysql.cursors.DictCursor)

    # ②、获取游标
    c = conn.cursor()
    # ③、调用执行select语句查询数据
    c.execute('select * from user_tb where user_id > %s', (2,))
    # 通过游标的description属性获取列信息
    description = c.description
    # 使用fetchall获取游标中的所有结果集
    rows = c.fetchall()
    for col in (c.description):
        print(col)
    # ④、关闭游标
    c.close()
    # ⑤、关闭连接
    conn.close()
    return description, rows 