#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
確認にはcutコマンドを用いよ．
"""

import sys

def divide(file):
    with open('col1.txt', 'w') as f, open('col2.txt', 'w') as f2:
        for line in file:
            col = line.split('\t')
            f.write(col[0] + '\n')
            f2.write(col[1] + '\n')

def main():
    with open(sys.argv[1]) as f:
        divide(f)

if __name__ == "__main__":
    main()
