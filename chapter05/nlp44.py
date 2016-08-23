#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
44. 係り受けの木の可視化
与えられた文の係り受け木を有向グラフとして可視化せよ．
可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
'''
import pydot
from nlp41 import readChunk

def graph(sent):
    edges = []
    for chunk in sent:
        for src in chunk.srcs:
            src_chunk = ''.join(sent[src].surfaces())
            dst_chunk = ''.join(sent[sent[src].dst].surfaces())
            edges.append((src_chunk, dst_chunk))
    g = pydot.graph_from_edges(edges, directed=True)
    g.set_rankdir('LR')
    g.write_jpeg('nlp44.jpg', prog='dot')

if __name__ == "__main__":
    sents =readChunk()
    graph(sents[5])
