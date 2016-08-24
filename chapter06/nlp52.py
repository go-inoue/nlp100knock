#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
52. ステミング

51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，単語と語幹をタブ区切り形式で出力せよ．
Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．
'''
from nltk.stem.porter import PorterStemmer
from nlp50 import sentenceSplit
from nlp51 import trimWord

def stemWord(words):
    output = ''
    for word in words.split('\n'):
        stemmer = PorterStemmer()
        output += '%s\t%s' % (word, stemmer.stem(word)) + '\n'
    return output[:-2]

if __name__ == "__main__":
    sents = sentenceSplit()
    words = trimWord(sents)
    print(stemWord(words))
