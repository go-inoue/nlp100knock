#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
50. 文区切り
(. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，入力された文書を1行1文の形式で出力せよ．
'''
import re

def sentenceSplit():
    with open('./nlp.txt', 'r') as f:
        output = ''
        pattern = re.compile('(?P<end>[\.;:\?!]) (?P<start>[A-Z])')
        for line in f.readlines():
            if line != '\n':
                output += pattern.sub('\g<end>\n\g<start>', line.strip())
    return output

if __name__ == "__main__":
    sents = sentenceSplit()
    print(sents)
