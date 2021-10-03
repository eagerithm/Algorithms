# 최소 스패닝 트리 (https://www.acmicpc.net/problem/1197)
# 최소 스패닝 트리(MST): 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리
# 풀이 방법: 쿠르스칼 알고리즘 or 프림 알고리즘

# 그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.
# 첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다. 다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다. 이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. 
# C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.

# 나의 정답: 쿠르스칼 - 가장 짧은 간선들을 순차적으로 선택해가며 정점의 집합들 생성, 사이클이 발생하게 되는 간선은 추가X
import sys
from heapq import *

input = sys.stdin.readline

V, E = map(int, input().split())

edges = []

for _ in range(E):
    A, B, w = map(int, input().split())
    heappush(edges, (w, A, B))

parent = [i for i in range(V+1)]

def find_ancestor(node):
    if parent[node] == node:
        return node
    ancestor = find_ancestor(parent[node])
    parent[node] = ancestor
    return ancestor

def unite(A, B):
    is_cycle = False
    pa = find_ancestor(A)
    pb = find_ancestor(B)
    if pa == pb:
        is_cycle = True
    elif pa > pb:
        parent[pa] = pb
    elif pa < pb:
        parent[pb] = pa
    return is_cycle

weight_sum = 0

while edges:
    (w, A, B) = heappop(edges)
    is_cycle = unite(A, B)
    if not is_cycle:
        weight_sum += w

print(weight_sum)

# ==================================================================
# 3 3
# 1 2 1
# 2 3 2
# 1 3 3

# 3
# ==================================================================
# 3 3
# 1 2 -1
# 2 3 -2
# 1 3 -3

# -5
# ==================================================================