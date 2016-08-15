#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
30. 形態素解析結果の読み込み  形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

def readMecab():
    with open('neko.txt.mecab', 'r') as f:
        sent, sents = [], []
        for morph in f.readlines():
            if morph != 'EOS\n':
                surface, features = morph.split('\t')
                feature_li = features.split(',')
                base, pos, pos1 = feature_li[6], feature_li[0], feature_li[1] 
                morph_dict = {'surface':surface, 'base':base, 'pos':pos, 'pos1':pos1}
                sent.append(morph_dict)
            else:
                if sent:
                    sents.append(sent)
                sent = []

    return sents

if __name__ == "__main__":
    sents = readMecab()
    print(sents[1:100])
