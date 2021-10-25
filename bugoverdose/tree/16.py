# 문자열 집합 (https://www.acmicpc.net/problem/14425)

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

strings = {}
for _ in range(N):
    cur_dic = strings
    for letter in list(input()):
        if letter not in cur_dic.keys():
            cur_dic[letter] = {}
        cur_dic = cur_dic[letter]    

counter = 0
for _ in range(M):
    exists = True
    cur_dic = strings
    for letter in list(input()):
        if letter not in cur_dic.keys():
            exists = False
            break
        cur_dic = cur_dic[letter]
    if exists:
        if cur_dic == {}:
            counter += 1

print(counter)

#  =================================================================
# 5 11
# baekjoononlinejudge
# startlink
# codeplus
# sundaycoding
# codingsh
# baekjoon
# codeplus
# codeminus
# startlink
# starlink
# sundaycoding
# codingsh
# codinghs
# sondaycoding
# startrink
# icerink

# 4
#  =================================================================