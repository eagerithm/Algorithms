# 특정한 최단경로 (https://www.acmicpc.net/problem/1504)
# 방향성이 없는 그래프
# 1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.

# 나의 정답 - 개별적으로 구하고 합치기
import sys
from heapq import heappop, heappush

input = sys.stdin.readline

V, E = map(int, input().split())
inf_distance = 999999999*V # 왔다갔다 오가는 경우도 있으므로 극한으로 높여야 함

edges = {}
for i in range(1, V+1):
    edges[i] = []

for _ in range(E):
    A, B, w = map(int, input().split())
    edges[A].append((w, B))
    edges[B].append((w, A))

v1, v2 = map(int, input().split()) 
min_routes = []
for start, end in [(1, v1), (1, v2), (v1, v2), (v1, V), (v2, V)]:
    queue = [(0, start)]
    distance = [inf_distance]*(V+1)
    distance[start] = 0
    while queue:
        _, cur = heappop(queue)
        for weight, next in edges[cur]:
            if distance[next] > distance[cur] + weight:
                distance[next] = distance[cur] + weight
                heappush(queue, (distance[next], next))
    min_routes.append(distance[end])


route1 = min_routes[0] + min_routes[2] + min_routes[4] # 1->v1->v2->N 
route2 = min_routes[1] + min_routes[2] + min_routes[3] # 1->v2->v1->N
min_route = min(route1, route2)

print(min_route if min_route < inf_distance else -1)

# ==================================================================