#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""
from nlp30 import readMecab

def nounCompound(sents):
    noun_compound, tmp = [], []
    for sent in sents:
        for morph in sent:
            if morph['pos'] == '名詞':
                tmp.append(morph['surface'])
            else:
                if len(tmp) > 1:
                    noun_compound.append(''.join(tmp))
                tmp = []

    return noun_compound

if __name__ == "__main__":
    sents = readMecab()
    print(nounCompound(sents))
