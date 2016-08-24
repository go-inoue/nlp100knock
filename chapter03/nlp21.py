#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
'''

import re

def categoryLine():
    cat = re.compile('\[\[Category:(.+)\]\]')
    with open('UK.txt', 'r') as f:
        for line in f.readlines():
            if re.search(cat, line):
                print(line.strip())

if __name__ == '__main__':
    categoryLine()
