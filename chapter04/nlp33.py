#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
33. サ変名詞
サ変接続の名詞をすべて抽出せよ．
"""
from nlp30 import readMecab

def nounSahen(sents):
    noun_sahen = []
    for sent in sents:
        for morph in sent:
            if morph['pos1'] in 'サ変接続':
                noun_sahen.append(morph['surface'])
    return noun_sahen

if __name__ == "__main__":
    sents = readMecab()
    print(nounSahen(sents))
