#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
確認にはcut, uniq, sortコマンドを用いよ．
"""

import sys

def freq(f):
    lines = f.readlines()
    col = [line.split('\t')[0] for line in lines]
    f_dict = {word:col.count(word) for word in col}
    sorted_dict = sorted(f_dict.items(), key=lambda x:x[1], reverse=True)
    return sorted_dict

def main():
    with open(sys.argv[1], 'r') as f:
        for k,v in freq(f):
            print(v, k)

if __name__ == "__main__":
    main()
