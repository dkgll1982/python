from ctypes import *
 
dll = windll.LoadLibrary(r"D:\Programing\Python3.6\DLLs\aci.dll")  
print(dll) 
print('====================')
#连接数据库
r = dll.ACILogon(None,None,None,'SYSDBA','6','szoscar55','9','10.21.198.201:2003/osrdb','24');
print(r)