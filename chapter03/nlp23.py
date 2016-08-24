#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
'''

import re

def section():
    sec = re.compile('(=+ *)([^= ]*)( *=+)')
    with open('UK.txt', 'r') as f:
        for line in f.readlines():
            s = re.match(sec, line)
            if s:
                print('Section: {}, Level: {}'.format(s.group(2),len(s.group(1))-1))

if __name__ == '__main__':
    section()
