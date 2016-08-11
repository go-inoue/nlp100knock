#!/usr/bin env python
# -*- coding: utf-8 -*-
'''
09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．
適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
'''

import random

def shuffle(sentence):
    output = []
    for token in sentence.split():
        if len(token) > 4:
            word = []
            inside = list(token[1:-1])       
            random.shuffle(inside)
            output.append(token[0] + ''.join(inside) + token[-1])
        else:
            output.append(token)
    return ' '.join(output)

if __name__ == "__main__":    
    sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(shuffle(sentence))
