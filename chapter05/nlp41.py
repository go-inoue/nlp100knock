#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
41. 係り受け解析結果の読み込み（文節・係り受け）
40に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．
第5章の残りの問題では，ここで作ったプログラムを活用せよ．
'''

from nlp40 import Morph

class Chunk:
    def __init__(self):
        self.morphs = []
        self.dst = 0
        self.srcs = []

    def surfaces(self):
        surfaces = [morph.surface for morph in self.morphs if morph.pos != '記号']
        return surfaces

    def hasNoun(self):
        return any([morph.pos =='名詞' for morph in self.morphs])

    def hasVerb(self):
        return any([morph.pos =='動詞' for morph in self.morphs])

    def hasSahen(self):
        return any([self.morphs[i].pos == 'サ変接続' and self.morphs[i+1].surface == 'を' for i in range(len(self.morphs)-1)])
def readChunk():
    with open('./neko.txt.cabocha', 'r') as f:
        chunk, sent, sents = [], [], []
        lines = f.readlines()
        for i in range(len(lines)):
            if lines[i-1][0] == '*':
                c = Chunk()
                c.dst = int(lines[i-1].split(' ')[2].strip('D'))
            if lines[i] == 'EOS\n' or lines[i][0] =='*':
                if chunk:
                    c.morphs = chunk
                    sent.append(c)
                    chunk = []
                if lines[i] == 'EOS\n':
                    if sent:
                        sents.append(sent)
                        for k, j in enumerate(sent):
                            dst_k = sent[k].dst
                            if dst_k != -1:
                                sent[dst_k].srcs.append(k)
                        sent = []
            else:
                surface, features = lines[i].split('\t')
                feature_list = features.split(',')
                morph = Morph(surface, feature_list[6], feature_list[0], feature_list[1])
                chunk.append(morph)

    return sents

if __name__ == "__main__":
    sents = readChunk()
    for i,j in enumerate(sents[5]):
        morphs = [morph.surface for morph in j.morphs]
        if j.dst == -1:
            j.dst = None
        print('Chunk:{} {}---> Chunk:{}'.format(i,''.join(morphs), j.dst))
