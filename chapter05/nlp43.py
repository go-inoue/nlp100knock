#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
43. 名詞を含む文節が動詞を含む文節に係るものを抽出
名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
'''

from nlp41 import readChunk

def noun2verb(sents):
    result = []
    for sent in sents:
        for chunk in sent:
            for src in chunk.srcs:
                if sent[src].hasNoun() and sent[sent[src].dst].hasVerb():
                    src_chunk = ''.join(sent[src].surfaces())
                    dst_chunk = ''.join(sent[sent[src].dst].surfaces())
                    tmp = src_chunk + '\t' + dst_chunk
                    result.append(tmp)
    return result

if __name__ == "__main__":
    sents = readChunk()
    for i in noun2verb(sents):
        print(i)
