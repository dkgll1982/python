import jieba 
 
seg_list1 = jieba.cut("今天下雨我骑车差点摔倒了好在我一把把把把住了")
seg_list2 = jieba.cut('我想过过儿过过的生活')
print(", ".join(seg_list1))
print(", ".join(seg_list2)) 
 
print('*'*40)

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式
 
seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
 
seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print(", ".join(seg_list))
 
seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print(", ".join(seg_list))
# ————————————————
# 版权声明：本文为CSDN博主「请叫我算术嘉」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/ssjdoudou/java/article/details/84142602