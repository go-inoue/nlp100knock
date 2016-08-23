#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
40. 係り受け解析結果の読み込み（形態素）
形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
'''

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

def readMorph():
    with open('./neko.txt.cabocha', 'r') as f:
        sent, sents = [], []
        for line in f.readlines():
            if line != 'EOS\n' and line[0] != '*':
                surface, features = line.split('\t')
                feature_list = features.split(',')
                morph = Morph(surface, feature_list[6], feature_list[0], feature_list[1])
                sent.append(morph)
            elif line == 'EOS\n':
                if sent:
                    sents.append(sent)
                sent = []
    return sents

if __name__ == "__main__":
    sents = readMorph()
    print([morph.surface for morph in sents[2]])
