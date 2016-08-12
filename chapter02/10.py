#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
'''

import sys

def count(file):
    count = 0
    for line in file:
        count += 1
    return count

def main():
    with open(sys.argv[1], 'r') as f:
        print(count(f))

if __name__ == "__main__":
    main()
