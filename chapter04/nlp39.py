#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
39. Zipfの法則
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
"""

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from nlp30 import readMecab
from nlp36 import wordFreq

def zipf(sents):
    freq_list = wordFreq(sents)
    X = [x[1] for x in freq_list]
    rank = list(range(1, len(freq_list)+1))

    fp = FontProperties(fname='./ipag.ttf')
    plt.title('ZipFの法則',fontproperties=fp)
    plt.xlabel('単語の出現頻度順位', fontproperties=fp)
    plt.ylabel('出現頻度', fontproperties=fp)
    plt.xscale('log')
    plt.yscale('log')
    plt.plot(X, rank)
    plt.show()

if __name__ == "__main__":
    sents = readMecab()
    zipf(sents)
