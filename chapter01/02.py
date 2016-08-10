'''
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
'''

string_1 = 'パトカー'
string_2 = 'タクシー'
string_3 = ''

for (a, b) in zip(string_1, string_2):
    string_3 += ''.join(a+b)

print(string_3)
