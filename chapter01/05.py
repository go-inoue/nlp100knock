#!/usr/bin env python
# -*- coding: utf-8 -*-
'''
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
'''

def n_gram(sequence, n, word=True):
    start, end = '<S>', '</S>'
    n_gram_list = []

    if word:
        sequence = sequence.split()
    else:
        sequence = list(sequence)

    sequence.insert(0,start)
    sequence.append(end)

    n_gram_list = list(zip(*[sequence[i:] for i in range(n)]))

    return n_gram_list

if __name__ == "__main__":
    string = "I am an NLPer"
    print("word:", n_gram(string, 2))
    print("character:", n_gram(string, 2, False))
