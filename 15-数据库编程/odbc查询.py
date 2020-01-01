import pyodbc
 
#DSN名称
conn = pyodbc.connect('DSN=DM8')

sqlStr = 'select * from "PERSON"."ADDRESS"'

cursor = conn.cursor()
 
cursor.execute(sqlStr)
row = cursor.fetchone()         #取出首行
print(row)
result = cursor.fetchall()      #取出所有行
for row in result:
    print(row)
cursor.close()
conn.close()

