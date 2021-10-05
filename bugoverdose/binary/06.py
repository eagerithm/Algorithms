# 공유기 설치 (https://www.acmicpc.net/problem/2110)
# 도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.
# 집에 공유기 C개를 설치하려고 한다. 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.
# C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

N, C = map(int, input().split())

houses = [int(input()) for _ in range(N)]
houses.sort()

distances = [] # 집들 사이의 거리
for idx in range(N-1):
    distances.append(houses[idx+1]-houses[idx])

max_d = sum(distances)//(C-1)
center = (max_d+1)//2
min_d = 1

maximum = 1

while min_d <= max_d:
    counter = 1
    sum = 0
    for d in distances:
        if sum + d >= center:
            counter += 1
            sum = 0
        else:
            sum += d
    if counter >= C:
        maximum = max(maximum, center)
        min_d = center + 1
    else:
        max_d = center - 1
    center = (max_d+min_d)//2

print(maximum)

# ==================================================================
