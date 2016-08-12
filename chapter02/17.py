#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．
確認にはsort, uniqコマンドを用いよ．
"""

import sys

def split(f):
    lines = f.readlines()
    first = [line.split('\t')[0] for line in lines]
    return set(first)

def main():
    with open(sys.argv[1], 'r') as f:
        for i in split(f):
            print(i)
if __name__ == "__main__":
    main()
