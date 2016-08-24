#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
55. 固有表現抽出

入力文中の人名をすべて抜き出せ．
'''
import sys
import re

def NERer(filename):
    output, tmp = [], []

    WORD = re.compile(r'<word>(.+)</word>')
    NER = re.compile(r'<NER>(.+)</NER>')

    for line in filename.readlines():
        if len(tmp) == 0:
            word = WORD.search(line.strip())
            if word:
                tmp.append(word.group(1))
        elif len(tmp) == 1:
            ner = NER.search(line.strip())
            if ner:
                tmp.append(ner.group(1))
                output.append(tmp)
                tmp = []
    return [name[0] for name in output if name[1] == 'PERSON']

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        for line in NERer(f):
            print(line)
