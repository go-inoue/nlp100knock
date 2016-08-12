#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
確認にはtailコマンドを用いよ．
"""

import sys

def end2n(f, n):
    lines = f.readlines()
    for i in range(len(lines)-n, len(lines)):
        print(lines[i], end="")

def main():
    with open(sys.argv[1], 'r') as f:
        end2n(f, int(sys.argv[2]))

if __name__ == "__main__":
    main()
