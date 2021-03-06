#!/usr/bin env python
# -*- coding: utf-8 -*-
'''
04. 元素記号
"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
'''

import re

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

pattern = re.compile('[.,]')

tokens = sentence.split(' ')
words = []
for w in tokens:
    w = pattern.sub('',w)
    words.append(w)

d = {}
for (i, w) in enumerate(words):
    if i+1 in [1,5,6,7,8,9,15,16,19]:
        index = 1
    else:
        index = 2
    d[w[:index]] = i+1

print(d)
