# 행성 터널 (https://www.acmicpc.net/problem/2887)
# 행성은 3차원 좌표위의 한 점으로 생각하면 된다. 
# 두 행성 A(xA, yA, zA)와 B(xB, yB, zB)를 터널로 연결할 때 드는 비용은 min(|xA-xB|, |yA-yB|, |zA-zB|)이다.
# 민혁이는 터널을 총 N-1개 건설해서 모든 행성이 서로 연결되게 하려고 한다. 이때, 모든 행성을 터널로 연결하는데 필요한 최소 비용을 구하는 프로그램을 작성하시오.

# 나의 정답 - 실제 모든 간선 대신, 가짜를 포함하더라도 최소거리 간선만 고려
import sys

input = sys.stdin.readline

N = int(input())

stars = []
parent = {}

for _ in range(N):
    X, Y, Z = map(int, input().split())
    stars.append((X, Y, Z))
    parent[(X, Y, Z)] = (X, Y, Z)

edges = []

for i in range(3): # x축, y축, z축 기준으로 각각 일렬로 나열하여 두개씩만 간선 생성
    stars.sort(key=lambda x:(x[i], x[(i+1)%3], x[(i+2)%3]))
    for idx in range(N-1):
        A, B = stars[idx], stars[idx+1]
        d = abs(A[i]-B[i]) 
        edges.append((d, A, B)) 
        # x/y/z 중 가장 짧은 거리가 실제 가중치 - 나머지 2개는 잘못된 정보지만 무시될 예정

def find_parent(node):
    if parent[node] == node:
        return node
    ancestor = find_parent(parent[node])
    parent[node] = ancestor
    return ancestor

def unite(A, B):
    pa = find_parent(A)
    pb = find_parent(B)
    if pa == pb: 
        return False
    pa, pb = sorted([pa, pb], key=lambda x:(x[0], x[1], x[2]))
    parent[pb] = pa
    return True

total_cost = 0

edges.sort()

for d, A, B in edges:
    if unite(A, B):
        total_cost += d

print(total_cost)

# ==================================================================
# 메모리 초과 - 모든 간선을 전부 다 고려하는 경우
import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())

stars = []
parent = {}

for _ in range(N):
    X, Y, Z = map(int, input().split())
    stars.append((X, Y, Z))
    parent[(X, Y, Z)] = (X, Y, Z)

edges = []
for c in combinations(stars, 2):
    A = c[0]
    B = c[1]
    d = min(abs(A[0]-B[0]), abs(A[1]-B[1]), abs(A[2]-B[2]))
    edges.append((d, A, B))
# for i in range(N-1):
#     for j in range(i+1,N):
#         A = stars[i]
#         B = stars[j]
#         d = min(abs(A[0]-B[0]), abs(A[1]-B[1]), abs(A[2]-B[2]))
#         edges.append((d, A, B))


def find_parent(node):
    if parent[node] == node:
        return node
    ancestor = find_parent(parent[node])
    parent[node] = ancestor
    return ancestor

def unite(A, B):
    pa = find_parent(A)
    pb = find_parent(B)
    if pa == pb: 
        return False
    pa, pb = sorted([pa, pb], key=lambda x:(x[0], x[1], x[2]))
    parent[pb] = pa
    return True

edges.sort()

total_cost = 0

for d, A, B in edges:
    if unite(A, B):
        total_cost += d

print(total_cost)

# ==================================================================