import jaydebeapi 

url = 'jdbc:sqlite:D:\\data\\first.db'
user = 'SYSDBA'
password = 'szoscar55'
dirver = 'org.sqlite.JDBC'
jarFile = r'D:\Programing\pdi-ce-8.3.0.0-371\data-integration\lib\\sqlite-jdbc-3.7.2.jar'
sqlStr = 'select * from main.TEST'
conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
curs = conn.cursor()
curs.execute(sqlStr)
result = curs.fetchall()
print(result)
curs.close()
conn.close()

