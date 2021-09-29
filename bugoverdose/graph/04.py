# DFS와 BFS (https://www.acmicpc.net/problem/1260)
# 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
# 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
# 중요: 도달불가능한 정점도 존재함

import sys
import heapq
from collections import deque

input = sys.stdin.readline

N, M, start = map(int, input().split())

dfs = {}
bfs = {} # .copy()할 경우 value들은 reference되기 때문에 dfs에서 변경한 내역이 bfs에 그대로 반영됨 

for _ in range(M): # 간선 정보. start로부터 시작하는 간선이 없는 경우 start라는 key 자체가 없음
    A, B = map(int, input().split())

    if A in dfs.keys():
        heapq.heappush(dfs[A], B)
        heapq.heappush(bfs[A], B)
    else:
        dfs[A] = [B]
        bfs[A] = [B]

    if B in dfs.keys():
        heapq.heappush(dfs[B], A)
        heapq.heappush(bfs[B], A)
    else:
        dfs[B] = [A]
        bfs[B] = [A]

# dfs - 현재 정점 기준으로 끝가지 탐색. 끝에 도달하면 이전 정점 기준으로 탐색.
dfs_stack = [start] # 지나온 길. 연결된 모든 간선 조회. 전부 이미 간 곳이면 스택에서 빼고 그 이전 정점에서 조회.
dfs_visited = [start]

while dfs_stack:
    if len(dfs_visited) == N:
        break
    cur = dfs_stack[-1]
    if cur in dfs.keys(): # start로부터 시작하는 간선이 없는 경우 key 자체가 없음
        for _ in range(len(dfs[cur])):
            to = heapq.heappop(dfs[cur])
            if to not in dfs_visited:
                dfs_stack.append(to)
                dfs_visited.append(to)
                break
    if cur == dfs_stack[-1]: # 전혀 이동하지 못한 경우
        dfs_stack.pop()

print(' '.join(map(str, dfs_visited)))

# bfs 
bfs_queue = deque([start]) # 지나갈 수 있는 간선들. 연결된 모든 간선 조회. 전부 이미 간 곳이면 큐에서 빼고 맨 처음 정점에서 갈 수 있는 곳들을 조회.
bfs_visited = [start]

while bfs_queue:
    if len(bfs_visited) == N:
        break
    cur = bfs_queue[0]
    if cur in bfs.keys():
        for _ in range(len(bfs[cur])):
            to = heapq.heappop(bfs[cur])

            if to not in bfs_visited:
                bfs_queue.append(to)
                bfs_visited.append(to)
    bfs_queue.popleft() # 해당 정점에서 갈 수 있는 간선들 전부 순회 완료

print(' '.join(map(str, bfs_visited)))

# =================================================================
