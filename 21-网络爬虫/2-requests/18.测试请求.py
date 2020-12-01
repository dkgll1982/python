import requests

def send_request(url,header):
    response = requests.get(url = url,headers = header)
    if response.status_code == 200:
        return response

def write_content(content):
    with open(r'backup\test.html','w') as f:
        f.write(content)
        
if __name__ == "__main__":
    url = 'https://careers.tencent.com/search.html?index=1'
    header = {      
        "user_agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
    }
    res = send_request(url,header)
    if res:
        write_content(res.text) 
        
