#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
53. Tokenization

Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．
'''
import sys
import re

def tokenize(filename):
    output = []
    pattern = re.compile(r'<word>(.+)</word>')
    for line in filename.readlines():
        word = pattern.search(line.strip())
        if word:
            output.append(word.group(1))
    return output

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        for line in tokenize(f):
            print(line)
