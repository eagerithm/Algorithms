# 터렛 (https://www.acmicpc.net/problem/1002)
# 두 원의 교차점 개수

# 나의 정답 
import sys

input = sys.stdin.readline

for i in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5
    
    if distance == 0 and r1 == r2: # 완전히 일치하므로 무한대
        print(-1)
        continue

    if distance < abs(r1 - r2) or distance > r1 + r2:
        print(0)
    elif distance == abs(r1 - r2) or distance == r1 + r2:
        print(1)
    else: # abs(r1 - r2) < distance < r1 + r2
        print(2)

# =========================================