import requests
from concurrent.futures import ThreadPoolExecutor

urls_list = [
    'https://www.baidu.com',
    'http://www.gaosiedu.com',
    'https://www.jd.com',
    'https://www.taobao.com',
    'https://news.baidu.com',
]
#pool = ThreadPoolExecutor(3)

def request(url):
    response = requests.get(url) 
    return response

def read_data(future,*args,**kwargs):
    response = future.result()
    response.encoding = 'utf-8'
    print(response.status_code,response.url)

def main():
    # for url in urls_list:
    #     done = pool.submit(request,url)
    #     done.add_done_callback(read_data)
    
    with ThreadPoolExecutor(max_workers=3) as pool: 
        for result in pool.map(request,urls_list):
            print(result.status_code,result.url)

if __name__ == '__main__':
    main()
    # pool.shutdown(wait=True) 