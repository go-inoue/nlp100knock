#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
"""

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from nlp30 import readMecab
from nlp36 import wordFreq

def histogram(sents):
    freq_list = wordFreq(sents)
    X = [x[1] for x in freq_list]

    fp = FontProperties(fname='./ipag.ttf')
    plt.title('ヒストグラム',fontproperties=fp)
    plt.xlabel('出現頻度', fontproperties=fp)
    plt.ylabel('単語種類数', fontproperties=fp)
    plt.hist(X, bins=100, range=(0,100))
    plt.show()

if __name__ == "__main__":
    sents = readMecab()
    histogram(sents)
