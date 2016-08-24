#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
'''

import re

def template():
    text_reg = re.compile('({{基礎情報 国\n\|)((.\n*)*)(\n}})')
    line_reg = re.compile('^(.+) = ((.\n*)+)')

    with open('UK.txt', 'r') as f:
        info_dict = dict()
        text = re.search(text_reg, f.read()).group(2)
        for li in text.split('\n|'):
            pattern = re.search(line_reg, li)
            if pattern:
                info_dict[pattern.group(1)] = pattern.group(2)
        return info_dict

if __name__ == '__main__':
    temp_dict = template()
    for k,v in temp_dict.items():
        print('{}:{}'.format(k,v))
