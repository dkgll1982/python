

import threading
import requests
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

Pass=[]
Fail=[]
restime=[]
class Multi_thread():
    def get_info(self,sumget,i,URL2,param):
        for n in range(sumget):

            try:
                r = requests.get(URL2, params=param, timeout=10)
                restime.append(r.elapsed.total_seconds())

                if r.status_code == 200:
                    # print (res.text)
                    # print(res.status_code)
                    Pass.append(r.status_code)
                    logger.info(str((i+1))+'线程的第'+str(n+1)+'次请求，请求成功，状态码' + str(r.status_code))
                else:
                    # print (res.status_code)
                    Fail.append(r.status_code)
                    logger.info(str(i*n)+'请求异常，状态码' + str(r.status_code))
                # time.sleep(10)
                # get_info()

            except Exception as e:
                print(e)




    def start(self,sumthread,sumget,URL2,param):
        threads = []
        n_t=1
        for i in range(sumthread):
            threads.append(threading.Thread(target=Multi_thread.get_info(sumget,i,URL2,param),args=()))

        for t in threads:
            #time.sleep(0.3)
            t.start()
        for t in threads:
            t.join()
    def statistics(self,sumthread, sumget,URL2,param):
        Multi_thread.start(sumthread, sumget,URL2,param)
        print('请求通过次数：',len(Pass))
        print('请求异常次数：',len(Fail))
        print('总响应最大时长：', max(restime))
        print('总响应最小时长：', min(restime))
        print('总响应时长：', sum(restime))
        print('平均响应时长：', sum(restime) / len(restime))


        if (len(Fail))==0:
            print(str(sumthread)+'个线程，每个线程压力请求'+str(sumget)+'次,共计'+str(sumthread*sumget)+'次，没有请求异常')
        else:
            print('存在'+str(len(Fail))+'个，请求异常')
            print(Fail)

if __name__ == '__main__':
    Multi_thread=Multi_thread()
    URL2 = "http://59.202.115.11/gateway/api/001008005007001/dataSharing/2MW316cQ4lf823za.htm?appKey=%33%32%38%32%37%65%65%65%62%66%31%32%34%35%37%33%39%37%33%63%37%66%30%65%37%34%32%63%34%64%37%34&sign=%66%38%39%63%37%39%66%31%31%32%64%65%34%63%62%62%63%30%33%66%64%36%66%61%30%63%61%33%30%35%36%38&requestTime=%31%35%37%37%31%35%36%36%34%39%37%30%33&additional=%7B%22%70%6F%77%65%72%4D%61%74%74%65%72%73%22%3A%22%E7%BB%99%E4%BB%98%2D%30%30%30%30%37%2D%30%30%30%22%2C%22%73%75%62%50%6F%77%65%72%4D%61%74%74%65%72%73%22%3A%22%E7%BB%99%E4%BB%98%2D%30%30%30%30%37%2D%30%31%39%22%2C%22%61%63%63%65%73%73%63%61%72%64%49%64%22%3A%22%73%6A%67%6C%22%2C%22%6D%61%74%65%72%69%61%6C%4E%61%6D%65%22%3A%22%E5%9F%BA%E6%9C%AC%E5%8C%BB%E7%96%97%E4%BF%9D%E9%99%A9%E5%8F%82%E4%BF%9D%E4%BA%BA%E5%91%98%E5%8C%BB%E7%96%97%E8%B4%B9%E7%94%A8%E9%9B%B6%E6%98%9F%E6%8A%A5%E9%94%80%22%2C%22%73%70%6F%6E%73%6F%72%4E%61%6D%65%22%3A%22%E5%A4%A7%E6%95%B0%E6%8D%AE%E7%AE%A1%E7%90%86%E4%B8%AD%E5%BF%83%22%7D&uniscId=%39%31%33%33%30%35%32%32%35%38%35%30%31%37%37%38%58%36"
    param = {'type' : 'zhongtong' , 'postid' :'73116039505988' }  #参数
    sumthread=50 #线程数
    sumget=10  #每个线程请求次数
    
    Multi_thread.statistics(sumthread, sumget,URL2,param)
    input('Press Enter to exit...')