#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
'''

import re

def removeLink(text):
    enpha_reg = '\'{2,5}'
    int_link = '(\[\[)([^\|\#\n\]]+)(.*?)(\]\])'
    tags = '<.*?>'
    ext_link = '\[.*?\]'
    lang = '\{\{.+?\|.+?\|(.+?)\}\}'
    text = re.sub(enpha_reg, '', text)
    text = re.sub(int_link, '\2', text)
    text = re.sub(tags, '', text)
    text = re.sub(ext_link, '', text)
    text = re.sub(lang, '', text)

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
