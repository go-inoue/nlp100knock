#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
48. 名詞から根へのパスの抽出
文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ． ただし，構文木上のパスは以下の仕様を満たすものとする．

*各文節は（表層形の）形態素列で表現する
*パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する

「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

吾輩は -> 見た
ここで -> 始めて -> 人間という -> ものを -> 見た
人間という -> ものを -> 見た
ものを -> 見た
'''
from nlp41 import readChunk

def noun2root(sents):
    result = []
    for sent in sents:
        for chunk in sent:
            dst = int(chunk.dst)
            if dst != -1 and chunk.hasNoun():
                output = ''.join(chunk.surfaces())
                while dst != -1:
                    output += ' -> ' + ''.join(sent[dst].surfaces())
                    result.append(output)
                    dst = int(sent[dst].dst)
    return result

if __name__ == "__main__":
    sents =readChunk()
    for line in noun2root(sents[:10]):
        print(line)
