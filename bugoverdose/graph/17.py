# 플로이드 (https://www.acmicpc.net/problem/11404)
# 플로이드 와셜 알고리즘: 각 정점마다 두 정점 사이를 지나가는 비용 vs 자신을 경유해서 지나가는 비용을 비교
# Dab = min(Dab, Dak + Dkb) 
# 1번~V번 노드까지 순차적으로 1번씩만 순회하면 모든 경우 코버됨

# 나의 정답
import sys

input = sys.stdin.readline

V = int(input())
E = int(input())

INF = 999999*V

distances = [[INF]*(V+1) for _ in range(V+1)]
for i in range(1, V+1):
    distances[i][i] = 0
for _ in range(E):
    A, B, cost = map(int, input().split()) 
    distances[A][B] = min(cost, distances[A][B]) # 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.

# 플로이드 와셜 : Dab = min(Dab, Dak + Dkb)
for mid in range(1,V+1):
    for start in range(1,V+1):
        if start == mid: continue # 없어도 차이 없음
        for end in range(1,V+1):
            if start == end: continue
            if mid == end: continue
            distances[start][end] = min(distances[start][end], distances[start][mid] + distances[mid][end])

# 만약, i에서 j로 갈 수 없는 경우에는 그 자리에 0을 출력한다.
for i in range(1, V+1):
    for j in range(1, V+1):
        if distances[i][j] == INF:
            distances[i][j] = 0

for i in range(1, V+1):
    print(" ".join(map(str, distances[i][1:])))

# =================================================================
