#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
確認にはheadコマンドを用いよ．
"""

import sys

def start2n(input_file, n):
    while n > 0:
        print(input_file.readline(), end="")
        n -= 1

def main():
    with open(sys.argv[1], 'r') as f:
        start2n(f, int(sys.argv[2]))

if __name__ == "__main__":
    main()
