'''
06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
'''

string_1 = 'paraparaparadise'
string_2 = 'paragraph'

X = set(n_gram(string_1,2,'char'))
Y = set(n_gram(string_2,2,'char'))

print(X|Y)
print(X&Y)
print(X-Y)

print('"se" in X:',('s','e') in X) 
print('"se" in Y:',('s','e') in Y) 
