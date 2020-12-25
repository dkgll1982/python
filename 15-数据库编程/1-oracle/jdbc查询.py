import jaydebeapi
 
url = 'jdbc:oracle:thin:@127.0.0.1:1521:orcl'
user = 'cigproxy'
password = 'cigproxy'
dirver = 'oracle.jdbc.driver.OracleDriver'
jarFile = r'D:\Programing\pdi-ce-9.1.0.0-324\data-integration\lib\ojdbc8.jar'
sqlStr = 'select TABLE_NAME,NUM_ROWS from USER_TABLES WHERE ROWNUM<10'
# conn=jaydebeapi.connect('oracle.jdbc.driver.OracleDriver',['jdbc:oracle:thin:@127.0.0.1/orcl','scott','tiger'],'D:\\MY_TOOLS\\ojdbc6.jar')
# 注意此处配置不要写错，之前写成：jaydebeapi.connect(dirver, [url, user, password], jarFile) 一直报TypeError: Class oracle.jdbc.OracleDriver is not found 
conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
# conn = jaydebeapi.connect('oracle.jdbc.driver.OracleDriver',                                     
#                          'jdbc:oracle:thin:@127.0.0.1:1521:orcl', ['cigproxy', 'cigproxy'],      
#                          r'D:\Programing\pdi-ce-9.1.0.0-324\data-integration\lib\ojdbc8.jar')
curs = conn.cursor()
curs.execute(sqlStr)
result = curs.fetchall()
print(result)
curs.close()
conn.close()
 