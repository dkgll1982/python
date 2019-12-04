#参考链接：https://blog.csdn.net/kaikai136412162/article/details/90813588
"""
实时语音识别测试
"""
import time
import speech_recognition as sr
import logging
logging.basicConfig(level=logging.DEBUG)
from aip import AipSpeech
 
#filename = './audio/test.wav'
 
BAIDU_APP_ID = '17680061'
BAIDU_API_KEY = 'CXlUYNeSxyhlpvMIqFVZCPVD'
BAIDU_SECRET_KEY = 'WmGA8wA5yMAfLjH09ayU4FntiwWuubZI'
aip_speech = AipSpeech(BAIDU_APP_ID, BAIDU_API_KEY, BAIDU_SECRET_KEY)
 
r = sr.Recognizer()
# 麦克风
mic = sr.Microphone(sample_rate=16000)
while True:
    logging.info('录音中...')
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    logging.info('录音结束，识别中...')
 
    start_time = time.time()
    print(type(audio))
    audio_data = audio.get_wav_data()
    print(type(audio_data))
    # 识别本地文件
    ret = aip_speech.asr(audio_data, 'wav', 16000, {'dev_pid': 1536, })
    print(ret)
    if ret and ret['err_no'] == 0:
        result = ret['result'][0]
        print(result)
        end_time = time.time()
        print(end_time - start_time)
    else:
        print(ret['err_msg'])
    logging.info('end')
 