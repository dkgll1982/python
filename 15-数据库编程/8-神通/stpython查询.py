import STPython

connection = STPython.Connection(user='sysdba',password='szoscar55',dsn='10.21.197.162:2003/osrdb')
cur = STPython.Cursor(connection) 
cur.execute('select * from "PUBLIC"."TEST"')
print(cur.fetchall())