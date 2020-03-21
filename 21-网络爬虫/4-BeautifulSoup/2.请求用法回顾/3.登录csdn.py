import urllib.request
import urllib.response 
import urllib.parse
import urllib.error 
from urllib import request
 
values = {"username":"dkgll","password":"tggc123456789"}
data = bytes(urllib.parse.urlencode(values),'utf8')
url = "https://passport.csdn.net/login?from=http://my.csdn.net/my/mycsdn"
request = request.Request(url,data)
response = urllib.request.urlopen(request)
print(response.read())