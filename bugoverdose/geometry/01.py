# 네 번째 점 (https://www.acmicpc.net/problem/3009)
# (x1, y1), (x1, y2), (x2, y1) => (x2, y2) 찾기

# 나의 정답 
import sys

x_list = []
y_list = []

for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    x_list.append(x)
    y_list.append(y)

x = max(x_list) if x_list.count(max(x_list)) == 1 else min(x_list)
y = max(y_list) if y_list.count(max(y_list)) == 1 else min(y_list)

print(x, y)

# =========================================