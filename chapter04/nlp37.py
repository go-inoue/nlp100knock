#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
37. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
"""
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from nlp30 import readMecab
from nlp36 import wordFreq

def top10(sents):
    top_10 = wordFreq(sents)[:10]
    X = [x[0] for x in top_10]
    Y = [y[1] for y in top_10]

    fp = FontProperties(fname='./ipag.ttf')
    plt.title('頻度上位10語',fontproperties=fp)
    plt.xlabel('単語', fontproperties=fp)
    plt.ylabel('頻度', fontproperties=fp)
    plt.bar(range(10), Y, align="center")
    plt.xticks(range(10), X, fontproperties=fp)
    plt.show()

if __name__ == "__main__":
    sents = readMecab()
    top10(sents)
