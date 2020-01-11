import requests        #导入requests包
import json
def get_translate_date(word=None):
    url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
        "cookie":"BAIDUID=6326DBD1EB010DD85AEDD544210482FF:FG=1; PSTM=1553591829; BIDUPSID=92C83AEDC037E73DCF8ED13A0C1C380F; H_WISE_SIDS=132694_125704_114553_132819_132654_131777_128069_131676_132688_125580_132799_120153_132286_132910_132460_132718_132713_131247_132440_130762_132393_132379_132326_132213_131518_132261_118893_118869_131402_118840_118821_118802_131649_131577_132840_131533_131530_132873_131295_131872_132604_131391_129565_107315_131796_132590_130124_132638_131873_132709_131196_132565_131241_132890_129650_127024_132558_132538_131036_131905_132294_132551_131045_132308_132495_129646_130826_131423_132039_131445_110085_131570_127969_131506_123289_131749_131297_128201_131550_131831_131750_132725_132652_132198_132710; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; MCITY=-218%3A294%3A; BDUSS=dlRHVsQ2NWflpKQWlaSWFCbDBTSmpTUTI1NjNxMjBlZktCYzNucXNJczltaEJlSVFBQUFBJCQAAAAAAAAAAAEAAAAfo-IAZGtnbGwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD0N6V09DeldRW; APPGUIDE_8_2_2=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=6; H_PS_PSSID=1422_21081_30210_30472_26350; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1576228382,1578131436,1578131872,1578624034; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1578624034; __yjsv5_shitong=1.0_7_0f03ee8fa96b9f31c0cd9b21a92233a1e551_300_1578624035122_119.97.241.74_4db015a4; yjs_js_security_passport=1f0e9a57d4eb6719bfafd13864eadbea16245ef1_1578624037_js; to_lang_often=%5B%7B%22value%22%3A%22yue%22%2C%22text%22%3A%22%u7CA4%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D"
    }
    From_data = {'from':'zh',
                'to':'en',
                'query':'单独',
                'transtype':'translang',
                'simple_means_flag':'3',
                'sign':'296944.25793',
                'token':'ac8369b506f082ccb886ec0e6c7f415c'}
    #请求表单数据
    response = requests.post(url,data=From_data,headers = headers)
    #将Json格式字符串转字典 
    content = json.loads(response.text)
    #print(content)
    #打印翻译后的数据
    print(content['dict_result']['simple_means']['word_means'])
if __name__=='__main__':
    get_translate_date()