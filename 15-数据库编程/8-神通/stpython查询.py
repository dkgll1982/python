import STPython

connection = STPython.Connection(user='sysdba',password='szoscar55',dsn='10.21.198.201:2003/osrdb')
cur = STPython.Cursor(connection) 
cur.execute('select * from public.test')
print(cur.fetchall())