# if 后面跟的是条件表达式，条件表达式的结果为True或者False。

# （1）如果if后面的条件是数字，只要这个数字不是0，python都会把它当做True处理，见下面的例子：
if 3:
    print('OK')
if 0:
    print('条件1')
else:
    print('0 是Flase')
# 输出OK，但是如果数字是0，就会被认为是False。
# （2）如果if后面跟的是字符串，则只要这个字符串不为空串，python就把它看作True，参见下例
if 'hehe':
    print('No problem')

if '':
    print('条件2')
else:
    print('空字符')

# （3）1与True，0与False在python来说是完全相等的东西。
if 0 == False:
    print('0 是flase')

if 1 == True:
    print('1是True')
