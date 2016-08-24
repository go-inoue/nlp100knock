#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
54. 品詞タグ付け

Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．
'''
import sys
import re

def tokenize(filename):
    output, tmp = [], []

    WORD = re.compile(r'<word>(.+)</word>')
    LEMMA = re.compile(r'<lemma>(.+)</lemma>')
    POS = re.compile(r'<POS>(.+)</POS>')

    for line in filename.readlines():
        if len(tmp) == 0:
            word = WORD.search(line.strip())
            if word:
                tmp.append(word.group(1))
        elif len(tmp) == 1:
            lemma = LEMMA.search(line.strip())
            if lemma:
                tmp.append(lemma.group(1))
        elif len(tmp) == 2:
            pos = POS.search(line.strip())
            if pos:
                tmp.append(pos.group(1))
                output.append('\t'.join(tmp))
                tmp = []
    return output

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        for line in tokenize(f):
            print(line)
