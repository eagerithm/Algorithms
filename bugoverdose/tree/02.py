# 트리의 지름 (https://www.acmicpc.net/problem/1167)
# 트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 트리의 지름을 구하는 프로그램을 작성하시오.

# 나의 정답 - 1) 임의의 지점에서 dfs로 본인으로부터 가장 멀리 떨어져있는 노드 탐색
#             2) 해당 노드로부터 가장 멀리 떨어져있는 노드까지의 거리를 구하면 양극단의 노드 탐색 가능
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

edge = {}

for node in range(1,N+1):
    edge[node] = []

for _ in range(N):
    cur, *info = list(map(int, input().split()))[:-1]
    for idx in range(0, len(info), 2):
        next = info[idx]
        edge[cur].append((next, info[idx+1])) # (다음 노드, 다음 노드까지의 거리)
        # edge[next].append((cur, distance)) # 1->2 정보와 2->1 정보를 모두 입력받음.

def dfs(stack, visited, prev_distance):
    max_distance = prev_distance # 다음 노드 없으면 입력받은 여태까지의 거리를 그대로 반환
    cur = stack.pop()
    the_farthest = cur
    for (next, distance) in edge[cur]:
        if not visited[next]:
            visited[next] = True
            stack.append(next)
            stack, visited, nex_max_distance, farthest = dfs(stack, visited, prev_distance+distance)
            if nex_max_distance > max_distance:
                the_farthest = farthest
                max_distance = nex_max_distance # 현재 노드 cur를 기준으로 최종적인 재귀호출 결과들끼리 비교

    return stack, visited, max_distance, the_farthest

# 1) 임의의 지점에서 dfs로 본인으로부터 가장 멀리 떨어져있는 노드 탐색
visited = [False]*(N+1)
visited[1] = True
_, _, _, first_end = dfs(deque([1]),visited,0)

# 2) 해당 노드로부터 가장 멀리 떨어져있는 노드까지의 거리를 구하면 양극단의 노드 탐색 가능
visited = [False]*(N+1)
visited[first_end] = True
_, _, distance, _ = dfs(deque([first_end]),visited,0)

print(distance)

# ==============================================================
# 시간초과 - DFS로 각 노드를 시작점으로 설정한 각 경우에 대해 모든 route 탐색하면서 최대 거리 선정
import sys

input = sys.stdin.readline

N = int(input())

edge = {}

for node in range(1,N+1):
    edge[node] = []

for _ in range(N):
    cur, *info = list(map(int, input().split()))[:-1]
    for idx in range(0, len(info), 2):
        next = info[idx]
        distance = info[idx+1]
        edge[cur].append((next, distance))
        # edge[next].append((cur, distance)) # 1->2 정보와 2->1 정보를 모두 입력받음.

max_distance = 0

def dfs(stack, visited, prev_distance):
    distances = [prev_distance]
    cur = stack.pop()
    for (next, distance) in edge[cur]:
        if not visited[next]:
            visited[next] = True
            stack.append(next)
            stack, visited, nex_max_distance = dfs(stack, visited, prev_distance+distance)
            distances.append(nex_max_distance)
    return stack, visited, max(distances)

for start in range(1,N+1):
    visited = [False]*(N+1)
    visited[start] = True
    _, _, distance = dfs([start],visited,0)

    max_distance = max(max_distance, distance)

print(max_distance)

# ==============================================================
# 5
# 1 3 2 -1
# 2 4 4 -1
# 3 1 2 4 3 -1
# 4 2 4 3 3 5 6 -1
# 5 4 6 -1

# 11

# 1-3 : 2 
# 3-4 : 3
# 4-5 : 6
# 지름: 11
# ==============================================================
# 6
# 1 2 3 -1
# 2 1 3 5 3 3 5 -1
# 3 2 5 4 7 -1
# 4 3 7 -1
# 5 2 3 6 5 -1
# 6 5 5 -1

# 20
# ==============================================================
