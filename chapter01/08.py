'''
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
    英小文字ならば(219 - 文字コード)の文字に置換
    その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
'''

import re

def cipher(string):
    code = []
    pattern = re.compile('[a-z]')
    for c in string:
        if pattern.match(c):
            code.append(chr(219 - ord(c)))
        else:
            code.append(c)
    return "".join(code)    

if __name__ == "__main__":
    string = 'This is a secret message.'
    print('Original sentence:\t{}'.format(string))
    print('Encrypted sentence:\t{}'.format(cipher(string)))
    print('Decrypted sentence:\t{}'.format(cipher(cipher(string))))
