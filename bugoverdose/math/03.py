# https://www.acmicpc.net/problem/1011
 
# 나의 정답 
import sys

input = sys.stdin.readline

for line in range(int(input())):
    i = 1
    a, b = map(int, input().split())
    distance = b - a
    if distance == 1:
        print(1)
        continue
    while True:
        if i * (i+1) < distance:
            i += 1
            continue
        i -= 1
        if distance == i * (i+1): # 1 2 3 3 2 1
            print(2 * i)
        elif distance <= i * (i+1) + (i+1): # 1 2 3 4 3 2 1
            print(2 * i + 1)
        else:
            print(2 * i + 2) # 1 2 3 4 3 2 1 1  # 1 2 3 4 3 2 2 1
        break

# =========================================
# 다른 사람의 풀이 
import sys
n=int(input())

for i in range(n):
    x,y=map(int,sys.stdin.readline().split())
    a=y-x
    t=int(pow(a-1,0.5))
    if t**2<a<=t**2+t:
        print(t*2)
    else:
        print(t*2+1)

# =========================================