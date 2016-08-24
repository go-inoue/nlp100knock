#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
51. 単語の切り出し

空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ．
'''
from nlp50 import sentenceSplit

def trimWord(sents):
    output = ''
    for sent in sents.split('\n'):
        output += '\n'.join(sent.split(' ')) + '\n\n'
    return output[:-2]

if __name__ == "__main__":
    sents = sentenceSplit()
    print(trimWord(sents))
