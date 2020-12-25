import jaydebeapi 

url = 'jdbc:dm://127.0.0.1:5236/CIGPROXY'
user = 'SYSDBA'
password = 'tggc12345'
dirver = 'dm.jdbc.driver.DmDriver'
jarFile = r'D:\Programing\dmdbms\drivers\jdbc\DmJdbcDriver18.jar'
sqlStr = 'select * from "CIGPROXY"."TEST"'
conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)

# conn = jaydebeapi.connect('dm.jdbc.driver.DmDriver',                                     
#                          'jdbc:dm://10.21.198.201:5236/DMHR', ['SYSDBA', 'tggc12345'],      
#                          r'D:\Programing\pdi-ce-9.1.0.0-324\data-integration\lib\\DmJdbcDriver17.jar')

curs = conn.cursor()
curs.execute(sqlStr)
result = curs.fetchall()
print(result)
curs.close()
conn.close()

