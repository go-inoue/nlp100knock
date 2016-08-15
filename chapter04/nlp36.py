#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""
from nlp30 import readMecab

def wordFreq(sents):
    freq_dict = dict()
    for sent in sents:
        for morph in sent:
            if morph['surface'] in freq_dict:
                freq_dict[morph['surface']] += 1
            else:
                freq_dict[morph['surface']] = 1
    return sorted(freq_dict.items(), key=lambda x:x[1], reverse=True)

if __name__ == "__main__":
    sents = readMecab()
    print(wordFreq(sents)[:50])
