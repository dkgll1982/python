#!/usr/bin/env python
#encoding:utf8

import itertools
import random

cardNum = []                    # 存放随机牌组
listSet = []                    # 存放随机牌组对
cardGroup = ()                  # 调用牌组
symbols = ["+","-","*","/"]
cardOne = 0 ; cardTwo = 0 ; cardThr = 0 ;cardFor = 0     # 存放卡牌信息
resultOne = 0 ; resultTwo = 0 ; resultThr = 0            # 存放运算计算结果
cardValue = []                  # 保存结果打印信息
cardResult = []

# 发牌器
def cardFun(*kw):
    for x in range(len(kw)):
        cardNum.append(kw[x])
    #for i in range(4):
    #     cardNum.append(int(random.random() * 100 % 13) + 1)
    listSet = list(set(itertools.permutations(cardNum, 4)))
    return listSet         # 存放A(4,4)种排列方式的列表

# 计算用函数
cardList = cardFun(12,2,3,9)
def cardCompute():
    for i in range(len(cardList)):
        cardGroup = cardList[i]
        cardOne = cardGroup[0]
        cardTwo = cardGroup[1]
        cardThr = cardGroup[2]
        cardFor = cardGroup[3]
        flag = False
        # 下面的循环运算体系会有数学上逻辑上的报错，所以用try检测
        try:
            for s1 in symbols:
                resultOne = 0
                if s1 == "+":
                    resultOne = cardOne + cardTwo
                elif s1 == "-":
                    resultOne = cardOne - cardTwo
                elif s1 == "*":
                    resultOne = cardOne * cardTwo
                elif s1 == "/":
                    resultOne = cardOne / cardTwo
                for s2 in symbols:
                    resultTwo = 0
                    if s2 == "+":
                        resultTwo = resultOne + cardThr
                    elif s2 == "-":
                        resultTwo = resultOne - cardThr
                    elif s2 == "*":
                        resultTwo = resultOne * cardThr
                    elif s2 == "/":
                        resultTwo = resultOne / cardThr
                    for s3 in symbols:
                        resultThr =0 ; resultelse = 0
                        if s3 == "+":
                            resultThr = resultTwo + cardFor
                            resultelse = cardThr + cardFor
                        elif s3 == "-":
                            resultThr = resultTwo - cardFor
                            resultelse = cardThr - cardFor
                        elif s3 == "*":
                            resultThr = resultTwo * cardFor
                            resultelse = cardThr * cardFor
                        elif s3 == "/":
                            resultThr = resultTwo / cardFor
                            resultelse = cardThr / cardFor

                        # 判断最终结果是否为24
                        if resultThr == 24:
                            cardValue.append("((%s %s %s) %s %s ) %s %s = 24" % (cardOne,s1,cardTwo,s2,cardThr,s3,cardFor))
                            flag = True
                        # 括号与括号的运算
                        elif resultThr != 24 and 24 % resultOne == 0:
                            for s4 in symbols:
                                resultThr = 0
                                if s4 == "+":
                                    resultThr = resultOne + resultelse
                                elif s4 == "-":
                                    resultThr = resultOne - resultelse
                                elif s4 == "*":
                                    resultThr = resultOne * resultelse
                                elif s4 == "/":
                                    resultThr = resultOne / resultelse
                                if resultThr == 24:
                                    cardValue.append("(%s %s %s) %s (%s %s %s) = 24" % (cardOne,s1,cardTwo,s4,cardThr,s3,cardFor))
                                    flag = True
                                if flag:
                                    break
                    # 如果得到结果，就退出3次运算的循环
                        if flag:
                            break
                    if flag:
                        break
                if flag:
                    break
        except ZeroDivisionError:
            pass

    cardResult = set(cardValue)
    return cardResult

# 执行主体
if __name__ == "__main__":
    Compute = cardCompute()
    print("你手上的卡牌为：%s %s %s %s" % (cardList[0][0],cardList[0][1],cardList[0][2],cardList[0][3]))
    print("这组卡牌共有 %s 种算法" % (len(Compute)))
    print("---" * 10)
    for i in Compute:
        print(i)