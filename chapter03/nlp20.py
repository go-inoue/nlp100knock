#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
問題21-29では，ここで抽出した記事本文に対して実行せよ．
'''

import json
import re

def readJson():
    keyword = re.compile('イギリス')
    with open('jawiki-country.json', 'r') as f, open('UK.txt', 'w') as o:
        for line in f.readlines():
            data = json.loads(line)
            if re.search(keyword, data['title']):
                o.write(data['text'])

if __name__ == '__main__':
    readJson()
