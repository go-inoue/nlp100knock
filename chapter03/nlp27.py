#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
27. 内部リンクの除去
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．
'''
import re

def removeLink(text):
    enpha_reg = '\'{2,5}'
    link_reg = '(\[\[)([^\|\#\n\]]+)(.*?)(\]\])'
    text = re.sub(enpha_reg, '', text)
    text = re.sub(link_reg, '\2', text)
    return text

def template():
    text_reg = re.compile('({{基礎情報 国\n)((.\n*)*)(\n}})')
    line_reg = re.compile('^(.+) = ((.\n*)+)')

    with open('UK.txt', 'r') as f:
        info_dict = dict()
        text = re.search(text_reg, f.read()).group(2)
        for li in text.split('\n|'):
            pattern = re.search(line_reg, li)
            if pattern:
                info_dict[pattern.group(1)] = removeLink(pattern.group(2))
        return info_dict

if __name__ == '__main__':
    temp_dict = template()
    for k,v in temp_dict.items():
        print('{}:{}'.format(k,v))
