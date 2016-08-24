#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
'''

import re

def categoryName():
    cat = re.compile('\[\[Category:(.+)\]\]')
    with open('UK.txt', 'r') as f:
        for line in f.readlines():
            s = re.search(cat, line)
            if s:
                print(s.group(1).strip('|*'))

if __name__ == '__main__':
    categoryName()
