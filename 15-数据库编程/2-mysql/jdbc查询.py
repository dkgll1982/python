import jaydebeapi 

url = 'jdbc:mysql://10.21.198.127:13306/CXZNMS'
user = 'root'
password = 'esri@123'
dirver = 'com.mysql.cj.jdbc.Driver'
jarFile = r'D:\Programing\datax\plugin\reader\mysqlreader\libs\mysql-connector-java-8.0.17.jar'
sqlStr = 'select id,YSLX,YSZT from YSJBXX limit 22'
conn = jaydebeapi.connect(dirver, url, [user, password], jarFile) 

curs = conn.cursor()
curs.execute(sqlStr)
result = curs.fetchall()
print(result)
curs.close()
conn.close()

