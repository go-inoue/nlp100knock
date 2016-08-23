#!/bin/bash
echo '*コーパス中で頻出する述語（サ変接続名詞+を+動詞）をUNIXコマンドを用いて確認'
cat nlp47.txt | cut -f 1| sort | uniq -c | sort -r | head -10

echo '*コーパス中で頻出する述語と助詞パターンをUNIXコマンドを用いて確認'
cat  nlp47.txt | cut -f 1,2 | sort | uniq -c | sort -r | head -10
