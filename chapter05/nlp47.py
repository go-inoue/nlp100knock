#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
47. 機能動詞構文のマイニング
動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．
46のプログラムを以下の仕様を満たすように改変せよ．
*「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
*述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
*述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
*述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，以下の出力が得られるはずである．

返事をする      と に は        及ばんさと 手紙に 主人は

このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．
*コーパス中で頻出する述語（サ変接続名詞+を+動詞）
*コーパス中で頻出する述語と助詞パターン
'''
from nlp41 import readChunk

def functionalVerbs(sents):
    result, src_chunks = [], []
    for sent in sents:
        for chunk in sent:
            if chunk.hasVerb():
                verb = [morph.base for morph in chunk.morphs if morph.pos == '動詞'][0]
                sahen = ''
                for src in chunk.srcs:
                    if len(sent[src].morphs) > 1:
                        if sent[src].morphs[-2].pos1 == 'サ変接続' and sent[src].morphs[-1].surface == 'を':
                            sahen = sent[src]
                if sahen:
                    verb = ''.join(sahen.surfaces()) + verb
                    for src in chunk.srcs:
                        tmp = [[morph.surface, sent[src]] for morph in sent[src].morphs if morph.pos =='助詞' and sent[src] != sahen]
                        if tmp:
                            src_chunks.append(tmp[-1])
                    if src_chunks:
                        src_chunks = sorted(src_chunks, key=lambda x:x[0])
                        parts, chunk = [], []
                        for item in src_chunks:
                            parts.append(item[0])
                            chunk.append(''.join(item[1].surfaces()))
                    if parts:
                        result.append([verb, parts, chunk])
                        src_chunks, parts, chunk = [], [], []
    #return result
    return [l[0] + '\t' + ' '.join(l[1]) + '\t' +' '.join(l[2]) + '\n' for l in result]


if __name__ == "__main__":
    sents =readChunk()
    with open('nlp47.txt', 'w') as f:
        f.writelines(functionalVerbs(sents))
