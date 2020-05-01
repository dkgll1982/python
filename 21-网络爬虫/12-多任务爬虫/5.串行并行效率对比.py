import grequests
import time

#并行
start = time.time()
req_list = [grequests.get('https://www.baidu.com/') for i in range(200)]
res_list2 = grequests.map(req_list)
print(time.time()-start)

#串行
import requests
start = time.time()
res_list = [requests.get('https://www.baidu.com/') for i in range(200)]
print(time.time()-start)
 
