#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
42. 係り元と係り先の文節の表示
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
'''

from nlp41 import readChunk

def srcsDst(sents):
    result = []
    for sent in sents:
        for chunk in sent:
            for src in chunk.srcs:
                src_chunk = ''.join(sent[src].surfaces())
                dst_chunk = ''.join(sent[sent[src].dst].surfaces())
                tmp = src_chunk + '\t' + dst_chunk
                result.append(tmp)
    return result

if __name__ == "__main__":
    sents = readChunk()
    for i in srcsDst(sents):
        print(i)
