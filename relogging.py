#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-05 09:32
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : logging
# @Software: PyCharm

import logging  # 引入logging模块
logging.basicConfig(level=logging.NOTSET)  # 设置日志级别
# 将信息打印到控制台上
logging.debug(u"如果设置了日志级别为NOTSET,那么这里可以采取debug、info的级别的内容也可以显示在控制台上了")
logging.debug(u"苍井空")
logging.info(u"麻生希")
logging.warning(u"小泽玛利亚")
logging.error(u"桃谷绘里香")
logging.critical(u"泷泽萝拉")