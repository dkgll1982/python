import pyodbc

# 第一种连接方式：驱动名称等参数
# DRIVER = "{OSCAR ODBC DRIVER}"
# SERVER = "127.0.0.1"
# PORT = 2003
# UID = "SYSDBA"
# PWD = "szoscar55"
# CONN = "DRIVER=%s;SERVER=%s,%s;UID=%s;PWD=%s" % (
#     DRIVER, SERVER, PORT, UID, PWD)
#第一种连接方式：DSN名称
conn = pyodbc.connect('DSN=st,UID=SYSDBA,PWD=szoscar55')

sqlStr = 'select * from "PUBLIC"."TEST"'

cursor = conn.cursor()

cursor.execute(sqlStr)
row = cursor.fetchone()         #取出首行
print(row)
result = cursor.fetchall()      #取出所有行
for row in result:
    print(row)
cursor.close()
conn.close()
