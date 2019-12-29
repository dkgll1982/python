#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-26 00:04
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 1.例子.py
# @Software: PyCharm

import sys
from PyQt5.QtWidgets import QWidget, QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.show()
    w.setWindowTitle("Hello PyQt5")
    sys.exit(app.exec_())