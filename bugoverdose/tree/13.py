# 우주신과의 교감 (https://www.acmicpc.net/problem/1774)

# 첫째 줄에 우주신들의 개수(N<=1,000) 이미 연결된 신들과의 통로의 개수(M<=1,000)가 주어진다.
# 두 번째 줄부터 N개의 줄에는 황선자를 포함하여 우주신들의 좌표가 (0<= X<=1,000,000), (0<=Y<=1,000,000)가 주어진다. 
# 그 밑으로 M개의 줄에는 이미 연결된 통로가 주어진다. 번호는 위의 입력받은 좌표들의 순서라고 생각하면 된다. 좌표는 정수이다.

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

points = []
parents = {}

for _ in range(N):
    X, Y = map(int, input().split())
    points.append((X,Y))
    parents[(X,Y)] = (X,Y)

def find_parent(point):
    if parents[point] == point:
        return point
    ancestor = find_parent(parents[point])
    parents[ancestor] = ancestor
    return ancestor

def unite(A, B):
    pa = find_parent(A)
    pb = find_parent(B)
    if pa == pb:
        return False
    pa, pb = sorted([pa, pb], key=lambda x:(x[0], x[1]))
    parents[pb] = pa
    return True

for _ in range(M):
    idx_A, idx_B = map(int, input().split())
    A = points[idx_A-1]
    B = points[idx_B-1]
    unite(A, B)

edges = []
for i in range(N-1):
    cur = points[i]
    for j in range(i+1, N):
        next = points[j]
        edges.append((((cur[0]-next[0])**2 + (cur[1]-next[1])**2)**0.5, cur, next))

edges.sort()
additional_distance = 0

for w, A, B in edges:
    if unite(A, B):
        additional_distance += w

print(f'{additional_distance:.2f}')

# ==================================================================