import emoji

import re

def filter_emoji(desstr,restr=''):
    '''
    过滤表情
    '''
    try:
        co = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return co.sub(restr, desstr)

print(emoji.emojize('Python is :thumbs_up:')) 
print(emoji.emojize('Python is :four_leaf_clover:')) 
print(emoji.emojize('Python is :thumbsup:', use_aliases=True)) 
print(emoji.demojize('Python is 👍🍀')) 
print(filter_emoji('这是👍🍀方法'))