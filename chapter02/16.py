#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
同様の処理をsplitコマンドで実現せよ．
"""

import sys
import math

def split(input_file, n):
    l = [line.strip() for line in input_file.readlines()]
    total = len(l)
    unit = math.ceil(total/n)
    result = [l[x:x+unit] for x in range(0, total,unit)]

    for i, line in enumerate(result):
        with open('split{}.txt'.format(i), 'w') as f:
            f.writelines(line)

def main():
    with open(sys.argv[1], 'r') as f:
        split(f, int(sys.argv[2]))

if __name__ == "__main__":
    main()
