#!/bin/bash
echo '*コーパス中で頻出する述語と格パターンの組み合わせ'
grep '^する\t' nlp45.txt | sort | uniq -c | sort -r | head -10

echo '*「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）'
grep '^する\t\|^見る\t\|^与える\t' nlp45.txt | sort | uniq -c | sort -r | head -10
