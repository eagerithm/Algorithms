# 트리의 지름 (https://www.acmicpc.net/problem/1167)
# 트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 트리의 지름을 구하는 프로그램을 작성하시오.

# 나의 정답 - 1) 임의의 지점에서 dfs로 본인으로부터 가장 멀리 떨어져있는 노드 탐색
#             2) 해당 노드로부터 가장 멀리 떨어져있는 노드까지의 거리를 구하면 양극단의 노드 탐색 가능
import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline

N = int(input())

edge = {}

for node in range(1,N+1):
    edge[node] = []

for _ in range(N-1):
    A, B, weight = map(int, input().split())
    edge[A].append((B, weight)) 
    edge[B].append((A, weight)) 

def dfs(stack, visited, prev_distance):
    cur = stack.pop()
    visited[cur] = 1
    max_distance = prev_distance
    farthest_node = cur
    for (next, distance) in edge[cur]:
        if visited[next] == 0:
            stack.append((next))
            visited[next] = 1
            stack, visited, new_distance, far = dfs(stack, visited, prev_distance+distance)
            if max_distance < new_distance: # 최종 재귀결과들끼리 비교
                max_distance = new_distance
                farthest_node = far
    return stack, visited, max_distance, farthest_node

_, _, _, first_end = dfs([1], [0]*(N+1), 0)
_, _, distance, _ = dfs([first_end], [0]*(N+1), 0)

print(distance)

# ==============================================================
