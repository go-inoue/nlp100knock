#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
32. 動詞の原形
動詞の原形をすべて抽出せよ．
"""
from nlp30 import readMecab

def verbBase(sents):
    verb_surface = []
    for sent in sents:
        for morph in sent:
            if morph['pos'] in '動詞':
                verb_surface.append(morph['base'])
    return verb_surface

if __name__ == "__main__":
    sents = readMecab()
    print(verbBase(sents))
