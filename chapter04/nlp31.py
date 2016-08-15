#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
31. 動詞
動詞の表層形をすべて抽出せよ．
"""
from nlp30 import readMecab

def verbSurface(sents):
    verb_surface = []
    for sent in sents:
        for morph in sent:
            if morph['pos'] in '動詞':
                verb_surface.append(morph['surface'])
    return verb_surface

if __name__ == "__main__":
    sents = readMecab()
    print(verbSurface(sents))
