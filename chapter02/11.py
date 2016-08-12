#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
'''
import sys

def tab2space(file):
    with open('tab2space_' + sys.argv[1], 'w') as f:
        for line in file:
            f.write(line.replace('\t', ' '))

def main():
    with open(sys.argv[1]) as f:
        tab2space(f)

if __name__ == "__main__":
    main()

# sed -e "s/    / /g" hightemp.txt > tab2space_sed_hightemp.txt
# cat hightemp.txt | tr "\t" " " > tab2space_tr_hightemp.txt
# expand -t 1 hightemp.txt > tab2space_expand_hightemp.txt
