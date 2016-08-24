#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
'''

import re

def section():
    sec = re.compile(r'(File|ファイル):(.+\.[a-zA-Z\d]+)\|')
    with open('UK.txt', 'r') as f:
        for line in f.readlines():
            s = re.search(sec, line)
            if s:
                print(s.group(2))

if __name__ == '__main__':
    section()
