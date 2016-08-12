#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
確認にはpasteコマンドを用いよ．
"""

import sys

def merge():
    with open('col1.txt', 'r') as f, open('col2.txt', 'r') as f2, open('merged.txt', 'w') as m:
        for (a, b) in zip(f,f2):
            m.write(a.strip('\n') + '\t' + b)

if __name__ == "__main__":
    merge()
