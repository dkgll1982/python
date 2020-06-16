import jaydebeapi

url = 'jdbc:oracle:thin:@127.0.0.1:1521/orcl'
user = 'cigproxy'
password = 'cigproxy'
dirver = 'oracle.jdbc.driver.OracleDriver'
jarFile = r'D:\\data\\ojdbc8.jar'
sqlStr = 'select * from dual'
#conn=jaydebeapi.connect('oracle.jdbc.driver.OracleDriver','jdbc:oracle:thin:@127.0.0.1:1521/orcl',['hwf_model','hwf_model'],'E:/pycharm/lib/ojdbc14.jar')
conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
curs = conn.cursor()
curs.execute(sqlStr)
result = curs.fetchall()
print(result)
curs.close()
conn.close()