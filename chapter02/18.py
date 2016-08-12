#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
"""

import sys

def sort3(f):
    lines = f.readlines()
    l = [line.strip().split('\t') for line in lines]
    sorted_lines = sorted(l, key=lambda x: float(x[2]), reverse=True)
    return sorted_lines

def main():
    with open(sys.argv[1], 'r') as f:
        for i in sort3(f):
            print('\t'.join(i))
if __name__ == "__main__":
    main()
