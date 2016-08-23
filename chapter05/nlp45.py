#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
45. 動詞の格パターンの抽出

今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい．
動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ．
ただし，出力は以下の仕様を満たすようにせよ．

*動詞を含む文節において，最左の動詞の基本形を述語とする
*述語に係る助詞を格とする
*述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる

「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える．
この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

始める  で
見る    は を

このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

 *コーパス中で頻出する述語と格パターンの組み合わせ
*「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
'''
from nlp41 import readChunk

def casePattern(sents):
    result, parts = [], []
    for sent in sents:
        for chunk in sent:
            if chunk.hasVerb():
                verb = [morph.base for morph in chunk.morphs if morph.pos == '動詞'][0]
                for src in chunk.srcs:
                    tmp = [morph.surface for morph in sent[src].morphs if morph.pos == '助詞']
                    if tmp:
                        parts.append(tmp[-1])
                if parts:
                    result.append([verb, sorted(parts)])
                    parts = []
    return [l[0] + '\t' + ' '.join(l[1]) + '\n' for l in result]

if __name__ == "__main__":
    sents =readChunk()
    with open('nlp45.txt', 'w') as f:
        f.writelines(casePattern(sents))
