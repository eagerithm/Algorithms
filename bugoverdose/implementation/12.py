# Encryption (https://www.hackerrank.com/challenges/encryption/problem?h_r=next-challenge&h_v=zen)
# 경계값 설정

words = list(input().split())
sentence = ""
for word in words:
    sentence += word

min_len = int(len(sentence) ** 0.5)

max_len = min_len
if len(sentence)/min_len > min_len:
    max_len += 1

if max_len * min_len < len(sentence):
    min_len += 1

answers = [""]*max_len

for row in range(min_len):
    start = row*max_len
    end = (row+1)*max_len
    cut = sentence[start:end]
    for col in range(len(cut)):
        answers[col] += cut[col]

print(" ".join(answers))

#  =================================================================