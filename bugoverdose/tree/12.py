# 별자리 만들기 (https://www.acmicpc.net/problem/4386)
# 별들이 2차원 평면 위에 놓여 있다. 선을 하나 이을 때마다 두 별 사이의 거리만큼의 비용이 든다고 할 때, 별자리를 만드는 최소 비용을 구하시오.
# 첫째 줄에 별의 개수 n이 주어진다. (1 ≤ n ≤ 100)
# 둘째 줄부터 n개의 줄에 걸쳐 각 별의 x, y좌표가 실수 형태로 주어지며, 최대 소수점 둘째자리까지 주어진다. 좌표는 1000을 넘지 않는 양의 실수이다.

# 나의 정답 - 존재할 수 있는 모든 간선과 그 가중치(정점 간의 거리)를 다 찾고, 최소 거리들부터 하나씩 합집합 진행
import sys
from heapq import * 
from math import sqrt

input = sys.stdin.readline

N = int(input())

points = []

for _ in range(N):
    X, Y = map(float, input().split())
    points.append((X,Y))

parent = {}
for point in points:
    parent[point] = point

def find_ancestor(point):
    if parent[point] == point:
        return point
    ancestor = find_ancestor(parent[point])
    parent[point] = ancestor
    return ancestor

def connect(A, B):
    pa = find_ancestor(A)
    pb = find_ancestor(B)
    if pa == pb:
        return False
    small, big = sorted([pa, pb], key=lambda x:(x[0], x[1]))
    parent[big] = small
    return True

edges = [] # 존재 가능한 모든 간선
for i in range(N-1):
    cur = points[i]
    for j in range(i+1, N):
        next = points[j]
        d = sqrt((cur[0]-next[0])**2 + (cur[1]-next[1])**2)
        heappush(edges, (d, cur, next))

distance = 0

while edges:
    d, A, B = heappop(edges)
    if connect(A, B):
        distance += d

print(distance)

# ==================================================================
# 5
# 1.0 1.0
# 1.0 3.0
# 1.0 2.0
# 2.0 2.0
# 2.0 4.0

# 4.414213562373095

# 18
# 1.0 1.02
# 2.0 2.04
# 3.0 4.06
# 4.0 4.07
# 5.0 4.09
# 6.0 4.07
# 7.0 4.06
# 8.0 4.05
# 9.0 4.02
# 12.0 4.01
# 22.0 4.03
# 32.0 4.02
# 42.0 4.01
# 52.0 4.05
# 62.0 44.0
# 72.0 34.0
# 82.0 24.0
# 92.0 14.0

# 131.1238542867547

# print(parent)
# {(1.0, 1.02): (1.0, 1.02), (2.0, 2.04): (1.0, 1.02), (3.0, 4.06): (1.0, 1.02), (4.0, 4.07): (1.0, 1.02), (5.0, 4.09): (1.0, 1.02), (6.0, 4.07): (1.0, 1.02), (7.0, 4.06): (1.0, 1.02), (8.0, 4.05): (1.0, 1.02), (9.0, 4.02): (1.0, 1.02), (12.0, 4.01): (1.0, 1.02), (22.0, 4.03): (1.0, 1.02), (32.0, 4.02): (1.0, 1.02), (42.0, 4.01): (1.0, 1.02), (52.0, 4.05): (1.0, 1.02), (62.0, 44.0): (1.0, 1.02), (72.0, 34.0): (1.0, 1.02), (82.0, 24.0): (1.0, 1.02), (92.0, 14.0): (1.0, 1.02)}
# ==================================================================
# 오답 - 전체 간선의 합이 최소 != 임의의 정점에서의 최소거리 합 // 전체 간선들 중에서 최단 거리들 찾아야 함
import sys
from math import sqrt

input = sys.stdin.readline

N = int(input())

points = []

for _ in range(N):
    X, Y = map(float, input().split())
    points.append((X,Y))

parent = {}
for point in points:
    parent[point] = point

def find_ancestor(point):
    if parent[point] == point:
        return point
    ancestor = find_ancestor(parent[point])
    parent[point] = ancestor
    return ancestor

def connect(pa, pb):
    small, big = sorted([pa, pb], key=lambda x:(x[0], x[1]))
    parent[big] = small

distance = 0
points.sort()

while points:
    cur = points.pop(0)
    pa = find_ancestor(cur)

    parent_of_closest = (-1, -1)
    closest_distance = 2000

    for p in points:
        pb = find_ancestor(p)
        if pa == pb: continue # 서로 이미 연결된 경우 사이클 생성되므로 생략
        d = sqrt((cur[0]-p[0])**2 + (cur[1]-p[1])**2)
        if d < closest_distance:
            parent_of_closest = pb
            closest_distance = d

    if parent_of_closest == (-1, -1): continue

    connect(pa, parent_of_closest)
    distance += closest_distance

print(distance)

# ==================================================================