#!/usr/bin env python
# -*- coding: utf-8 -*-
'''
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
'''

string_1 = 'パトカー'
string_2 = 'タクシー'

print(''.join([a + b for a, b in zip(string_1, string_2)]))
