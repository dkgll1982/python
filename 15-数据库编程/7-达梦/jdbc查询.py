import jaydebeapi 

url = 'jdbc:dm://10.21.198.201:5236/DMHR'
user = 'SYSDBA'
password = 'tggc12345'
dirver = 'dm.jdbc.driver.DmDriver'
jarFile = r'D:\\Data\\DmJdbcDriver18.jar'
sqlStr = 'select * from dual'
conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
curs = conn.cursor()
curs.execute(sqlStr)
result = curs.fetchall()
print(result)
curs.close()
conn.close()

