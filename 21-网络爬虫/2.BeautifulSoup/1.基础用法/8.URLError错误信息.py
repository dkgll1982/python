import urllib.request
import urllib.response
import urllib.parse
import urllib.error 
from urllib import request
 
#req = request.Request(url='https://www.xxxxxx.com',method='get') 
req = request.Request('http://blog.csdn.net/cpqcre')
try:  
    request.urlopen(req)
except urllib.error.HTTPError as e:
    print(e.code,e.reason)
except urllib.error.URLError as e:
    print(e.code,e.reason)
else:
    print ("OK")