from pypinyin import Style, pinyin, load_phrases_dict
# 官方文档：https://pypi.org/project/pypinyin/#id5

print(pinyin('行走'),pinyin('行伍出身'))
print(pinyin('朝阳'),pinyin('朝向'))
print(pinyin('螳臂当车'),pinyin('安步当车'))

# 词语中的多音字拼音有误？
# 目前是通过词组拼音库的方式来解决多音字问题的。如果出现拼音有误的情况， 可以自定义词组拼音来调整词语中的拼音：
print(pinyin('步履蹒跚'))
load_phrases_dict({'步履蹒跚': [['bù'], ['lǚ'], ['mán'], ['shān']]})
print(pinyin('步履蹒跚'))
print(pinyin('下雨天'))
