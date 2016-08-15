#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
34. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．
"""
from nlp30 import readMecab

def nounPhrase(sents):
    noun_phrase = []
    for sent in sents:
        for i in range(len(sent)-3):
            phrase = sent[i:i+3]
            A = phrase[0]['pos'] == '名詞'
            no = phrase[1]['surface'] == 'の'
            B = phrase[2]['pos'] == '名詞'
            if A and no and B:
                noun_phrase.append(''.join([morph['surface'] for morph in phrase]))
    return noun_phrase

if __name__ == "__main__":
    sents = readMecab()
    print(nounPhrase(sents))
