# 정수 삼각형 (https://www.acmicpc.net/problem/1932)

# 나의 정답 
import sys
input = sys.stdin.readline

N = int(input())

prev = [0]*N
cur = [0]*N

for _ in range(N):
    values = list(map(int, input().split()))
    length = len(values)
    for idx in range(length):
        if idx == 0:
            cur[0] = prev[0] + values[0]
        elif idx == length-1:
            cur[length-1] = prev[length-2] + values[length-1]
        else:
            cur[idx] = max(prev[idx-1], prev[idx]) + values[idx]
    prev = cur.copy()

print(max(cur))

# =================================================================