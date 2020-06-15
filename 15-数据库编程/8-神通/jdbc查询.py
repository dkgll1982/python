import jaydebeapi

# # 3.6运行正常，3.8运行报错（AttributeError: '_jpype.PyJPField' object has no attribute 'getStaticAttribute'）
# url = 'jdbc:oracle:thin:@10.21.198.126:15214/xe'
# user = 'cigwbj'
# password = 'esri@123'
# dirver = 'oracle.jdbc.driver.OracleDriver'
# jarFile = 'C:\\Program Files\\data-integration\\lib\\ojdbc8.jar'
# sqlStr = 'select TABLE_NAME,NUM_ROWS from USER_TABLES WHERE ROWNUM<10'
# # conn=jaydebeapi.connect('oracle.jdbc.driver.OracleDriver',['jdbc:oracle:thin:@127.0.0.1/orcl','scott','tiger'],'D:\\MY_TOOLS\\ojdbc6.jar')
# conn = jaydebeapi.connect(dirver, [url, user, password], jarFile)
# curs = conn.cursor()
# curs.execute(sqlStr)
# result = curs.fetchall()
# print(result)
# curs.close()
# conn.close()

#测试神通数据库连接（3.6运行正常，3.8运行报错）
url = 'jdbc:oscar://10.21.197.160:2003/osrdb'
user = 'SYSDBA'
password = 'szoscar55'
dirver = 'com.oscar.Driver'
jarFile = r'D:\Programing\pdi-ce-8.3.0.0-371\data-integration\lib\oscarJDBC16.jar'
sqlStr = 'select TABLE_NAME,NUM_ROWS from USER_TABLES WHERE ROWNUM<10'
# conn=jaydebeapi.connect('oracle.jdbc.driver.OracleDriver',['jdbc:oracle:thin:@127.0.0.1/orcl','scott','tiger'],'D:\\MY_TOOLS\\ojdbc6.jar')
conn = jaydebeapi.connect(dirver, [url, user, password], jarFile)
curs = conn.cursor()
curs.execute(sqlStr)
result = curs.fetchall()
print(result)
curs.close()
conn.close()

