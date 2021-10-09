# 플로이드 2 (https://www.acmicpc.net/problem/11780)

# i번째 줄에 출력하는 j번째 숫자는 도시 i에서 j로 가는데 필요한 최소 비용이다. 만약, i에서 j로 갈 수 없는 경우에는 그 자리에 0을 출력한다.
# 도시 i에서 도시 j로 가는 최소 비용에 포함되어 있는 도시의 개수 k를 출력한다. 그 다음, 도시 i에서 도시 j로 가는 경로를 공백으로 구분해 출력한다. 이때, 도시 i와 도시 j도 출력해야 한다. 만약, i에서 j로 갈 수 없는 경우에는 0을 출력한다.

import sys

input = sys.stdin.readline

V = int(input())
E = int(input())

INF = 999999*V

dist = [[INF]*(V+1) for _ in range(V+1)]
route = [[0]*(V+1) for _ in range(V+1)]

for idx in range(V+1):
    dist[idx][idx] = 0

for _ in range(E):
    A, B, d = map(int, input().split())
    dist[A][B] = min(d, dist[A][B])

for start in range(1,V+1):
    for end in range(1,V+1):
        route[start][end] = [start, end]

for mid in range(1,V+1):
    for start in range(1,V+1):
        for end in range(1,V+1):
            if dist[start][end] > dist[start][mid] + dist[mid][end]:
                dist[start][end] = dist[start][mid] + dist[mid][end]
                route[start][end] = route[start][mid][:-1] + route[mid][end]

for y in range(1,V+1):
    for x in range(1,V+1):
        if dist[y][x] == INF:
            dist[y][x] = 0

for row in range(1,V+1):
    print(" ".join(map(str, dist[row][1:])))

for start in range(1,V+1):
    for end in range(1,V+1):
        if dist[start][end] == 0:
            print(0)
        else:
            print(len(route[start][end]), end=" ")
            print(" ".join(map(str, route[start][end])))

# =================================================================