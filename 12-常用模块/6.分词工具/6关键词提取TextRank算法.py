import jieba
import jieba.analyse
sentence = """
地灵殿的主人。
虽然地底都市已经被排除在地狱之外，但那些曾经是地狱设施的遗迹里
依然还残留着无数充满怨念的灵们，因而必须有人对他们进行管理。
在灼热地狱遗址上建立起了地灵殿，她就在那里居住了下来。
因为她能够读取他人心中的想法，不管是任何妖怪，怨灵都为之感到恐惧，
不知从何时起几乎没有人再来地灵殿造访了。
但是，相反因为能读心而受到那些不会说话的动物们的喜爱，地灵殿逐渐
变成了充满火焰猫，地狱鸦等宠物们的房屋。
因为宠物的增多结果导致灼热地狱遗迹无法完美的管理，最后只得把很多
管理事项交由宠物们去做。
把宠物的管理交给宠物去做。
把庭院的修缮交给宠物去做。
把陪妹妹玩的工作交给宠物去做，如此。
但是，突然出现不应该出现的地上的人类，在听说怨灵和间歇泉异变
之后她大吃一惊。
怨灵的管理她交由阿燐去做，灼热地狱的火力调节则交给了阿空。
她们应该都是忠心于觉不会做什么坏事才对。她相信决不会发生
什么异变才对。
搞不好，也许是眼前这个人类撒谎有什么别的企图，她这么想着。
读了那人类心中的想法之后，她又吃了一惊。
她们的心中，几乎没有任何关于怨灵和间歇泉的情报。
觉诧异了，她决定先试探一下她们。
"""
for x in jieba.analyse.textrank(sentence, withWeight=True):
    """
    接收参数如下,和extract_tags参数一致，但allowPOS默认值不会空：
    sentence：句子
    topK：返回几个 TF/IDF 权重最大的关键词，默认值为20
    withWeight：是否一并返回关键词权重值，默认值为 False
    allowPOS：仅包括指定词性的词，默认值不为空
    """
    print(x)
"""
('宠物', 1.0)
('地狱', 0.8169410022497963)
('管理', 0.7111631257164159)
('怨灵', 0.6872520018950034)
('交给', 0.5766849288790858)
('不会', 0.5671709845112852)
('地灵', 0.5418423145115177)
('人类', 0.4235967140492308)
('怨念', 0.40976053284203795)
('遗迹', 0.3890312542892664)
('出现', 0.38728082208337444)
('异变', 0.3678994864195963)
('间歇泉', 0.3523723288507097)
('导致', 0.3217237709168045)
('读心', 0.3193653873378865)
('受到', 0.29192544019397326)
('听说', 0.2910761395893028)
('说话', 0.28670968889003423)
('动物', 0.28639826197065527)
('试探', 0.2805685960379144)
"""