# 행렬 곱셈 (https://www.acmicpc.net/problem/2740)

import sys

input = sys.stdin.readline

r1, c1 = map(int, input().split())
A = []
for _ in range(r1):
    A.append(list(map(int, input().split())))

r2, c2 = map(int, input().split())
B = []
for _ in range(r2):
    B.append(list(map(int, input().split())))

prod = [[0]*c2 for _ in range(r1)]

for y in range(r1):
    for x in range(c2):
        cur_sum = 0
        for idx in range(c1):
            prod[y][x] += A[y][idx] * B[idx][x]

for p in prod:
    print(" ".join(map(str, p)))
        
# =================================================================